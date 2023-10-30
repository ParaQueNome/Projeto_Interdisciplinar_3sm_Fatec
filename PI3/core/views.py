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
            try:

                nome = form.clean_nome()
                email = form.clean_email()
                cnpj = form.clean_cnpj()
                cep = form.cleanCep()
                numero = form.cleanNumero()
                senha = form.cleanSenha()
            
            except forms.ValidationError as e:
                return render(request, 'cadastro.html', {'form': form})
            

            
            conexao = ConexaoService()
            client = MongoConnection(conexao)
            client.insert(nome = nome, email = email,cnpj = cnpj, cep=cep,numero = numero, password = senha)
            
            return render(request, 'cadastro.html',{'form':EmpresaForm()})
        
    else:
        return render(request, 'cadastro.html',{'form':EmpresaForm()})
    