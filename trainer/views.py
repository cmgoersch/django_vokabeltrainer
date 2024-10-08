from django.shortcuts import render, redirect, get_object_or_404
from .models import Wort, Satz
from .forms import WortForm, SatzForm
import random
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView


# --- Listenansicht für Wörter und Sätze ---
class WortSatzListeView(ListView):
    template_name = 'trainer/wort_satz_liste.html'
    context_object_name = 'items'

    # Dummy QuerySet
    def get_queryset(self):
        return Wort.objects.none()  # Gib ein leeres QuerySet zurück, da die Daten in get_context_data kommen

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['wörter'] = Wort.objects.all()  # Alle Wörter holen
        context['sätze'] = Satz.objects.all()  # Alle Sätze holen
        return context


# --- Erstellen eines neuen Wortes ---
class WortErstellenView(CreateView):
    model = Wort
    form_class = WortForm
    template_name = 'trainer/wort_hinzufuegen.html'
    success_url = reverse_lazy('wort_satz_liste')


# --- Erstellen eines neuen Satzes ---
class SatzErstellenView(CreateView):
    model = Satz
    form_class = SatzForm
    template_name = 'trainer/satz_hinzufuegen.html'
    success_url = reverse_lazy('wort_satz_liste')


# --- Bearbeiten eines Wortes ---
class WortBearbeitenView(UpdateView):
    model = Wort
    form_class = WortForm
    template_name = 'trainer/wort_bearbeiten.html'
    success_url = reverse_lazy('wort_satz_liste')


# --- Bearbeiten eines Satzes ---
class SatzBearbeitenView(UpdateView):
    model = Satz
    form_class = SatzForm
    template_name = 'trainer/satz_bearbeiten.html'
    success_url = reverse_lazy('wort_satz_liste')


# --- Löschen eines Wortes ---
class WortLoeschenView(DeleteView):
    model = Wort
    template_name = 'trainer/wort_loeschen.html'
    success_url = reverse_lazy('wort_satz_liste')


# --- Löschen eines Satzes ---
class SatzLoeschenView(DeleteView):
    model = Satz
    template_name = 'trainer/satz_loeschen.html'
    success_url = reverse_lazy('wort_satz_liste')


def vokabel_uebung(request, mode):
    # Falls der Benutzer auf "Ich weiß es!" geklickt hat
    if request.method == 'POST' and 'wort_id' in request.session:
        wort_id = request.session['wort_id']
        wort = Wort.objects.get(id=wort_id)
        show_answer = True  # Antwort anzeigen
    else:
        # Zufälliges Wort auswählen und in der Session speichern
        wörter = list(Wort.objects.all())
        if not wörter:
            return render(request, 'trainer/vokabel_uebung.html', {'error': 'Keine Wörter vorhanden.'})

        wort = random.choice(wörter)
        request.session['wort_id'] = wort.id  # Speichern der Wort-ID für spätere Verwendung
        show_answer = False  # Antwort nicht anzeigen

    # Frage und Antwort entsprechend dem Modus zuweisen
    if mode == "deutsch-finnisch":
        question = wort.deutsch  # Zeige die deutsche Frage
        answer = wort.finnisch  # Zeige die finnische Antwort
    elif mode == "finnisch-deutsch":
        question = wort.finnisch  # Zeige die finnische Frage
        answer = wort.deutsch  # Zeige die deutsche Antwort
    else:  # gemischt
        # Zufällig Deutsch oder Finnisch als Frage auswählen und die Antwort passend setzen
        if random.choice([True, False]):
            question = wort.deutsch
            answer = wort.finnisch
        else:
            question = wort.finnisch
            answer = wort.deutsch

    # Rendern der Übungsseite mit der Frage und der korrekten Antwort
    return render(request, 'trainer/vokabel_uebung.html', {
        'question': question,
        'answer': answer,
        'show_answer': show_answer,
        'mode': mode
    })