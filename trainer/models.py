from django.db import models

class Kategorie(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Wort(models.Model):
    deutsch = models.CharField(max_length=100)
    finnisch = models.CharField(max_length=100)
    merksatz = models.TextField(null=True, blank=True)  # Neues Feld für den Merksatz
    kategorie = models.ForeignKey(Kategorie, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.deutsch} - {self.finnisch}'

class Satz(models.Model):
    deutsch = models.CharField(max_length=255)
    finnisch = models.CharField(max_length=255)
    merksatz = models.TextField(null=True, blank=True)  # Neues Feld für den Merksatz
    kategorie = models.ForeignKey(Kategorie, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.deutsch} - {self.finnisch}'