from .Repositories.FoodShareRepository import FoodShareRepository


class DoacaoService():
    def __init__(self, empresaRepository : FoodShareRepository) -> None:
        self.empresaRepository = empresaRepository

    def insert(self, data):
        data = {key: value for key, value in data.items() if value}
        self.empresaRepository.insert('Doacoes',**data)
    
    def findOne(self, data):
        return self.empresaRepository.findOne('Doacoes', **data)
    
    def findAll(self, data):
        return self.empresaRepository.findAll('Doacoes', **data)
    
    def __del__(self):
        self.empresaRepository.closeConnection()
    