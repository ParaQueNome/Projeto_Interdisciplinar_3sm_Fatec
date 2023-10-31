from django.test import TestCase

from django.test import RequestFactory

from .forms import EmpresaForm
from django import forms
import re
from .views import cadastro

# Create your tests here.

class cadastroTest(TestCase):
    def test_cadastro(self):
        
        request = RequestFactory().get('/cadastro')
        response = cadastro(request)
        self.assertEqual(response.status_code, 200)
    

    

from .forms import EmpresaForm

class EmpresaFormTest(TestCase):
    def test_nome_validation(self):
        form_data = {'nome': 'João'}  # Nome com menos de 5 caracteres
        form = EmpresaForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('Nome muito curto', form.errors['nome'])

    def test_cnpj_validation(self):
        form_data = {'cnpj': '123'}  # CNPJ com menos de 14 caracteres
        form = EmpresaForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('CNPJ invalido', form.errors['cnpj'])
    
    def test_email_validation(self):
        form_data = {'email': 'joao'}  # Email invalido
        form = EmpresaForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('Email invalido', form.errors['email'])

    def test_cep_validation(self):
        form_data = {'cep': '123'}  # CEP com menos de 8 caracteres
        form = EmpresaForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('CEP invalido', form.errors['cep'])

    def test_numero_validation(self):
        form_data = {'numero': 0}  # Número menor que 1
        form = EmpresaForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('Numero invalido', form.errors['numero'])

    def test_senha_validation(self):
        form_data = {'senha': 'senha'}  # Senha fraca (menos de 8 caracteres)
        form = EmpresaForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('A senha deve conter pelo menos 8 caracteres, incluindo pelo menos uma letra maiúscula, uma letra minúscula, um número e um caractere especial.', form.errors['senha'])