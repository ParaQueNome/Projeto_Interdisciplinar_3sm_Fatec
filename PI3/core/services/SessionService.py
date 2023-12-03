import logging
from .Repositories.FoodShareRepository import FoodShareRepository
from django.shortcuts import redirect, render
from django.contrib.auth import login
from bson import ObjectId



class SessionService():

    def __init__(self, empresaRepository : FoodShareRepository) -> None:
        self.empresaRepository = empresaRepository

    def authenticate(self, collection, data):
        data_c = self.verifyData(collection,data)
        user = self.empresaRepository.findOne(collection, **data_c)
        if user:
            return False
        else:
            return True
    def verifyUser(self, data):
        collection = 'Pessoas' if len(data['login']) == 14 else 'Empresas'
        return collection
    def verifyData(self,collection,data):
        data_c = {}
        if collection == 'Pessoas':
            data_c['cpf'] = data['login']
            data['senha'] = data['senha']
        else:
            data_c['cnpj'] = data['login']
            data_c['senha'] = data['senha']
        return data_c
    def sessionInit(self, request,collection, data):
        data_c = self.verifyData(collection,data)
        
        user = self.empresaRepository.findOne(collection, **data_c)

        if user:
            id = str(user['_id'])
            request.session['user_id'] = id
            request.session['username'] = user['nome']
            
        else:
            return False
    def sessionDestroy(request):
    # Limpa as chaves da sessão
        request.session.pop('user_id', None)
        request.session.pop('username', None)

        return redirect('login')  # Redirecionar para a página inicial ou qualquer outra página desejada
