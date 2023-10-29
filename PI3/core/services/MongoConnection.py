from .ConexaoService import ConexaoService


class MongoConnection:
    def __init__(self,connection) -> None:
        self.client = connection.getConnection()
        self.db = self.client['FoodShare']
        
    
    def insert(self, **kwargs):
        data = {}
        collection = self.db['Empresas']
        for key, value in kwargs.items():
            data[key] = value
        
        collection.insert_one(data)