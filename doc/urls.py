from django.urls import path
from . import views
from . import response

urlpatterns = [
    path('pdf2docx', views.pdf2docx, name='pdf2docx'),
    path('csv2excel', views.csv2excel, name='csv2excel'),
    path('excel2csv', views.excel2csv, name='excel2csv'),
    path('pdf2image', views.pdf2image, name='pdf2image'),
    path('mergepdf', views.merge_pdf, name='mergepdf'),

    path('pdf2docx/<str:id>/', response.download_docx, name='download-docx'),
    path('csv2excel/<str:id>/', response.download_excel, name='download-excel'),
    path('excel2csv/<str:id>/', response.download_csv, name='download-csv'),
    path('pdf2image/<str:id>/', response.download_image, name='download-images'),
    path('mergepdf/<str:id>/', response.download_pdf, name='download-merged-pdf'),
]
