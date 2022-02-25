from fnmatch import translate
from uuid import uuid4
from django.db import models

class textToSpeech(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    text = models.TextField()
    lang = models.CharField(max_length=5)
    translated_text = models.TextField()
    speech = models.FileField(upload_to='tts')

    def __str__(self):
        try:
            return f'({self.lang})  {self.text[:25]}'
        except:
            return f'({self.lang})  {self.text}'