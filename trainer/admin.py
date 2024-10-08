from django.contrib import admin
from .models import Wort, Satz, Kategorie

# Admin-Modell für Wort
@admin.register(Wort)
class WortAdmin(admin.ModelAdmin):
    list_display = ('id', 'deutsch', 'finnisch', 'kategorie')  # Zeigt die ID und Felder an
    readonly_fields = ('id',)  # ID nur lesbar machen

# Admin-Modell für Satz
@admin.register(Satz)
class SatzAdmin(admin.ModelAdmin):
    list_display = ('id', 'deutsch', 'finnisch', 'kategorie')  # Zeigt die ID und Felder an
    readonly_fields = ('id',)  # ID nur lesbar machen

# Admin-Modell für Kategorie
@admin.register(Kategorie)
class KategorieAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')  # Zeigt die ID und den Namen an
    readonly_fields = ('id',)  # ID nur lesbar machen