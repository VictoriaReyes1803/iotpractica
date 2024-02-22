from pymongo import MongoClient

class Mongo:
    def __init__(self, conexion=None, db=None):
        if conexion is None:
            self.conexion = "mongodb+srv://myAtlasDBUser:280304Da@myatlasclusteredu.ino9cmx.mongodb.net/"
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
        "numero_funcion": 2,
        "hora_inicio": "13:00",
        "duracion": ":00 horas",
        "tipo_proyeccion": "imax",
        "precio_entrada": 12.0,
        "pelicula": "jj"
    }
    mongo.insert_one("Funciones", nueva_funcion)
    resultados = mongo.find("Funciones")
    print("Funciones encontradas:", resultados)
