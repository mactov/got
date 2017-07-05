from django.contrib import admin

from .models import Language, ConceptualWord, TranslatedWord, Category, Type, Gender

admin.site.register(Language)
admin.site.register(ConceptualWord)
admin.site.register(TranslatedWord)
admin.site.register(Category)
admin.site.register(Type)
admin.site.register(Gender)
