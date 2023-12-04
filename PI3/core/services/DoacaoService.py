from .Repositories.FoodShareRepository import FoodShareRepository
from bson import ObjectId

class DoacaoService():
    def __init__(self, empresaRepository : FoodShareRepository) -> None:
        self.empresaRepository = empresaRepository
    def verifyUser(self, data):
        if self.empresaRepository.findOne('Empresas', **data):
            return 'Empresas'
        else:
            return 'Pessoas'
    
    def insert(self,data, userId):
        userId = ObjectId(userId)
        userIdDict = {'_id': userId}
        collection = self.verifyUser(userIdDict)
        condicao = {'_id': userId}
        data['_id'] = ObjectId()
        data['status'] = 'Pendente'
        atualizacao ={'produtos': data}
        
        self.empresaRepository.update(collection,condicao = condicao,**atualizacao)
    
    def delete(self, data, userId):
        userId = ObjectId(userId)
        userIdDict = {'_id': userId}
        collection = self.verifyUser(userIdDict)
        condicao = {'_id': userId}
        atualizacao = {'produtos': data}
        
        self.empresaRepository.update(collection,condicao = condicao,**atualizacao)
    
    def findAll(self,userId):
        
        userIdDict = {'_id': ObjectId(userId)}
        collection = self.verifyUser(userIdDict)
        return self.empresaRepository.findAll(collection, **userIdDict)
    
    def __del__(self):
        self.empresaRepository.closeConnection()
    