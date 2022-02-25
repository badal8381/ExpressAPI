from django.http import HttpResponse
from .models import jpgToPng, pngToJpg, imgToPdf

def download_jpg(request, id):
    obj = pngToJpg.objects.get(id=id)

    fl_path = obj.jpg.url[1:]
    filename = 'converted.jpg'

    fl = open(fl_path, 'rb')
    response = HttpResponse(fl, content_type='image/jpeg')
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    return response


def download_png(request, id):
    obj = jpgToPng.objects.get(id=id)

    fl_path = obj.png.url[1:]
    filename = 'converted.png'

    fl = open(fl_path, 'rb')
    response = HttpResponse(fl, content_type='image/png')
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    return response


def download_pdf(request, id):
    obj = imgToPdf.objects.get(id=id)

    fl_path = obj.pdf.url[1:]
    filename = 'converted.pdf'

    fl = open(fl_path, 'rb')
    response = HttpResponse(fl, content_type='application/pdf')
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    return response