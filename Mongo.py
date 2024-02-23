from pymongo import MongoClient
import pymongo
from pymongo.server_api import ServerApi

class Mongo:
    def __init__(self, conexion=None, db=None):
        if conexion is None:
            self.conexion = "mongodb+srv://VictoriaReyes:1234567$@cluster0.ti3duhj.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
        else:
            self.conexion = conexion
        self.db = db
        self.client = None

        self.startconexion()

    def startconexion(self):
        try:
            self.client = MongoClient(self.conexion)
            info = self.client.server_info()
            print("Conexión exitosa. Información del servidor:", info)
        except Exception as e:
            print("Error al conectar a MongoDB:", e)

    def check_connection(self):
        try:
            self.client.admin.command('ping')
            return True
        except Exception as e:
            print("Error al verificar conexión a MongoDB:", e)
            return False

    def insert_one(self, collection, document):
        try:
            db = self.client[self.db]
            collectionn = db[collection]
            resultado = collectionn.insert_one(document)
            print("Documento insertado, ID:", resultado.inserted_id)
        except Exception as e:
            print("Error al insertar el documento:", e)
    
   
    def find(self, collection, query={}):
        try:
            db = self.client[self.db]
            collectionn = db[collection]
            results = collectionn.find(query)
            return list(results)
        except Exception as e:
            print("Error al buscar en la colección:", e)


if __name__ == '__main__':
    mongo = Mongo(db="Iot_db")
    nueva_funcion = {
        "nf": 4,
        "hora_inicio": "13:00",
        "duracion": ":00 horas",
        "tipo_proyeccion": "imax",
        "precio_entrada": 12.0,
        "pelicula": "El señor de los anillos",
    }
 
    mongo.insert_one("Funciones", nueva_funcion)
    resultados = mongo.find("Funciones")
    print("Funciones encontradas:", resultados)
