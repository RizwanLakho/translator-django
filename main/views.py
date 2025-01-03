from django.shortcuts import render
from django.http import HttpResponse
from translate import Translator

def home(request):
    context = {
        'translated_text': '',
        'original_text': '',
        'selected_language': ''
    }
    
    if request.method == 'POST':
        text = request.POST.get('translate', '')
        language = request.POST.get('language', '')
        try:
            translator = Translator(to_lang=language)
            translation = translator.translate(text)
            context['translated_text'] = translation
            context['original_text'] = text
            context['selected_language'] = language
        except Exception as e:
            context['translated_text'] = "Translation error. Please try again."
    
    return render(request, 'main/home.html', context)