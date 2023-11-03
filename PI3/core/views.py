from django.shortcuts import redirect, render
from django.http import HttpResponse, JsonResponse
from .forms import EmpresaForm, PessoaForm
from .services .ConexaoService import ConexaoService
from .services .MongoConnectionService import MongoConnectionService
from .services.Repositories.FoodShareRepository import FoodShareRepository
from .services .EmpresaService import EmpresaService



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
        pass
        

def listar_empresas(request):
    conexao = ConexaoService()
    client = MongoConnectionService(conexao,'FoodShare')
    empresaRe = EmpresaRepository(client)
    empresa = EmpresaService(empresaRe)
    empresas = empresa.findOne({'cnpj':'45.445.452/4564-54'})
    if empresas:
        return render(request, 'listarEmpresas.html', {'empresas': empresas})
    else: 
        return redirect('cadastro')