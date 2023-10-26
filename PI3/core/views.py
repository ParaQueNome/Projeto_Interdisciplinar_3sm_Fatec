from django.shortcuts import render
from .models import Empresas

def cadastro(request):
    return render(request, 'cadastro.php')
    empresa = Empresas.save( )