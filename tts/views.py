import os
from uuid import uuid4
from django.http import HttpResponse
from django.shortcuts import render
from .func import translate_text, text_to_speech
from .models import textToSpeech
from django.core.files import File

def tts_home(request):
    if request.method == 'POST':
        text = request.POST['text']
        lang = request.POST['lang']
        translated = translate_text(text, lang)
        speech = text_to_speech(translated,lang)
        id = str(uuid4())
        with open(speech, 'rb') as f:
            textToSpeech(id = id, text = text, lang = lang, translated_text = translated, speech=File(f, f'{id}.mp3')).save()
        os.remove(speech)
        obj = textToSpeech.objects.get(id=id)
        return render(request, 'tts/tts.html', {'data':obj})

    return render(request, 'tts/tts.html')


def download_speech(request, id):
    obj = textToSpeech.objects.get(id=id)

    fl_path = obj.speech.url[1:]
    filename = 'speech.mp3'

    fl = open(fl_path, 'rb')
    response = HttpResponse(fl, content_type='audio/mpeg')
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    return response

