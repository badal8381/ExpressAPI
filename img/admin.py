from django.contrib import admin
from .models import jpgToPng, pngToJpg, imgToPdf

admin.site.register(jpgToPng)
admin.site.register(pngToJpg)
admin.site.register(imgToPdf)
