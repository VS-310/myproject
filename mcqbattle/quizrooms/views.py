from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import QuizRoom
from .serializers import QuizRoomSerializer
from mcqs.models import MCQ  # Assuming MCQ model is defined in mcqs app
from quizrooms import models
DEFAULT_TOPICS = ['Science', 'CS', 'Math', 'General Knowledge', 'History']

class CreateQuizRoomView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        name = request.data.get('name')
        is_random = request.data.get('is_random', False)
        topic = request.data.get('topic')  # Assuming topic is sent in request data

        if not name:
            return Response({"error": "Room name is required."}, status=status.HTTP_400_BAD_REQUEST)

        if is_random:
            if not topic:
                return Response({"error": "Topic is required for random room creation."}, status=status.HTTP_400_BAD_REQUEST)

            # Check if there's an existing room for this topic with space
            rooms = QuizRoom.objects.filter(topic=topic, is_random=True).annotate(num_participants=models.Count('participants'))
            existing_room = rooms.filter(num_participants__lt=16).first()

            if existing_room:
                quiz_room = existing_room
            else:
                quiz_room = QuizRoom.objects.create(name=name, host=request.user, is_random=True, topic=topic)

        else:
            quiz_room = QuizRoom.objects.create(name=name, host=request.user, is_random=False)

        quiz_room.save()
        serializer = QuizRoomSerializer(quiz_room)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class JoinQuizRoomView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, room_id):
        try:
            quiz_room = QuizRoom.objects.get(id=room_id)
        except QuizRoom.DoesNotExist:
            return Response({"error": "Room not found"}, status=status.HTTP_404_NOT_FOUND)

        max_participants = 16
        if quiz_room.participants.count() >= max_participants:
            return Response({"error": "Room is full. Maximum participants reached."},
                            status=status.HTTP_400_BAD_REQUEST)

        if request.user in quiz_room.participants.all():
            return Response({"error": "You are already a participant in this room."},
                            status=status.HTTP_400_BAD_REQUEST)

        quiz_room.participants.add(request.user)
        quiz_room.save()

        serializer = QuizRoomSerializer(quiz_room)
        return Response(serializer.data, status=status.HTTP_200_OK)