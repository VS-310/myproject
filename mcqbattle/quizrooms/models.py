# quizrooms/models.py

import uuid
from django.db import models
from auth_app.models import User  # Assuming User model is in auth_app
from mcqs.models import MCQ  # Assuming MCQ model is defined in mcqs app

class QuizRoom(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    host = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    is_random = models.BooleanField(default=False)
    participants = models.ManyToManyField(User, related_name='rooms')
    mcqs = models.ManyToManyField(MCQ)

    def __str__(self):
        return self.name