import os
from django.core.files import File
from uuid import uuid4
from django.shortcuts import render
from .models import pdfToDoc, csvToExcel, excelToCSV, pdfToImage, mergePDF
from .func import convert_csv2excel, convert_excel2csv, convert_pdf2docx, convert_pdf2image, pdf_merge


def pdf2docx(request):
    if request.method == 'POST':
        pdf = request.FILES['pdf']
        if pdf.name[-3:] != 'pdf':
            return render(request, 'doc/pdf2doc.html', {'error': True})

        id = str(uuid4())
        pdfToDoc(id=id, pdf=pdf).save()
        obj = pdfToDoc.objects.get(id=id)
        doc = convert_pdf2docx(obj.pdf.url[1:], id)

        with open(doc, 'rb') as f:
            obj.doc = File(f, f'{id}.docx')
            obj.pdf.delete()
            obj.save()

        os.remove(doc)
        return render(request, 'doc/pdf2doc.html', {'data': obj})

    return render(request, 'doc/pdf2doc.html')




def csv2excel(request):
    if request.method == 'POST':
        csv = request.FILES['csv']
        if csv.name[-3:] != 'csv':
            return render(request, 'doc/csv2excel.html', {'error': True})

        id = str(uuid4())
        csvToExcel(id=id, csv=csv).save()
        obj = csvToExcel.objects.get(id=id)
        doc = convert_csv2excel(obj.csv.url[1:], id)

        with open(doc, 'rb') as f:
            obj.excel = File(f, f'{id}.xlsx')
            obj.csv.delete()
            obj.save()

        os.remove(doc)
        return render(request, 'doc/csv2excel.html', {'data': obj})

    return render(request, 'doc/csv2excel.html')


def excel2csv(request):
    if request.method == 'POST':
        excel = request.FILES['xlsx']
        if excel.name[-4:] != 'xlsx':
            return render(request, 'doc/excel2csv.html', {'error': True})

        id = str(uuid4())
        excelToCSV(id=id, excel=excel).save()
        obj = excelToCSV.objects.get(id=id)
        doc = convert_excel2csv(obj.excel.url[1:], id)

        with open(doc, 'rb') as f:
            obj.csv = File(f, f'{id}.csv')
            obj.excel.delete()
            obj.save()

        os.remove(doc)
        return render(request, 'doc/excel2csv.html', {'data': obj})

    return render(request, 'doc/excel2csv.html')



def pdf2image(request):
    if request.method == 'POST':
        pdf = request.FILES['pdf']
        if pdf.name[-3:] != 'pdf':
            return render(request, 'doc/pdf2image.html', {'error': True})

        id = str(uuid4())
        pdfToImage(id=id, pdf=pdf).save()
        obj = pdfToImage.objects.get(id=id)
        doc = convert_pdf2image(obj.pdf.url[1:], id)

        with doc.open(mode = 'rb') as f:
            obj.image = File(f, f'{id}.zip')
            obj.pdf.delete()
            obj.save()

        os.remove(doc)
        return render(request, 'doc/pdf2image.html', {'data': obj})

    return render(request, 'doc/pdf2image.html')


def merge_pdf(request):
    if request.method == 'POST':
        pdf1 = request.FILES['pdf1']
        pdf2 = request.FILES['pdf2']
        if pdf1.name[-3:] != 'pdf' or pdf2.name[-3:] != 'pdf':
            return render(request, 'doc/mergepdf.html', {'error': True})

        id = str(uuid4())
        mergePDF(id=id, pdf1=pdf1, pdf2=pdf2).save()
        obj = mergePDF.objects.get(id=id)
        doc = pdf_merge(obj.pdf1.url[1:], obj.pdf2.url[1:], id)

        with open(doc, 'rb') as f:
            obj.pdf = File(f, f'{id}.pdf')
            obj.pdf1.delete()
            obj.pdf2.delete()
            obj.save()

        os.remove(doc)
        return render(request, 'doc/mergepdf.html', {'data': obj})

    return render(request, 'doc/mergepdf.html')