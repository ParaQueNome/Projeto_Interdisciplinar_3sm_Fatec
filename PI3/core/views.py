from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django import forms
from .forms import EmpresaForm
from .services .ConexaoService import ConexaoService
from .services .MongoConnection  import MongoConnection


def cadastro(request):
    
    if request.method == 'POST':
        tipo_cadastro = request.POST.get('tipo_cadastro')

        if tipo_cadastro == 'juridica':
            form = EmpresaForm(request.POST)
            if form.is_valid():
                
                template = 'cadastroFisico.html'
                contexto = {'form':form}
                return render(request, template,contexto)
            else:
                return render(request, 'cadastroFisico.html',{'form':form})
    
    return render(request,'cadastro.html')