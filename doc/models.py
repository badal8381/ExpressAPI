from uuid import uuid4
from django.db import models

class pdfToDoc(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    pdf = models.FileField(upload_to='documents/temp')
    doc = models.FileField(upload_to='documents/docx')

    def __str__(self):
        return str(self.id)

class excelToCSV(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    excel = models.FileField(upload_to='documents/temp')
    csv = models.FileField(upload_to='documents/csv')

    def __str__(self):
        return str(self.id)

class csvToExcel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    csv = models.FileField(upload_to='documents/temp')
    excel = models.FileField(upload_to='documents/excel')

    def __str__(self):
        return str(self.id)


class pdfToImage(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    pdf = models.FileField(upload_to='documents/temp')
    image = models.FileField(upload_to='documents/image')

    def __str__(self):
        return str(self.id)


class mergePDF(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    pdf1 = models.FileField(upload_to='documents/temp')
    pdf2 = models.FileField(upload_to='documents/temp')
    pdf = models.FileField(upload_to='documents/pdf')

    def __str__(self):
        return str(self.id)