from django import forms

class EmpresaForm(forms.Form):
    nome = forms.CharField(max_length=50)



    def clean_nome(self):
        nome = self.cleaned_data['nome']
        if len(nome) < 5:
            raise forms.ValidationError('Nome muito curto')
        return nome