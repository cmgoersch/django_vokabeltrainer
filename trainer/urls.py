from django.conf import settings
from django.urls import include, path
from .views import (
    WortSatzListeView, WortErstellenView, SatzErstellenView, WortBearbeitenView, SatzBearbeitenView,
    WortLoeschenView, SatzLoeschenView, vokabel_uebung
)

urlpatterns = [
    # URLs für die Liste, Hinzufügen, Bearbeiten und Löschen von Wörtern und Sätzen
    path('', WortSatzListeView.as_view(), name='wort_satz_liste'),  # Verwendung der Class-based View
    path('wort-hinzufuegen/', WortErstellenView.as_view(), name='wort_hinzufuegen'),
    path('satz-hinzufuegen/', SatzErstellenView.as_view(), name='satz_hinzufuegen'),
    path('wort-loeschen/<int:pk>/', WortLoeschenView.as_view(), name='wort_loeschen'),
    path('satz-loeschen/<int:pk>/', SatzLoeschenView.as_view(), name='satz_loeschen'),

    # URLs für das Bearbeiten von Wörtern und Sätzen
    path('wort-bearbeiten/<int:pk>/', WortBearbeitenView.as_view(), name='wort_bearbeiten'),
    path('satz-bearbeiten/<int:pk>/', SatzBearbeitenView.as_view(), name='satz_bearbeiten'),

    # URL für die Vokabel-Übung (mit und ohne Modus)
    path('vokabel-uebung/', vokabel_uebung, name='vokabel_uebung'),
    path('vokabel-uebung/<str:mode>/', vokabel_uebung, name='vokabel_uebung'),
]

# Debug toolbar, falls Debug-Modus aktiv ist
if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns