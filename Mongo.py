from bson import ObjectId
from pymongo import MongoClient
import pymongo
from pymongo.server_api import ServerApi

class Mongo:
    def __init__(self, conexion=None, db=None, myclient=None):
        if conexion is None:
            self.conexion = "mongodb+srv://VictoriaReyes:1234567$@cluster0.ti3duhj.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
            self.myclient = pymongo.MongoClient( "mongodb+srv://VictoriaReyes:1234567$@cluster0.ti3duhj.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
        else:
            self.conexion = conexion
            self.myclient = myclient
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
    
    def find_Oneever(self, myclient,db,collection, query):
            mydb = myclient[ db]
            mycol = mydb[collection]

            x = mycol.find_one(query)

            object_id = x['_id']
            return x

    def find_One(self, myclient,db,collection, query):
            mydb = myclient[ db]
            mycol = mydb[collection]

            x = mycol.find_one(query)

            object_id = x['_id']
            return object_id
    
    def update_one(self,myclient,db,collection,object,colum,campo):
        mydb = myclient[ db]
        mycol = mydb[collection]
        filtro = {"_id": object}
        actualizacion = {"$set": {colum: campo}}



        x= mycol.update_many(filtro, actualizacion)
        return "***************Documento actualizado",x
    
    def delete_One(self,myclient,db,collection,colum, campo):
        mydb = myclient[ db]
        mycol = mydb[collection]
        myquery = { colum:campo }
        mycol.delete_one(myquery)
    
    def delete_many(self,myclient,db,collection):
        mydb = myclient[ db]
        mycol = mydb[collection]
        x = mycol.delete_many({})

        print(x.deleted_count,"Documentos Borrados")

  

if __name__ == '__main__':
    mongo = Mongo(db="basededates")

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
    
    # myclient = pymongo.MongoClient( "mongodb+srv://VictoriaReyes:1234567$@cluster0.ti3duhj.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

    # query = {"nf": 4 }
    # print (mongo.find_One(myclient,"basededates","Funciones", query))
    
    # colum = ("hora_inicio")
    # campo = ("19:00")
    # print (mongo.update_one(myclient,"basededates","Funciones",mongo.find_One(myclient,"basededates","Funciones", query), colum, campo))

    # query = {"nf": 4 }
    # print (mongo.find_Oneever(myclient,"basededates","Funciones", query))

    pass
    