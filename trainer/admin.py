from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Wort, Kategorie

admin.site.register(Wort)
admin.site.register(Kategorie)