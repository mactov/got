from django.shortcuts import get_object_or_404, get_list_or_404, render
from django.http import HttpResponse
# from django.template import loader

from .models import TranslatedWord


def index(request):
    context = {
    }
    return render(request, 'dictionary/index.html', context)


def translate(request, word):
    found_word = get_object_or_404(TranslatedWord, translation=word)
    if found_word:
        translations = get_list_or_404(TranslatedWord, conceptual_word=found_word.conceptual_word)
        translations.remove(found_word)
    context = {
        'translations': translations,
        'word': found_word,
    }
    return render(request, 'dictionary/index.html', context)
