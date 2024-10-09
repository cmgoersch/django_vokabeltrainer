from django.db import models

class Kategorie(models.Model):
    id = models.AutoField(primary_key=True)  # Explizite ID für Kategorie
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Wort(models.Model):
    id = models.AutoField(primary_key=True)  # Explizite ID für Wort
    deutsch = models.CharField(max_length=100)
    finnisch = models.CharField(max_length=100)
    merksatz = models.TextField(null=True, blank=True)
    kategorie = models.ForeignKey(Kategorie, on_delete=models.CASCADE, null=True, default=1)

    def __str__(self):
        return f'{self.deutsch} - {self.finnisch}'

class Satz(models.Model):
    id = models.AutoField(primary_key=True)  # Explizite ID für Satz
    deutsch = models.CharField(max_length=255)
    finnisch = models.CharField(max_length=255)
    merksatz = models.TextField(null=True, blank=True)
    kategorie = models.ForeignKey(Kategorie, on_delete=models.CASCADE, null=True, default=1)

    def __str__(self):
        return f'{self.deutsch} - {self.finnisch}'