import re
from django import forms

class EmpresaForm(forms.Form):
    nome = forms.CharField(max_length=50, required= True)
    email = forms.CharField(max_length=20, required= True)
    cnpj = forms.CharField(max_length=18, widget=forms.TextInput(attrs={'placeholder': '99.999.999/9999-99'}))
    cep = forms.CharField(max_length=9, widget=forms.TextInput(attrs={'placeholder': '99.999-999', 'id': 'cep'}))
    numero = forms.IntegerField(required= True)
    senha = forms.CharField(max_length=25, required= True, widget= forms.TextInput(attrs={'type' : 'password'}))
    ramo = forms.CharField(max_length=25, required= False)
    descricao = forms.CharField(max_length=50, required= False)
    telefone = forms.CharField(max_length = 15, required = True, widget=forms.TextInput(attrs={'placeholder': '(99)99999-9999', 'id': 'telefone'}))
    site = forms.CharField(max_length=50, required= False)



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
        cnpj = self.cleaned_data['cnpj']
        if len(cnpj) < 14  and ('-' not in cnpj and '/' not in cnpj):
            
            raise forms.ValidationError('CNPJ invalido')
            
        return cnpj
    def clean_cep(self):
        cep = self.cleaned_data['cep']
        if len(cep) < 8:
            raise forms.ValidationError('CEP invalido')
            
        return cep
    
    def clean_numero(self):
        numero = self.cleaned_data['numero']
        if numero < 1:
            raise forms.ValidationError('Numero invalido')
            
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
            raise forms.ValidationError('Telefone invalido')
            
        return telefone
   
    
class PessoaForm(forms.Form):
        nome = forms.CharField(max_length=25, required= True)
        cpf = forms.CharField(max_length=13, required=True, widget=forms.TextInput(attrs={'placeholder':'999.999.999-99','id': 'cpf'}))
        email = forms.CharField(max_length=20, required= True)
        telefone = forms.CharField(max_length = 15, required = True, widget=forms.TextInput(attrs={'placeholder': '(99)99999-9999', 'id': 'telefone'}))
        senha = forms.CharField(max_length=25, required= True, widget= forms.TextInput(attrs={'type' : 'password'}))
        cep = forms.CharField(max_length=9, widget=forms.TextInput(attrs={'placeholder': '99.999-999', 'id': 'cep'}))
        data_nascimento  = forms.DateField(required= True)
        numero = forms.IntegerField(required= True)
        social = forms.CharField(max_length=20, required= False)
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
                raise forms.ValidationError('Telefone invalido')
            
            return telefone
        def clean_cpf(self):
            cpf = self.cleaned_data['cpf']
            if len(cpf) < 14:
                raise forms.ValidationError('CPF invalido')
            return cpf
        def clean_email(self):
            email = self.cleaned_data['email']
            if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
                raise forms.ValidationError('Email inválido')
    
            return email
        def clean_cep(self):
            cep = self.cleaned_data['cep']
            if len(cep) < 8:
                raise forms.ValidationError('CEP invalido')
                
            
            return cep
        def clean_numero(self):
            numero = self.cleaned_data['numero']
            if numero < 1:
                raise forms.ValidationError('Numero invalido')
            return numero