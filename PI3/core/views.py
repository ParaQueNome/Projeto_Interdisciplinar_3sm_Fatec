from django.shortcuts import redirect, render
from bson import ObjectId
from django.http import HttpResponse, JsonResponse
from .forms import EmpresaForm, PessoaForm, DoacaoForm, LoginForm, DoacaoAlimentoForm
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

def relatorio(request):
    if 'user_id' not in request.session:
        return redirect('login')
    
    connection = ConexaoService()
    bd = MongoConnectionService(connection,"FoodShare") 
    repository = FoodShareRepository(bd)
    doacao = DoacaoService(repository)
    produtos = doacao.findAll(request.session.get('user_id'))
    contexto = {
    'alimentos': [
        {   
            'id': str(alimento['_id']),
            'tipoAlimento': alimento['tipoAlimento'],
            'nome': alimento['nome'],
            'marca': alimento['marca'],
            'data_validade': alimento['data_validade'],
            'status': alimento['status']
            # Adicione outros campos conforme necessário
        }
        for produto in produtos
        for alimento in produto['produtos']
    ],
    'session': request.session.get('username')
}
    doacao.__del__
    return render(request, 'relatorios.html',contexto)
def remover_alimento(request,alimento_id):
    alimento_id = ObjectId(alimento_id)
    connection = ConexaoService()
    bd = MongoConnectionService(connection,"FoodShare")
    repository = FoodShareRepository(bd)
    doacao = DoacaoService(repository)
    doacao.delete(alimento_id,request.session.get('user_id'))
    doacao.__del__
    return redirect('relatorio')
    
def editarDoacao(request,alimento_id):
    userId = request.session.get('user_id')
    connection = ConexaoService()
    bd = MongoConnectionService(connection,"FoodShare")
    repository = FoodShareRepository(bd)
    doacao = DoacaoService(repository)

    produto = doacao.findOne(alimento_id,userId)
    print(produto)
    
    form = DoacaoAlimentoForm(initial={'tipoAlimento':produto['tipoAlimento'],'nome':produto['nome'],'marca':produto['marca'],'ean':produto['ean'],'data_validade':produto['data_validade'],'valor_base':produto['valor_base']})

    return render(request, 'editarDoacao.html',{'form':form,'session': request.session.get('username'),'alimento_id':alimento_id})

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
            return render(request, 'doacao.html',{'form':form,'session': request.session.get('username')})
    form  = DoacaoForm()
    return render(request, 'doacao.html',{'form':form,'session': request.session.get('username')})


def doar_alimento(request):
    if 'user_id' not in request.session:
        return redirect('login')
    if request.method == 'POST':
        form = DoacaoAlimentoForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            connection = ConexaoService()
            bd = MongoConnectionService(connection,"FoodShare")
            repository = FoodShareRepository(bd)
            doacao = DoacaoService(repository)
            doacao.insert(form.cleaned_data,request.session.get('user_id'))
            return redirect('doacao')
            
        else:
            return render(request, 'doacaoAlimento.html',{'form':form,'session': request.session.get('username')})
    form = DoacaoAlimentoForm()
    return render(request, 'doacaoAlimento.html',{'form':form,'session': request.session.get('username')})


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
            if erro:
                context = {'form':form, 'erro':'Credenciais inválidas'}
                return render(request, 'login.html', context)
            session = login.sessionInit(request,collection,form.cleaned_data)
            if session is None:
                return redirect('doacao') 
        else:
            return render(request, 'login.html',{'form':form}) 
    form = LoginForm()
    return render(request, 'login.html',{'form':form})

def processar_atualizacao(request, alimento_id):
    
    connection = ConexaoService()
    bd = MongoConnectionService(connection, "FoodShare")
    repository = FoodShareRepository(bd)
    doacao = DoacaoService(repository)

    if request.method == 'POST':
        form = DoacaoAlimentoForm(request.POST)
        if form.is_valid():
            dados_atualizados = {
                'tipoAlimento': form.cleaned_data['tipoAlimento'],
                'data_validade': form.cleaned_data['data_validade'],
                'valor_base': form.cleaned_data['valor_base'],
                'ean': form.cleaned_data['ean'],
                'nome': form.cleaned_data['nome'],
                'marca': form.cleaned_data['marca'],
            }

            doacao.update(request.session.get('user_id'),alimento_id, dados_atualizados)
            return redirect('relatorio')

    # Lidar com o caso em que o método da solicitação não é POST
    return redirect('relatorio')
