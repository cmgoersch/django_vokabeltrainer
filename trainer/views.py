from django.shortcuts import render, redirect, get_object_or_404
from .models import Wort, Satz, Kategorie
from .forms import WortForm, SatzForm


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

    # View zum Löschen eines Wortes
def wort_loeschen(request, id):
    wort = get_object_or_404(Wort, id=id)
    wort.delete()  # Löschen des Wortes
    return redirect('wort_satz_liste')  # Zurück zur Liste nach dem Löschen

# View zum Löschen eines Satzes
def satz_loeschen(request, id):
    satz = get_object_or_404(Satz, id=id)
    satz.delete()  # Löschen des Satzes
    return redirect('wort_satz_liste')  # Zurück zur Liste nach dem Löschen


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