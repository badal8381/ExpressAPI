from django.contrib import admin
from .models import pdfToDoc, csvToExcel, excelToCSV, pdfToImage, mergePDF

admin.site.register(pdfToDoc)
admin.site.register(csvToExcel)
admin.site.register(excelToCSV)
admin.site.register(pdfToImage)
admin.site.register(mergePDF)
