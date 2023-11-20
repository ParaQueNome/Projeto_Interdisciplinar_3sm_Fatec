from .Repositories.FoodShareRepository import FoodShareRepository



class AuthenticateService():

    def __init__(self, empresaRepository : FoodShareRepository) -> None:
        self.empresaRepository = empresaRepository

    def authenticate(self, email, senha):
        return self.empresaRepository.authenticate(email, senha)