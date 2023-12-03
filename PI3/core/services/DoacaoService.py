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
        atualizacao ={'produtos': data}
        
        self.empresaRepository.update(collection,condicao = condicao,**atualizacao)
        
    def findOne(self, data):
        return self.empresaRepository.findOne('Doacoes', **data)
    
    def __del__(self):
        self.empresaRepository.closeConnection()
    