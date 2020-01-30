from django.shortcuts import render,redirect
from .models import Salon,Branch,SalonForm

def show(request):
    forms = Salon.objects.all()
    return render(request, 'darjano/show.html',{'forms':forms})

def create(request):
    if request.method == 'POST':
        forms = SalonForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('/darjano/show')
        else:
            return redirect('/darjano/create')
    else:
        forms = SalonForm()
        return render(request, 'darjano/create.html',{'forms':forms})