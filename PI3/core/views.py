from django.shortcuts import render
from django.http import HttpResponse
from .forms import EmpresaForm
from .services .ConexaoService import ConexaoService
from .services .MongoConnection  import MongoConnection

def cadastro(request):
    if request.method == 'POST':
        form = EmpresaForm(request.POST)
        if form.is_valid():
            try:
                nome = form.clean_nome()
            except forms.ValidationError:
                return HttpResponse('Nome inválido')

            
            conexao = ConexaoService()
            client = MongoConnection(conexao)
            client.insert(nome)

            return HttpResponse('Cadastro realizado com sucesso')

    else:
        return render(request, 'cadastro.php',{'form':EmpresaForm()})
    