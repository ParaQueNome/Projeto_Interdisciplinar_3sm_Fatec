from ..MongoConnectionService import MongoConnectionService

class FoodShareRepository():

    def __init__(self, conexao : MongoConnectionService) -> None:
        self.conexao = conexao
    
    def insert(self, collection_name, **kwargs):
        self.conexao.insert(collection_name, **kwargs)

    def findOne(self, collection_name,**kwargs):
        return self.conexao.findOne(collection_name,**kwargs)
    
    def findAll(self, collection_name, **kwargs):
        return self.conexao.findAll(collection_name,**kwargs)
        
    
    def closeConnection(self):
        self.conexao.closeConnection()