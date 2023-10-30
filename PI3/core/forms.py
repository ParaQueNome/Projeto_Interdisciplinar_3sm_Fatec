import re
from django import forms

class EmpresaForm(forms.Form):
    nome = forms.CharField(max_length=50, required= True)
    email = forms.CharField(max_length=50, required= True)
    cnpj = forms.CharField(max_length=18, widget=forms.TextInput(attrs={'placeholder': '99.999.999/9999-99'}))
    cep = forms.CharField(max_length=9, widget=forms.TextInput(attrs={'placeholder': '99.999-999', 'id': 'cep'}))
    numero = forms.IntegerField(required= True)
    senha = forms.CharField(max_length=50, required= True, widget= forms.TextInput(attrs={'type' : 'password'}))
    ramo = forms.CharField(max_length=50, required= False)
    descricao = forms.CharField(max_length=50, required= False)
    telefone = forms.IntegerField(required= False)
    site = forms.CharField(max_length=50, required= False)



    def clean_nome(self):
        nome = self.cleaned_data['nome']
        if len(nome) < 5:
            raise forms.ValidationError('Nome muito curto')
        return nome
    
    def clean_email(self):
        email = self.cleaned_data['email']
        if len(email) < 5 and email.find('@') == -1:
            raise forms.ValidationError('Email invalido')
            
        return email
    def clean_cnpj(self):
        cnpj = self.cleaned_data['cnpj']
        if len(cnpj) < 14 and cnpj.find('-') == -1 and cnpj.find('/') == -1:
            
            raise forms.ValidationError('CNPJ invalido')
            
        return cnpj
    def cleanCep(self):
        cep = self.cleaned_data['cep']
        if len(cep) < 8:
            raise forms.ValidationError('CEP invalido')
            
        return cep
    
    def cleanNumero(self):
        numero = self.cleaned_data['numero']
        if numero < 1:
            raise forms.ValidationError('Numero invalido')
            
        return numero
    def cleanSenha(self):
        senha = self.cleaned_data['senha']
        if len(senha) < 8:
            
            if senha:
            # Verifique se a senha contém pelo menos uma letra maiúscula
                if not re.search(r'[A-Z]', senha):
                    raise forms.ValidationError('A senha deve conter pelo menos uma letra maiúscula.')

            # Verifique se a senha contém pelo menos uma letra minúscula
                if not re.search(r'[a-z]', senha):
                    raise forms.ValidationError('A senha deve conter pelo menos uma letra minúscula.')

                 # Verifique se a senha contém pelo menos um número
                if not re.search(r'\d', senha):
                    raise forms.ValidationError('A senha deve conter pelo menos um número.')

                # Verifique se a senha contém pelo menos um caractere especial
                if not re.search(r'[!@#$%^&*()_+{}":;\'<>,.\\-]', senha):
                    raise forms.ValidationError('A senha deve conter pelo menos um caractere especial.')
        return senha