from django import forms

class EmpresaForm(forms.Form):
    nome = forms.CharField(max_length=50, required= True)
    email = forms.CharField(max_length=50, required= True)
    cnpj = forms.CharField(max_length=18, widget=forms.TextInput(attrs={'placeholder': '99.999.999/9999-99'}))
    ##cep = forms.IntegerField(required= True)
    ##numero = forms.IntegerField(required= True)
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