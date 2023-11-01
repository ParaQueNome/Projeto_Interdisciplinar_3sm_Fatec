import unittest
from django.test import TestCase

from django.test import RequestFactory

from .forms import EmpresaForm, PessoaForm
from django import forms
import re
from .views import cadastro
from .services.MongoConnection import MongoConnection
from .services.ConexaoService import ConexaoService

# Create your tests here.
class TestMongoDb(unittest.TestCase):
    def setUp(self):
        self.mongo_connection = MongoConnection()
        self.conexao_service = ConexaoService()
        
class cadastroTest(TestCase):
    def test_cadastro(self):
        
        request = RequestFactory().get('/cadastro')
        response = cadastro(request)
        self.assertEqual(response.status_code, 200)

    def test_cadastro_post(self):
        form_data = {'nome': 'João', 'cnpj': '12345678901234', 'email': 'jonas@gmail.com', 'cep': '123456780', 'numero': '1', 'senha': 'Senha123@'}
        form = EmpresaForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data['nome'], 'João')
        self.assertEqual(form.cleaned_data['cnpj'], '12345678901234')
        self.assertEqual(form.cleaned_data['email'], 'XXXXXXXXXXXXXX')
        self.assertEqual(form.cleaned_data['cep'], '12345678')
        self.assertEqual(form.cleaned_data['numero'], '1')
        self.assertEqual(form.cleaned_data['senha'], 'senha123')
    

    



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

    
class PessoaFormTest(TestCase):
    def test_nome_validation(self):
        form_data = {'nome': 'João'}  # Nome com menos de 5 caracteres
        form = PessoaForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('Nome muito curto', form.errors['nome'])

    def test_telefone_validation(self):
        form_data = {'telefone': '123'}  # Telefone com menos de 15 caracteres
        form = PessoaForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('Telefone invalido', form.errors['telefone'])

    def test_email_validation(self):
        form_data = {'email': 'joao'}  # Email invalido
        form = PessoaForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('Email invalido', form.errors['email'])

    def test_senha_validation(self):
        form_data = {'senha': 'senha'}  # Senha fraca (menos de 8 caracteres)
        form = PessoaForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('A senha deve conter pelo menos 8 caracteres, incluindo pelo menos uma letra maiúscula, uma letra minúscula, um número e um caractere especial.', form.errors['senha'])
    
    def test_cpf_validation(self):
        form_data = {'cpf': '123'}  # CPF com menos de 11 caracteres
        form = PessoaForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('CPF invalido', form.errors['cpf'])
    
    def test_cep_validation(self):
        form_data = {'cep': '123'}  # CEP com menos de 8 caracteres
        form = PessoaForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('CEP invalido', form.errors['cep'])