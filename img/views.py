from doctest import DocTestFinder
import os
from uuid import uuid4
from django.shortcuts import render
from .models import pngToJpg, jpgToPng, imgToPdf
from .func import jpg2png, png2jpg, image2pdf
from django.core.files import File


def png_to_jpg(request):
    if request.method == 'POST':
        image = request.FILES['png']
        if image.name[-3:] != 'png':
            return render(request, 'img/png2jpg.html', {'error':True})
        
        id = str(uuid4())
        pngToJpg(id=id, png=image).save()
        obj = pngToJpg.objects.get(id=id)
        img = png2jpg(obj.png.url[1:], id)
        with open(img, 'rb') as f:
            obj.jpg = File(f, f'{id}.jpg')
            obj.png.delete()
            obj.save()

        os.remove(img)
        return render(request, 'img/png2jpg.html', {'data':obj})

    return render(request, 'img/png2jpg.html')
    




def jpg_to_png(request):
    if request.method == 'POST':
        image = request.FILES['jpg']
        if image.name[-3:] != 'jpg':
            return render(request, 'img/jpg2png.html', {'error':True})
        
        id = str(uuid4())
        jpgToPng(id=id, jpg=image).save()
        obj = jpgToPng.objects.get(id=id)
        img = jpg2png(obj.jpg.url[1:], id)
        with open(img, 'rb') as f:
            obj.png = File(f, f'{id}.png')
            obj.jpg.delete()
            obj.save()

        os.remove(img)
        return render(request, 'img/jpg2png.html', {'data':obj})

    return render(request, 'img/jpg2png.html')


def image_to_pdf(request):
    if request.method == 'POST':
        image = request.FILES['img']
        if image.name[-3:] not in ['jpg','png']:
            return render(request, 'img/img2pdf.html', {'error':True})
        
        id = str(uuid4())
        imgToPdf(id=id, img=image).save()
        obj = imgToPdf.objects.get(id=id)
        doc = image2pdf(obj.img.url[1:], id)
        with open(doc, 'rb') as f:
            obj.pdf = File(f, f'{id}.pdf')
            obj.img.delete()
            obj.save()

        os.remove(doc)
        return render(request, 'img/img2pdf.html', {'data':obj})

    return render(request, 'img/img2pdf.html')