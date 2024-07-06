"""
URL configuration for mcqbattle project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# mcqbattle/urls.py

from django.contrib import admin
from django.urls import path, include
from auth_app.views import LoginView, ProtectedView, RegisterView
# from mcqs.views import MCQListCreateView, MCQRetrieveUpdateDestroyView
# from quizrooms import urls as quizroom_urls  # Import quizroom urls

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('quiz-room/', include('quizrooms.urls')),  # Include quiz room URLs
    # path('register/', RegisterView.as_view(), name='register'),
    # path('login/', LoginView.as_view(), name='login'),
    # path('protected/', ProtectedView.as_view(), name='protected'),
    # path('mcqs/', MCQListCreateView.as_view(), name='mcq-list-create'),
    # path('mcqs/<uuid:pk>/', MCQRetrieveUpdateDestroyView.as_view(), name='mcq-detail'),
]

# Append the urlpatterns from quizroom_urls
# urlpatterns += quizroom_urls.urlpatterns