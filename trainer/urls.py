from django.conf import settings
from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.wort_satz_liste, name='wort_satz_liste'),
    path('wort-hinzufuegen/', views.wort_hinzufuegen, name='wort_hinzufuegen'),
    path('satz-hinzufuegen/', views.satz_hinzufuegen, name='satz_hinzufuegen'),
    path('wort-loeschen/<int:pk>/', views.wort_loeschen, name='wort_loeschen'),
    path('satz-loeschen/<int:pk>/', views.satz_loeschen, name='satz_loeschen'),
    
    # URLs für das Bearbeiten
    path('wort-bearbeiten/<int:pk>/', views.wort_bearbeiten, name='wort_bearbeiten'),
    path('satz-bearbeiten/<int:pk>/', views.satz_bearbeiten, name='satz_bearbeiten'),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns