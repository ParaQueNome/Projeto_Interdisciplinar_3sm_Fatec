from .Repositories.FoodShareRepository import FoodShareRepository



class EmpresaService():

    def __init__(self, empresaRepository : FoodShareRepository) -> None:
        self.empresaRepository = empresaRepository

    def insert(self, data):
        data = {key: value for key, value in data.items() if value}
        self.empresaRepository.insert('Empresas',**data)
    
    def findOne(self, data):
        return self.empresaRepository.findOne('Empresas', **data)
    
    def __del__(self):
        self.empresaRepository.closeConnection()
