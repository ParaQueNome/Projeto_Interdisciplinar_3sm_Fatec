from django.shortcuts import redirect, render
from django.http import HttpResponse, JsonResponse
from django import forms
from .forms import EmpresaForm, PessoaForm
from .services .ConexaoService import ConexaoService
from .services .MongoConnection  import MongoConnection


def cadastro(request):
    
    if request.method == 'POST':
        tipo_cadastro = request.POST.get('tipo_cadastro')

        if tipo_cadastro == 'juridica':
            return redirect('cadastro_juridico')
        elif tipo_cadastro == 'fisica':
            return redirect('cadastro_fisico')
    return render(request, 'cadastro.html')
    
    

def cadastro_juridico(request):
    if request.method == 'POST':
        form = EmpresaForm(request.POST)
        if form.is_valid():
            # Lógica para lidar com o formulário válido
            # Isso pode incluir salvar os dados no banco de dados
            nome = form.cleaned_data.get('nome')
            email = form.cleaned_data.get('email')
            cnpj = form.cleaned_data.get('cnpj')
            conexao = ConexaoService()
            client = MongoConnection(conexao)
            client.insert(nome=nome, email=email, cnpj=cnpj)
            
            # Redirecionar para uma página de sucesso ou qualquer outra página desejada
            return redirect('pagina_de_sucesso')
        else:
            # Se o formulário não for válido, retorne o formulário com os erros
            return render(request, 'cadastroJuridico.html', {'form': form})

    # Se o método da requisição não for POST ou se não houver uma solicitação POST válida,
    # renderize o formulário vazio
    form = EmpresaForm()
    return render(request, 'cadastroJuridico.html', {'form': form})
    
def cadastro_fisico(request):
    if request.method == 'POST':
        form = PessoaForm(request.POST)
        if form.is_valid():
            # Lógica para lidar com o formulário válido
            # Isso pode incluir salvar os dados no banco de dados
            nome = form.cleaned_data.get('nome')
            email = form.cleaned_data.get('email')
            cnpj = form.cleaned_data.get('cnpj')
            conexao = ConexaoService()
            client = MongoConnection(conexao)
            client.insert(nome=nome, email=email, cnpj=cnpj)
            
            # Redirecionar para uma página de sucesso ou qualquer outra página desejada
            return redirect('pagina_de_sucesso')
        else:
            # Se o formulário não for válido, retorne o formulário com os erros
            return render(request, 'cadastroFisico.html', {'form': form})

    # Se o método da requisição não for POST ou se não houver uma solicitação POST válida,
    # renderize o formulário vazio
    form = PessoaForm()
    return render(request, 'cadastroFisico.html', {'form': form})