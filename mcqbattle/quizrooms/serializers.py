# quizrooms/serializers.py

from rest_framework import serializers
from .models import QuizRoom
from mcqs.models import MCQ  # Import the MCQ model

class QuizRoomSerializer(serializers.ModelSerializer):
    mcqs = serializers.PrimaryKeyRelatedField(queryset=MCQ.objects.all(), many=True, required=False)

    class Meta:
        model = QuizRoom
        fields = ['id', 'name', 'host', 'created_at', 'is_random', 'participants', 'mcqs']
        read_only_fields = ['host', 'participants']