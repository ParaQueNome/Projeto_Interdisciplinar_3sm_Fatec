import datetime
import re
from django import forms
from .services.EmpresaService import EmpresaService
from .services.ConexaoService import ConexaoService
from .services.Repositories.FoodShareRepository import FoodShareRepository
from .services.MongoConnectionService import MongoConnectionService

class EmpresaForm(forms.Form):
    nome = forms.CharField(max_length=50, required=True)
    email = forms.CharField(max_length=20, required=True)
    cnpj = forms.CharField(max_length=18, widget=forms.TextInput(attrs={'placeholder': '99.999.999/9999-99'}))
    cep = forms.CharField(max_length=9, widget=forms.TextInput(attrs={'placeholder': '99.999-999', 'id': 'cep'}))
    numero = forms.IntegerField(required=True)
    senha = forms.CharField(max_length=25, required=True, widget=forms.TextInput(attrs={'type': 'password'}))
    ramo = forms.CharField(max_length=25, required=False)
    descricao = forms.CharField(max_length=50, required=False)
    telefone = forms.CharField(max_length=15, required=True, widget=forms.TextInput(attrs={'placeholder': '(99)99999-9999', 'id': 'id_telefone'}))
    site = forms.CharField(max_length=50, required=False)

    def valida_cnpj(self):
        connection = ConexaoService()
        bd = MongoConnectionService(connection, 'FoodShare')
        empresa = EmpresaService(FoodShareRepository(bd))
        cnpj = self.cleaned_data['cnpj']
        documento = empresa.findOne({'cnpj': cnpj})
        if documento:
            raise forms.ValidationError('CNPJ já cadastrado')
        return cnpj

    def clean_nome(self):
        nome = self.cleaned_data['nome']
        if len(nome) < 5:
            raise forms.ValidationError('Nome muito curto')
        return nome
    
    def clean_email(self):
        email = self.cleaned_data['email']
        if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
            raise forms.ValidationError('Email inválido')
        return email
            
    def clean_cnpj(self):
        cnpj = self.valida_cnpj()
        if len(cnpj) < 14 and ('-' not in cnpj and '/' not in cnpj):
            raise forms.ValidationError('CNPJ inválido')
        return cnpj

    def clean_cep(self):
        cep = self.cleaned_data['cep']
        if len(cep) < 8:
            raise forms.ValidationError('CEP inválido')
        return cep

    def clean_numero(self):
        numero = self.cleaned_data['numero']
        if numero < 1:
            raise forms.ValidationError('Número inválido')
        return numero

    def clean_senha(self):
        senha = self.cleaned_data['senha']
        if len(senha) < 8 or not (any(char.isupper() for char in senha) and
                                  any(char.islower() for char in senha) and
                                  any(char.isdigit() for char in senha) and
                                  any(char in "!@#$%^&*()_+{}\":;'<>.,\\-" for char in senha)):
            raise forms.ValidationError('A senha deve conter pelo menos 8 caracteres, incluindo pelo menos uma letra maiúscula, uma letra minúscula, um número e um caractere especial.')
        return senha

    def clean_telefone(self):
        telefone = self.cleaned_data['telefone']
        if len(telefone) < 11:
            raise forms.ValidationError('Telefone inválido')
        return telefone
   
    
class PessoaForm(forms.Form):
    nome = forms.CharField(max_length=25, required=True)
    cpf = forms.CharField(max_length=14, required=True, widget=forms.TextInput(attrs={'placeholder': '999.999.999-99','id': 'cpf'}))
    email = forms.CharField(max_length=50, required=True)
    telefone = forms.CharField(max_length=15, required=True, widget=forms.TextInput(attrs={'placeholder': '(99)99999-9999', 'id': 'id_telefone'}))
    senha = forms.CharField(max_length=25, required=True, widget=forms.TextInput(attrs={'type': 'password'}))
    cep = forms.CharField(max_length=9, widget=forms.TextInput(attrs={'placeholder': '99.999-999', 'id': 'cep'}))
    data_nascimento  = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'dd/mm/yyyy', 'id': 'data_nascimento'}))
    numero = forms.IntegerField(required=True)
    social = forms.CharField(max_length=20, required=False)

    def clean_senha(self):
        senha = self.cleaned_data['senha']
        if len(senha) < 8 or not (any(char.isupper() for char in senha) and
                                  any(char.islower() for char in senha) and
                                  any(char.isdigit() for char in senha) and
                                  any(char in "!@#$%^&*()_+{}\":;'<>.,\\-" for char in senha)):
            raise forms.ValidationError('A senha deve conter pelo menos 8 caracteres, incluindo pelo menos uma letra maiúscula, uma letra minúscula, um número e um caractere especial.')
        return senha

    def clean_nome(self):
        nome = self.cleaned_data['nome']
        if len(nome) < 5:
            raise forms.ValidationError('Nome muito curto')
        return nome

    def clean_telefone(self):
        telefone = self.cleaned_data['telefone']
        if len(telefone) < 11:
            raise forms.ValidationError('Telefone inválido')
        return telefone

    def clean_cpf(self):
        cpf = self.cleaned_data['cpf']
        if len(cpf) < 14:
            raise forms.ValidationError('CPF inválido')
        return cpf

    def clean_email(self):
        email = self.cleaned_data['email']
        if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
            raise forms.ValidationError('Email inválido')
        return email

    def clean_cep(self):
        cep = self.cleaned_data['cep']
        if len(cep) < 8:
            raise forms.ValidationError('CEP inválido')
        return cep

    def clean_numero(self):
        numero = self.cleaned_data['numero']
        if numero < 1:
            raise forms.ValidationError('Número inválido')
        return numero

    def validar_data(data):
        pattern = r'^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/\d{4}$'
        if not re.match(pattern, data):
            raise forms.ValidationError('Data inválida')

        dia, mes, ano = map(int, data.split('/'))

        if (mes in [4, 6, 9, 11] and dia > 30) or (mes == 2 and ((ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0) and dia > 29) or (mes == 2 and dia > 28):
            raise forms.ValidationError('Data inválida')

        return data
        
class DoacaoForm(forms.Form):
    nome = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'placeholder': 'nome'}))
    telefone = forms.CharField(max_length=14, required=True, widget=forms.TextInput(attrs={'name': 'telefone','placeholder': '(99)99999-9999', 'id': 'id_telefone'}))
    email = forms.CharField(max_length=50, required=True) 
    endereco = forms.CharField(max_length=100)
    numero = forms.IntegerField(required=True)
    cidade = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Cidade'}))
    estado = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Estado'}))
    cep = forms.CharField(max_length=9, widget=forms.TextInput(attrs={'placeholder': '99.999-999', 'id': 'cep'}))
    valor = forms.IntegerField(required=True)

    def clean_cep(self):
        cep = self.cleaned_data['cep']
        if len(cep) < 8:
            raise forms.ValidationError('CEP inválido')
        return cep

    def clean_nome(self):
        nome = self.cleaned_data['nome']
        if len(nome) < 5:
            raise forms.ValidationError('Nome muito curto')
        return nome

    def clean_telefone(self):
        telefone = self.cleaned_data['telefone']
        if len(telefone) < 11:
            raise forms.ValidationError('Telefone inválido')
        return telefone

    def clean_email(self):
        email = self.cleaned_data['email']
        if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
            raise forms.ValidationError('Email inválido')
        return email

    def clean_numero(self):
        numero = self.cleaned_data['numero']
        if numero < 1:
            raise forms.ValidationError('Número inválido')
        return numero

    def clean_valor(self):
        valor = self.cleaned_data['valor']
        if valor < 1:
            raise forms.ValidationError('Valor inválido')
        return valor
class DoacaoAlimentoForm(forms.Form):
    TIPOS_ALIMENTOS = [
        ('Selecione','Selecione'),
        ('Bebidas','Bebidas'),
        ('Pereciveis','Pereciveis'),
        ('Laticinios','Laticinios'),
        ('Carnes','Carnes'),
        ('Frutas','Frutas'),
        ('Legumes','Legumes'),
        ('Ovos','Ovos'),
        ('Agua Mineral','Agua Mineral')
    ]
    tipoAlimento = forms.ChoiceField(choices= TIPOS_ALIMENTOS,required=True)
    data_validade = forms.DateField(required=True, widget= forms.TextInput(attrs={'placeholder': 'dd/mm/yyyy', 'id': 'data_validade'}))
    valor_base = forms.IntegerField(required=True)
    ean = forms.CharField(required=True, max_length=13)
    nome = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'placeholder': 'nome'}))
    marca = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'placeholder': 'marca'}))

    def clean_tipoAlimento(self):
        tipoAlimento = self.cleaned_data['tipoAlimento']
        if tipoAlimento == 'Selecione':
            raise forms.ValidationError('Selecione um tipo de alimento')
        return tipoAlimento
    def clean_data_validade(self):
        data_validade = self.cleaned_data['data_validade']
        if data_validade < datetime.date.today() or data_validade < datetime.date.today() + datetime.timedelta(days=30):
            
            raise forms.ValidationError('Data de vencimento deve ser maior que 30 dias/Alimento vencido')
        data_validade_str = data_validade.strftime('%d/%m/%Y')  
        return data_validade_str
    def clean_valor_base(self):
        valor_base = self.cleaned_data['valor_base']
        if valor_base < 1:
            raise forms.ValidationError('Valor inválido')
        return valor_base
    def clean_nome(self):
        nome = self.cleaned_data['nome']
        if len(nome) < 5:
            raise forms.ValidationError('Nome muito curto')
        return nome 
    def clean_marca(self):
        marca = self.cleaned_data['marca']
        if len(marca) < 5:
            raise forms.ValidationError('Marca muito curta')
        return marca
    def clean_ean(self):
        ean = self.cleaned_data['ean']
        if len(ean) < 13:
            raise forms.ValidationError('EAN inválido')
        return ean
        
        
class LoginForm(forms.Form):
    login = forms.CharField(max_length=18, required=True, widget=forms.TextInput(attrs={'placeholder': 'CPF ou CNPJ','id': 'login'}))
    senha = forms.CharField(max_length=25, required=True, widget=forms.TextInput(attrs={'type': 'password'}))

    def clean_login(self):
        login = self.cleaned_data['login']
        return login if len(login) in (14, 18) else forms.ValidationError("O login deve ter 14 ou 18 caracteres.", code='invalid_length')
    
    def clean_senha(self):
        senha = self.cleaned_data['senha']
        if len(senha) < 8 or not (any(char.isupper() for char in senha) and
                            any(char.islower() for char in senha) and
                            any(char.isdigit() for char in senha) and
                            any(char in "!@#$%^&*()_+{}\":;'<>.,\\-" for char in senha)):
            raise forms.ValidationError('Senha inválida!')
        return senha
