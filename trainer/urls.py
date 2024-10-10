from django.conf import settings
from django.urls import include, path
from django.contrib.auth import views as auth_views
from . import views
from .views import (
    WortSatzListeView, WortErstellenView, SatzErstellenView, WortBearbeitenView, SatzBearbeitenView,
    WortLoeschenView, SatzLoeschenView, vokabel_uebung
)

urlpatterns = [
    # Startseite und Authentifizierung
    path('', views.startseite, name='startseite'),
    path('login/', auth_views.LoginView.as_view(template_name='trainer/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),

    # Wörter und Sätze: Liste, Hinzufügen, Bearbeiten, Löschen
    path('liste/', WortSatzListeView.as_view(), name='wort_satz_liste'),
    path('wort-hinzufuegen/', WortErstellenView.as_view(), name='wort_hinzufuegen'),
    path('satz-hinzufuegen/', SatzErstellenView.as_view(), name='satz_hinzufuegen'),
    path('wort-bearbeiten/<int:pk>/', WortBearbeitenView.as_view(), name='wort_bearbeiten'),
    path('satz-bearbeiten/<int:pk>/', SatzBearbeitenView.as_view(), name='satz_bearbeiten'),
    path('wort-loeschen/<int:pk>/', WortLoeschenView.as_view(), name='wort_loeschen'),
    path('satz-loeschen/<int:pk>/', SatzLoeschenView.as_view(), name='satz_loeschen'),

    # Vokabel-Übung mit Modus-Option
    path('vokabel-uebung/', vokabel_uebung, name='vokabel_uebung'),
    path('vokabel-uebung/<str:mode>/', vokabel_uebung, name='vokabel_uebung'),

    # DeepL-Übersetzung
    path('get_translation/', views.get_translation, name='get_translation'),
]

# Debug toolbar, falls Debug-Modus aktiv ist
if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns