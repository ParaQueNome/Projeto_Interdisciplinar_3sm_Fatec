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
    
    def updateOne(self, collection_name,condicao, **kwargs):
        self.conexao.updateOne(collection_name,condicao, **kwargs)
    
    def update(self, collection_name,condicao, **kwargs):
        self.conexao.update(collection_name,condicao, **kwargs)
    def delete(self, collection_name,condicao, **kwargs):
        self.conexao.delete(collection_name,condicao, **kwargs)
    
    def execute_aggregation(self, collection_name, pipeline):
        return self.conexao.execute_aggregation(collection_name, pipeline)
    
    def closeConnection(self):
        self.conexao.closeConnection()