from django.conf import settings
from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.wort_satz_liste, name='wort_satz_liste'),
    path('wort-hinzufuegen/', views.wort_hinzufuegen, name='wort_hinzufuegen'),
    path('satz-hinzufuegen/', views.satz_hinzufuegen, name='satz_hinzufuegen'),

    # URLs für das Löschen
    path('wort-loeschen/<int:id>/', views.wort_loeschen, name='wort_loeschen'),
    path('satz-loeschen/<int:id>/', views.satz_loeschen, name='satz_loeschen'),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns