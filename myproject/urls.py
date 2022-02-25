from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('base.urls')),
    path('doc/', include('doc.urls')),
    path('tts/', include('tts.urls')),
    path('img/', include('img.urls')),
    path('video/', include('video.urls')),
]

