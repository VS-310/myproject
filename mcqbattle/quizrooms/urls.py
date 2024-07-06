# quizrooms/urls.py

from django.urls import path
from .views import CreateQuizRoomView, JoinQuizRoomView

urlpatterns = [
    path('create/', CreateQuizRoomView.as_view(), name='create-quiz-room'),
    path('join/<uuid:room_id>/', JoinQuizRoomView.as_view(), name='join-quiz-room'),
    # Add more paths as needed for quiz rooms functionality
]