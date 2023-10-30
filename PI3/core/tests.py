from django.test import TestCase

from django.test import RequestFactory

from .forms import EmpresaForm
from django import forms
from .views import cadastro

# Create your tests here.

class cadastroTest(TestCase):
    def test_cadastro(self):
        
        request = RequestFactory().get('/cadastro')
        response = cadastro(request)
        self.assertEqual(response.status_code, 200)
    
    def test_form(self):

        form = EmpresaForm()
        self.assertTrue(form.is_valid())
        self.assertEqual(form.errors, {})

    def test_nome(self):


        form = EmpresaForm({'nome': 'teste'})
        
        
        
        self.assertEqual(form.cleaned_data['nome'],'teste')

