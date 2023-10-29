from django import forms

class EmpresaForm(forms.Form):
    nome = forms.CharField(max_length=50)
    email = forms.CharField(max_length=50)



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