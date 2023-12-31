import unittest
from django.test import TestCase

from django.test import RequestFactory

from .forms import DoacaoAlimentoForm, EmpresaForm, PessoaForm
from django import forms
import re
from .views import cadastro
from .services.MongoConnectionService import MongoConnectionService
from .services.ConexaoService import ConexaoService
from .services.Repositories.FoodShareRepository import FoodShareRepository
from .services.EmpresaService import EmpresaService

        
class cadastroTest(TestCase):
    def test_cadastro(self):
        
        request = RequestFactory().get('/cadastro')
        response = cadastro(request)
        self.assertEqual(response.status_code, 200)

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
        self.assertIn('CNPJ inválido', form.errors['cnpj'])
    
    def test_email_validation(self):
        form_data = {'email': 'joao'}  # Email invalido
        form = EmpresaForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('Email inválido', form.errors['email'])

    def test_cep_validation(self):
        form_data = {'cep': '123'}  # CEP com menos de 8 caracteres
        form = EmpresaForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('CEP inválido', form.errors['cep'])

    def test_numero_validation(self):
        form_data = {'numero': 0}  # Número menor que 1
        form = EmpresaForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('Número inválido', form.errors['numero'])

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
        self.assertIn('Telefone inválido', form.errors['telefone'])

    def test_email_validation(self):
        form_data = {'email': 'joao'}  # Email invalido
        form = PessoaForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('Email inválido', form.errors['email'])

    def test_senha_validation(self):
        form_data = {'senha': 'senha'}  # Senha fraca (menos de 8 caracteres)
        form = PessoaForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('A senha deve conter pelo menos 8 caracteres, incluindo pelo menos uma letra maiúscula, uma letra minúscula, um número e um caractere especial.', form.errors['senha'])
    
    def test_cpf_validation(self):
        form_data = {'cpf': '123'}  # CPF com menos de 11 caracteres
        form = PessoaForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('CPF inválido', form.errors['cpf'])
    
    def test_cep_validation(self):
        form_data = {'cep': '123'}  # CEP com menos de 8 caracteres
        form = PessoaForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('CEP inválido', form.errors['cep'])

class DoacaoAlimentoFormTest(TestCase):
    def test_quantidade_validation(self):
        form_data = {'nome': 'nome'}  # Quantidade menor que 1
        form = DoacaoAlimentoForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('Nome muito curto', form.errors['nome'])
    
    def test_data_validation(self):

        form_data = {'data': '01-01-2023'}  # Data inválida
        form = DoacaoAlimentoForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('This field is required.', form.errors['data_validade'])

    def test_ean(self):
        form_data = {'ean': '123'}  # EAN inválido
        form = DoacaoAlimentoForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('EAN inválido', form.errors['ean'])

    def test_valor_base(self):
        form_data = {'valor_base': '0'}  # Valor base inválido
        form = DoacaoAlimentoForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('Valor inválido', form.errors['valor_base'])



class TestMongoDb(TestCase):
    def setUp(self):
        self.conexao_service = ConexaoService()
        self.mongo_connection = MongoConnectionService(self.conexao_service, 'testdb')
        self.repository = FoodShareRepository(self.mongo_connection)
    
    def test_insert(self):
        self.conexao_service = ConexaoService()
        self.mongo_connection = MongoConnectionService(self.conexao_service, 'testdb')
        self.repository = FoodShareRepository(self.mongo_connection)
        data = {'nome': 'teste'}
        result = self.repository.insert('testes',**data)
        self.assertIsNone(result)
    def test_findOne(self):
        self.conexao_service = ConexaoService()
        self.mongo_connection = MongoConnectionService(self.conexao_service, 'testdb')
        self.repository = FoodShareRepository(self.mongo_connection)
        data = {'nome': 'teste'}
        result = self.repository.findOne('testes',**data)
        print('resultado', result)
        self.assertIsNotNone(result)
    ##def tearDown(self):
        ##self.mongo_connection.client.drop_database('testdb')
