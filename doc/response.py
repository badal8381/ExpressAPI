from django.http import HttpResponse
from .models import pdfToDoc, csvToExcel, excelToCSV, pdfToImage, mergePDF


def download_docx(request, id):
    obj = pdfToDoc.objects.get(id=id)

    fl_path = obj.doc.url[1:]
    filename = 'converted.docx'

    fl = open(fl_path, 'rb')
    mime_type = 'application/vnd.openxmlformats-officedocument.wordprocessingml.document'
    response = HttpResponse(fl, content_type=mime_type)
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    return response


def download_excel(request, id):
    obj = csvToExcel.objects.get(id=id)

    fl_path = obj.excel.url[1:]
    filename = 'converted.xlsx'

    fl = open(fl_path, 'rb')
    mime_type = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    response = HttpResponse(fl, content_type=mime_type)
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    return response


def download_csv(request, id):
    obj = excelToCSV.objects.get(id=id)

    fl_path = obj.csv.url[1:]
    filename = 'converted.csv'

    fl = open(fl_path, 'rb')
    response = HttpResponse(fl, content_type='text/csv')
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    return response


def download_image(request, id):
    obj = pdfToImage.objects.get(id=id)

    fl_path = obj.image.url[1:]
    filename = 'converted.zip'

    fl = open(fl_path, 'rb')
    response = HttpResponse(fl, content_type='application/zip')
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    return response


def download_pdf(request, id):
    obj = mergePDF.objects.get(id=id)

    fl_path = obj.pdf.url[1:]
    filename = 'merged.pdf'

    fl = open(fl_path, 'rb')
    response = HttpResponse(fl, content_type='application/pdf')
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    return response