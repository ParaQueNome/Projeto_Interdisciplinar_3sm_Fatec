from django.shortcuts import render
from .models import Empresas

def cadastro(request):
    empresas = Empresas(nome ='JAVA')
    empresas.save()
    return render(request, 'cadastro.php')
    