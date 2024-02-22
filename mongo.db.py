from pymongo import MongoClient
class mongo:
    def _init_(self, conexion = None, db = None):
        self.db = db
        self.conexion = conexion

    def startconexion(self):
        try:
            client = MongoClient(self.conexion)
            info = client.server_info()
            print("Conexión exitosa. Información del servidor:", info)

        except Exception as e:
            print("Error al conectar a MongoDB:", e)

    def myCollections(self):
            client = MongoClient(self.conexion)
            db=client[self.db]
            colecciones = db.list_collection_names()
            print("Conexión exitosa. Colecciones en la base de datos:", colecciones)

    def insert_one(self, collection, document):
            client = MongoClient(self.conexion)
            db=client[self.db]
            collectionn = db[collection]
            resultado = collectionn.insert_one(document)
            print("Documento insertado, ID:", resultado.inserted_ids)


    def Insert_Many(self, collection, documents):
            client = MongoClient(self.conexion)
            db=client[self.db]
            collectionn = db[collection]
            resultado = collectionn.insert_many(documents)
            print("Documento insertado, ID:", resultado.inserted_ids)