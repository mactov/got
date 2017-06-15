from django.db import models

class Language(models.Model):
    name = models.CharField(max_length=50)

class ConceptualWord(models.Model):
    formal = models.BooleanField()
    description = models.CharField(max_length=255)

class TranslatedWord(models.Model):
    conceptual_word = models.ForeignKey(ConceptualWord)
    language = models.ForeignKey(Language)
    translation = models.CharField(max_length=100)