from django.shortcuts import redirect, render
from django.http import HttpResponse, JsonResponse
from .forms import EmpresaForm, PessoaForm, DoacaoForm, LoginForm
from .services .ConexaoService import ConexaoService
from .services .MongoConnectionService import MongoConnectionService
from .services.Repositories.FoodShareRepository import FoodShareRepository
from .services .EmpresaService import EmpresaService
from .services .PessoaFisicaService import PessoaFisicaService
from .services .DoacaoService import DoacaoService
from .services .SessionService import SessionService
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
            bd = MongoConnectionService(connection, "FoodShare")
            repository = FoodShareRepository(bd)
            pessoa = PessoaFisicaService(repository)
            erro = pessoa.insert(form.cleaned_data)
            if erro is None:
                return redirect('cadastro')
        else:
            return render(request, 'cadastroFisico.html', {'form': form})
    
    
    form = PessoaForm()
    return render(request, 'cadastroFisico.html', {'form': form})

    


def doacao(request):
    if 'user_id' not in request.session:
        
        return redirect('login')
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
    return render(request, 'doacao.html',{'form':form,'session': request.session.get('username')})

def pagamento(request):
    pass

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            connection = ConexaoService()
            bd = MongoConnectionService(connection,"FoodShare")
            repository = FoodShareRepository(bd)
            login = SessionService(repository)
            collection = login.verifyUser(form.cleaned_data)
            erro = login.authenticate(collection,form.cleaned_data)
            print(erro)
            if erro:
                context = {'form':form, 'erro':'Credenciais inválidas'}
                return render(request, 'login.html', context)
            session = login.sessionInit(request,collection,form.cleaned_data)
            print(session)
            if session is None:
                return redirect('doacao') 
        else:
            return render(request, 'login.html',{'form':form}) 
    form = LoginForm()
    return render(request, 'login.html',{'form':form})
