from uuid import uuid4
from django.db import models

class pngToJpg(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    png = models.FileField(upload_to='img/temp')
    jpg = models.FileField(upload_to='img/jpg')

    def __str__(self):
        return str(self.id)


class jpgToPng(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    jpg = models.FileField(upload_to='img/temp')
    png = models.FileField(upload_to='img/png')

    def __str__(self):
        return str(self.id)


class imgToPdf(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    img = models.FileField(upload_to='img/temp')
    pdf = models.FileField(upload_to='img/pdf')

    def __str__(self):
        return str(self.id)