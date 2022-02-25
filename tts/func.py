from uuid import uuid4
from gtts import gTTS
from googletrans import Translator

speech_path = f'media/tts/temp/{str(uuid4())}.mp3'

text = 'Let’s Consider a dataset of a shopping store having data about Customer Serial Number, Customer Name, Customer ID, and Product Cost stored in Excel file'

def translate_text(text, lang):
    translator = Translator(service_urls=['translate.google.co.in'])
    translated = translator.translate(text, dest=lang)
    return translated.text

def text_to_speech(text, lang):
    tts = gTTS(text, lang=lang, tld='co.in')
    tts.save(speech_path)
    return speech_path
