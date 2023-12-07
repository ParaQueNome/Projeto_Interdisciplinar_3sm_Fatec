
from datetime import datetime
from .Repositories.FoodShareRepository import FoodShareRepository   
from bson import ObjectId

class AdminService():

    def __init__(self,repository : FoodShareRepository):
        self.repository = repository
        self.repository.insert('Admin',{'login':'admin', 'senha':'admin'}) if not self.repository.findAll('Admin',**{'login':'admin'}) else None

    def findAll(self):
        result = self.repository.findAll('Empresas', **{})
        produto = None
        if result:
            for prod in result:
                if prod and 'produtos' in prod:
                    produto = prod['produtos']
                    break
        result = self.repository.findAll('Pessoas', **{})
        if result:
            for prod in result:
                if prod and 'produtos' in prod:
                    produto = prod['produtos']
                    break
        return produto
            
    def insert(self,data):
        data['data_registro'] = datetime.now()
        return self.repository.insert('Doacoes',**data)
        