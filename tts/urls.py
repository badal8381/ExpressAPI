from django.urls import path
from . import views

urlpatterns = [
    path('', views.tts_home, name='tts'),
    path('<str:id>/', views.download_speech, name='download-audio'),
]
