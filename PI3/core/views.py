from django.shortcuts import render
from django.http import HttpResponse
from .models import Empresas
from .forms import EmpresaForm

def cadastro(request):
    if request.method == 'POST':
        form = EmpresaForm(request.POST)
        if form.is_valid():
            try:
                nome = form.clean_nome()
            except forms.ValidationError:
                return HttpResponse('Nome inválido')

            empresa = Empresas(nome = nome)
            empresa.save()

            return HttpResponse('Cadastro realizado com sucesso')

    else:
        return render(request, 'cadastro.php',{'form':EmpresaForm()})
    