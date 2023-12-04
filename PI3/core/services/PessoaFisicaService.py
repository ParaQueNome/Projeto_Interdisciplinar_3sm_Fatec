from .Repositories.FoodShareRepository import FoodShareRepository

class PessoaFisicaService():

    def __init__(self, empresaRepository : FoodShareRepository) -> None:
        self.empresaRepository = empresaRepository

    def insert(self, data):
        data = {key: value for key, value in data.items() if value}
        self.empresaRepository.insert('Pessoas',**data)
    
    def delete(self, data):
        self.empresaRepository.delete('Pessoas', **data)
    
    def findOne(self, data):
        return self.empresaRepository.findOne('Pessoas', **data)
    
    def __del__(self):
        self.empresaRepository.closeConnection()