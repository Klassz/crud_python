from django.shortcuts import render, redirect
from app.forms import MembrosForm
from app.models import Membros

def home(request):
    data = {}
    data['db'] = Membros.objects.all()

    return render(request, "index.html", data)

def form(request):
    data= {}
    data['form'] = MembrosForm()
    return render(request,"form.html", data)

def create(request):
    form = MembrosForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')

def view(request, pk):
    data = {}
    data['db'] = Membros.objects.get(pk = pk)
    return render(request, 'view.html', data)

def edit(request, pk):
    data = {}
    data['db'] = Membros.objects.get(pk = pk)
    data['form'] = MembrosForm(instance=data['db'])
    return render(request, 'form.html', data)

def update(request, pk):
    data = {}
    data['db'] = Membros.objects.get(pk = pk)
    form = MembrosForm(request.POST or None, instance= data['db'])
    if form.is_valid():
        form.save()
    return redirect('home')

def delete(request, pk):
    data = {}
    db = Membros.objects.get(pk = pk)
    db.delete()
    return redirect('home')







