from django.shortcuts import redirect, render
from django.http import HttpResponse, JsonResponse
from .forms import EmpresaForm, PessoaForm, DoacaoForm
from .services .ConexaoService import ConexaoService
from .services .MongoConnectionService import MongoConnectionService
from .services.Repositories.FoodShareRepository import FoodShareRepository
from .services .EmpresaService import EmpresaService
from .services .PessoaFisicaService import PessoaFisicaService
from .services .DoacaoService import DoacaoService
from django.contrib.auth.decorators import login_required



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
            connection = ConexaoService()
            bd = MongoConnectionService(connection,"FoodShare")
            repository = FoodShareRepository(bd)
            empresa = EmpresaService(repository)
            erro = empresa.insert(form.cleaned_data)
            if erro is None:
                return redirect('cadastro')
        else:
            return render(request, 'cadastroJuridico.html', {'form': form})
    form = EmpresaForm()
    return render(request, 'cadastroJuridico.html',{'form':form})

def cadastro_fisico(request):
    if request.method == 'POST':
        form = PessoaForm(request.POST)
        if form.is_valid():
            connection = ConexaoService()
            bd = MongoConnectionService(connection,"FoodShare")
            repository = FoodShareRepository(bd)
            pessoa = PessoaFisicaService(repository)
            erro = pessoa.insert(form.cleaned_data)
            if erro is None:
                return redirect('cadastro')
        else:
            return render(request,'cadastroFisico.html',{'form':form})
    pessoa.__del__
    form = PessoaForm()
    return render(request,'cadastroFisico.html',{'form':form})
@login_required
def listar_empresas(request):
    conexao = ConexaoService()
    client = MongoConnectionService(conexao,'FoodShare')
    empresaRe = FoodShareRepository(client)
    empresa = EmpresaService(empresaRe)
    empresas = empresa.findOne({'cnpj':'45.445.452/4564-54'})
    if empresas:
        return render(request, 'listarEmpresas.html', {'empresas': empresas})
    else: 
        return redirect('cadastro')
    


def doacao(request):
    if request.method == 'POST':
        form = DoacaoForm(request.POST)
        if form.is_valid():
            connection = ConexaoService()
            bd = MongoConnectionService(connection,"FoodShare")
            repository = FoodShareRepository(bd)
            doacao = DoacaoService(repository)
            erro = doacao.insert(form.cleaned_data)
            if erro is None:
                return redirect('doacao')
        else:
            return render(request, 'doacao.html',{'form':form})
    form  = DoacaoForm()
    return render(request, 'doacao.html',{'form':form})