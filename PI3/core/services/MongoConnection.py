from .ConexaoService import ConexaoService


class MongoConnection:
    def __init__(self,connection) -> None:
        self.client = connection.getConnection()
        self.db = self.client['FoodShare']
        
    
    def insert(self, nome):

        collection = self.db['core_empresas']
        data = {'nome': nome}
        collection.insert_one(data)