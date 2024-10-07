from django.db import models

class Kategorie(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Wort(models.Model):
    deutsch = models.CharField(max_length=100)
    finnisch = models.CharField(max_length=100)
    kategorie = models.ForeignKey(Kategorie, on_delete=models.CASCADE, verbose_name="Wörter")

    def __str__(self):
        return f'{self.deutsch} - {self.finnisch}'