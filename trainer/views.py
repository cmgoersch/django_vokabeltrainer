from django.shortcuts import render, redirect, get_object_or_404
from .models import Wort, Satz, Kategorie
from .forms import WortForm, SatzForm
import random


def wort_satz_liste(request):
    wörter = Wort.objects.all()  # Hol nur die Wörter
    sätze = Satz.objects.all()    # Hol nur die Sätze
    return render(request, 'trainer/wort_satz_liste.html', {'wörter': wörter, 'sätze': sätze})

# View zum Hinzufügen eines neuen Wortes
def wort_hinzufuegen(request):
    if request.method == 'POST':
        form = WortForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('wort_satz_liste')  # Zurück zur Liste der Wörter und Sätze
    else:
        form = WortForm()
    
    return render(request, 'trainer/wort_hinzufuegen.html', {'form': form})

# View zum Hinzufügen eines neuen Satzes
def satz_hinzufuegen(request):
    if request.method == 'POST':
        form = SatzForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('wort_satz_liste')  # Zurück zur Liste der Wörter und Sätze
    else:
        form = SatzForm()
    
    return render(request, 'trainer/satz_hinzufuegen.html', {'form': form})

    # View zum Löschen eines Wortes# Funktion zum Löschen eines Wortes
def wort_loeschen(request, pk):
    wort = get_object_or_404(Wort, pk=pk)  # Das Wort-Objekt anhand der pk holen
    if request.method == 'POST':
        wort.delete()  # Das Wort löschen
        return redirect('wort_satz_liste')  # Zurück zur Liste
    return redirect('wort_satz_liste')  # Falls kein POST-Request, zurück zur Liste

# Funktion zum Löschen eines Satzes
def satz_loeschen(request, pk):
    satz = get_object_or_404(Satz, pk=pk)  # Das Satz-Objekt anhand der pk holen
    if request.method == 'POST':
        satz.delete()  # Den Satz löschen
        return redirect('wort_satz_liste')  # Zurück zur Liste
    return redirect('wort_satz_liste')  # Falls kein POST-Request, zurück zur Liste

# Bearbeiten eines Wortes
def wort_bearbeiten(request, pk):
    wort = get_object_or_404(Wort, pk=pk)
    if request.method == 'POST':
        form = WortForm(request.POST, instance=wort)
        if form.is_valid():
            wort = form.save(commit=False)
            wort.kategorie = Kategorie.objects.get(name='Wort')  # Kategorie bleibt Wort
            wort.save()
            return redirect('wort_satz_liste')
    else:
        form = WortForm(instance=wort)
    
    return render(request, 'trainer/wort_bearbeiten.html', {'form': form})

# Bearbeiten eines Satzes
def satz_bearbeiten(request, pk):
    satz = get_object_or_404(Satz, pk=pk)
    if request.method == 'POST':
        form = SatzForm(request.POST, instance=satz)
        if form.is_valid():
            satz = form.save(commit=False)
            satz.kategorie = Kategorie.objects.get(name='Satz')  # Kategorie bleibt Satz
            satz.save()
            return redirect('wort_satz_liste')
    else:
        form = SatzForm(instance=satz)
    
    return render(request, 'trainer/satz_bearbeiten.html', {'form': form})

def vokabel_uebung(request, mode):
    wörter = list(Wort.objects.all())  # Alle Wörter abrufen
    if not wörter:
        return render(request, 'trainer/vokabel_uebung.html', {'error': 'Keine Wörter vorhanden.'})
    
    # Zufälliges Wort auswählen
    wort = random.choice(wörter)

    # Überprüfen, ob der Benutzer auf "Ich weiß es!" geklickt hat
    if request.method == 'POST':
        show_answer = True  # Antwort anzeigen
    else:
        show_answer = False  # Antwort nicht anzeigen

    # Modus überprüfen und entsprechend das Wort anzeigen
    if mode == "deutsch-finnisch":
        question = wort.deutsch
        answer = wort.finnisch
    elif mode == "finnisch-deutsch":
        question = wort.finnisch
        answer = wort.deutsch
    else:  # gemischt
        if random.choice([True, False]):
            question = wort.deutsch
            answer = wort.finnisch
        else:
            question = wort.finnisch
            answer = wort.deutsch

    return render(request, 'trainer/vokabel_uebung.html', {
        'question': question,
        'answer': answer,
        'show_answer': show_answer,
        'mode': mode
    })