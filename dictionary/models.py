from django.db import models

class Language(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Type(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Gender(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class ConceptualWord(models.Model):
    formal = models.BooleanField()
    description = models.CharField(max_length=255)
    category = models.ForeignKey(Category, null=True)
    type = models.ForeignKey(Type, null=True)

    def __str__(self):
        return self.description

class TranslatedWord(models.Model):
    conceptual_word = models.ForeignKey(ConceptualWord)
    language = models.ForeignKey(Language)
    translation = models.CharField(max_length=100)
    gender = models.ForeignKey(Gender, null=True)

    def __str__(self):
        return self.translation
