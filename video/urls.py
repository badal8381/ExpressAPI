from django.urls import path
from . import views

urlpatterns = [
    path('videomerge', views.videomerge, name="videomerge"),
    path('video-to-audio', views.video_to_audio, name="video2audio"),

    path('download/video/<str:id>/', views.download_video, name='download-video'),
    path('download/audio/<str:id>/', views.download_audio, name='download-audio'),
    path('preview/<str:id>/', views.preview_video, name='preview-video'),
]