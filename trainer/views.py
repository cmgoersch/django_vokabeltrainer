from django.shortcuts import render, redirect
from .models import Wort
from .forms import WortForm

def wort_liste(request):
    wörter = Wort.objects.all()
    return render(request, 'trainer/wortliste.html', {'wörter': wörter})

def wort_hinzufuegen(request):
    if request.method == 'POST':
        form = WortForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('wort_liste')
    else:
        form = WortForm()
    return render(request, 'trainer/wort_hinzufuegen.html', {'form': form})