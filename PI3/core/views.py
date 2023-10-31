from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django import forms
from .forms import EmpresaForm
from .services .ConexaoService import ConexaoService
from .services .MongoConnection  import MongoConnection


def cadastro(request):
    if request.method == 'POST':
        form = EmpresaForm(request.POST)
        if form.is_valid():
            nome = form.cleaned_data['nome']
        
            



            return render(request, 'cadastro.html', {'form': form})  # Por exemplo, renderize uma página de sucesso
        else:
            
            return render(request, 'cadastro.html', {'form': form})
    else:
        form = EmpresaForm()
        return render(request, 'cadastro.html', {'form': form})