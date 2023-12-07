
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
        produto1 = None
        if result:
            for prod in result:
                if prod and 'produtos' in prod:
                    produto1 = prod['produtos']
                    break
        if produto is not None and produto1 is not None:
            total = produto + produto1
        elif produto is not None:
            total = produto
        else:
            total = produto1
        return total
        
    def insert(self,data):
        data['data_registro'] = datetime.now()
        return self.repository.insert('Doacoes',**data)
    
    def login(self,login,senha):
        result = self.repository.findAll('Admin',**{'login':login,'senha':senha})
        return result
        
    def sessionInit(self,request,data):
        user = self.repository.findOne('Admin', **data)
        if user:
            id = str(user['_id'])
            request.session['user_id'] = id
            request.session['username'] = user['login']
            
        else:
            return False
        
    def agregacao_data(self, data_inicial, data_final):
        pipeline = [
            {
                "$match": {
                    "data_registro": {
                        "$gte": data_inicial,
                        "$lt": data_final
                    }
                }
            }
        ]

        resultado_agregacao = self.repository.execute_aggregation('Doacoes', pipeline)
        return resultado_agregacao