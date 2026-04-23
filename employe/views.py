from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Employe
from .forms import EmployeForm

@login_required
def liste_employes(request):
    employes = Employe.objects.all()
    return render(request, 'employe/list.html', {'employes' : employes})

@login_required
def ajouter_employe(request):
    form = EmployeForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('liste_employes')
    return render(request, 'employe/formulaire.html', {'form' : form})

@login_required
def modifier_employe(request, id):
    employe = get_object_or_404(Employe, id=id)
    form = EmployeForm(request.POST or None, instance=employe)
    if form.is_valid():
        form.save()
        return redirect('liste_employes')
    return render(request, 'employe/formulaire.html', {'form': form})

@login_required
def supprimer_employe(request, id):
    employe = get_object_or_404(Employe, id=id)
    if request.method == "POST":
        employe.delete()
        return redirect('liste_employes')
    return render(request, 'employe/confirmer_suppression.html', {'employe' : employe})