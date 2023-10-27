import pymongo


class ConexaoService:

    def getConnection(self):
        return pymongo.MongoClient("mongodb://localhost:27017/FoodShare")
