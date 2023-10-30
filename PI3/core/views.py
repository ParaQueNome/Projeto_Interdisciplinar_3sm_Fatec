from django.shortcuts import render
from django.http import HttpResponse
from django import forms
from .forms import EmpresaForm
from .services .ConexaoService import ConexaoService
from .services .MongoConnection  import MongoConnection


def cadastro(request):
    if request.method == 'POST':
        form = EmpresaForm(request.POST)
        if form.is_valid():
            try:

                nome = form.clean_nome()
                email = form.clean_email()
                cnpj = form.clean_cnpj()
            
            except Exception as e:
                return HttpResponse(f'Erro: {str(e)}')

            
            conexao = ConexaoService()
            client = MongoConnection(conexao)
            client.insert(nome = nome, email = email,cnpj = cnpj)
            
            return render(request, 'cadastro.html',{'form':EmpresaForm()})

    else:
        return render(request, 'cadastro.html',{'form':EmpresaForm()})
    