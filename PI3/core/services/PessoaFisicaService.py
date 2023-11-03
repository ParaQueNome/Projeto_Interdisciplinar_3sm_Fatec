from .Repositories.FoodShareRepository import FoodShareRepository

class PessoaFisicaService():

    def __init__(self, pessoaRepository : FoodShareRepository) -> None:
        self.pessoaRepository = pessoaRepository