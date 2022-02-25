from django.urls import path
from . import views
from . import response

urlpatterns = [
    path('png2jpg',views.png_to_jpg, name='png2jpg'),
    path('jpg2png',views.jpg_to_png, name='jpg2png'),
    path('img2pdf',views.image_to_pdf, name='img2pdf'),
    path('png2jpg/<str:id>/', response.download_jpg, name='download-jpg'),
    path('jpg2png/<str:id>/', response.download_png, name='download-png'),
    path('img2pdf/<str:id>/', response.download_pdf, name='download-pdf'),
]
