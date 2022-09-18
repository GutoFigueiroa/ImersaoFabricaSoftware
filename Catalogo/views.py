from django.shortcuts import render, redirect
from .models import Catalogo
from .forms import Formulariocatalogo

def home(request):
    catalogo = Catalogo.objects.all()
    data={}
    data['catalogo'] = catalogo

    return render(request, 'catalogo/home.html', data)

def create(request):
    form = Formulariocatalogo(request.POST or None)
    data = {}
    data['form'] = form

    if form.is_valid():
        form.save()
        return redirect('home')

    return render(request, 'catalogo/create.html', data)

def leitura(request, pk):
    catalogo = Catalogo.objects.get(pk=pk)
    data={}
    data['catalogo'] = catalogo

    return render(request, 'catalogo/leitura.html', data)

def update(request, pk):
    catalogo = Catalogo.objects.get(pk=pk)
    form = Formulariocatalogo(request.POST or None, instance=catalogo)
    data={}
    data['catalogo'] = catalogo
    data['form'] = form
    
    if form.is_valid():
        form.save()
        return redirect('home')

    return render(request, 'catalogo/update.html', data)

def delete(request, pk):
    catalogo = Catalogo.objects.get(pk=pk)
    catalogo.delete()

    return redirect('home')



    
