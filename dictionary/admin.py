from django.contrib import admin

from .models import Language, ConceptualWord, TranslatedWord

admin.site.register(Language)
admin.site.register(ConceptualWord)
admin.site.register(TranslatedWord)