from django.urls import path
from . import views

urlpatterns = [
    path('', views.wort_liste, name='wort_liste'),
    path('wort-hinzufuegen/', views.wort_hinzufuegen, name='wort_hinzufuegen'),
]