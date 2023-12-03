from .ConexaoService import ConexaoService


class MongoConnectionService:
    def __init__(self,connection : ConexaoService, db_name : str):
        self.client = connection.getConnection()
        self.db = self.client[db_name]
        
    
    def insert(self, collection_name, **kwargs) -> None:
        data = {}
        collection = self.db[collection_name]
        for key, value in kwargs.items():
            data[key] = value
        
        collection.insert_one(data)
    
    def update(self, collection_name,condicao, **kwargs) -> None:
        collection = self.db[collection_name]
        collection.update_one(condicao, {'$push': kwargs}, upsert=True)
        
    def findOne(self, collection_name, **kwargs):
        collection = self.db[collection_name]
        return collection.find_one(kwargs)
    
    def findAll(self, colletion_name, **kwargs):

        collection = self.db[colletion_name]
        return collection.find(kwargs)
    
    def closeConnection(self):
        return self.client.close()