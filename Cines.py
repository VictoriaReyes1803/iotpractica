
from Salas import Salas
from Funciones import Funciones
from Mongo import Mongo
from bson import ObjectId
from Arreglo import Arreglo
import pymongo
import json

class Cines(Arreglo):
    def __init__(self, num=None ,nombre=None, ubi=None, capacidad=None, numero_salas=None, clasificacion=None, salas=None, total_ganancias=None):
        super().__init__() 
        self.banderaLista= num==None and nombre==None and ubi==None 
        if self.banderaLista:  
            self.arreglo=[]
        else:
            self.arreglo=None
            self.num=num
            self.nombre = nombre
            self.ubi = ubi
            self.capacidad = capacidad
            self.numero_salas = numero_salas
            self.clasificacion = clasificacion
            self.total_ganancias = total_ganancias
            self.salas = salas
            
            if self.salas is None:
                 self.salas = Salas()
        #self.myclient = pymongo.MongoClient( "mongodb+srv://VictoriaReyes:1234567$@cluster0.ti3duhj.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

            


    def __str__(self):
        if not self.banderaLista:
            return f"Cine {self.num} - Nombre {self.nombre} - Ubicación: {self.ubi}\n" \
                   f"Capacidad: {self.capacidad}\n" \
                   f"Número de salas: {self.numero_salas}\n" \
                   f"Clasificación: {self.clasificacion}\n" \
                    f"Total de ganancias: {self.total_ganancias}\n" 
        else:
            return f"Es un arreglo de ({len(self.arreglo)}) elementos."

        
    def dictt(self):
        if self.banderaLista: 
            arreglo_dict=[]
            for c in self.arreglo:
                arreglo_dict.append(c.dictt())
            return arreglo_dict 
        
        return {
            "num": self.num,
            "nombre": self.nombre,
            "ubi": self.ubi,
            "capacidad": self.capacidad,
            "numero_salas": self.numero_salas,
            "clasificacion": self.clasificacion,
            "total_ganancias": self.total_ganancias,
            "salas":self.salas.to_dict()
        }
        

    def cargar_desde_diccionario(self, diccionario):
        for cine_data in diccionario:
            nueva_cine = Cines(
                num=cine_data['num'],
                nombre=cine_data['nombre'],
                ubi=cine_data['ubi'],
                capacidad=cine_data['capacidad'],
                numero_salas=cine_data['numero_salas'],
                clasificacion=cine_data['clasificacion'],
                total_ganancias=cine_data['total_ganancias']
            )
            salas_data = cine_data.get('salas', [])
            salas = Salas()
            salas.objetos_salas(salas_data)

            nueva_cine.salas = salas
            self.arreglo.append(nueva_cine)


    def inserMongo(self, nombre, ubi, capacidad, numero_salas, clasificacion, salas):
        cine_dict = {
        'nombre': nombre,
        'ubicacion': ubi,
        'capacidad': capacidad,
        'numero_salas': numero_salas,
        'clasificacion': clasificacion,
        'salas': []
        }
        for sala in salas:  # Usar el parámetro salas en lugar de cine.salas
            sala_dict = {
                'numero_sala': sala.numero_sala,
                'capacidad': sala.capacidad,
                'formato_pantalla': sala.formato_pantalla,
                'sonido': sala.sonido,
                'tipo': sala.tipo,
                'funciones': []
            }
            for funcion in sala.funciones:
                funcion_dict = {
                    'nf': funcion.nf,
                    'hora_inicio': funcion.hora_inicio,
                    'duracion': funcion.duracion,
                    'tipo_proyeccion': funcion.tipo_proyeccion,
                    'precio_entrada': funcion.precio_entrada,
                    'pelicula': funcion.pelicula
                }
                sala_dict['funciones'].append(funcion_dict)
            cine_dict['salas'].append(sala_dict)
        print(cine_dict)  # Mover la impresión fuera del bucle

        try:
            self.mongo.insert_one("Cines", cine_dict)
            print("Cine agregado exitosamente.")
            
            if self.banderaguardar:
                self.cines.guardar_a_json("archivo.json")
                
        except Exception as e:
            print("Error al insertar el cine en la base de datos:", e)

            

    def cargar_desde_archivo(self):
        nombre_archivo = "archivo.json"
        try:
            with open(nombre_archivo, 'r') as archivo:
                data = json.load(archivo)
                # self.mongo = Mongo(db="basededates")
                # for cine_data in data:
                #     self.mongo.insert_one("Cines", cine_data)

                self.cargar_desde_diccionario(data)
                print(f"\nDatos cargados desde '{nombre_archivo}'\n")
        except FileNotFoundError:
            print(f"Archivo '{nombre_archivo}' no encontrado. Iniciando con lista vacía.\n")

    
    def guardar_a_json(self, nombre_archivo):
        data = self.dictt()
        with open(nombre_archivo, 'w') as archivo:
            json.dump(data, archivo, indent=4)
            


    def objetos_cines(self,data):
        cines_list = []
        for cine_data in data:
            cine_instance = Cines(
                num=cine_data['num'],
                nombre=cine_data['nombre'],
                ubi=cine_data['ubi'],
                capacidad=cine_data['capacidad'],
                numero_salas=cine_data['numero_salas'],
                clasificacion=cine_data['clasificacion'],
                total_ganancias=cine_data['total_ganancias']
                )
            salas=Salas()
            salas.objetos_salas(cine_data["salas"])
            cine_instance.salas=salas
            cines_list.append(cine_instance)


        for cine_instance in cines_list:
            print(f"Cine {cine_instance.num} - Nombre: {cine_instance.nombre} - Ubicación: {cine_instance.ubi}")
            print(f"Capacidad: {cine_instance.capacidad}")
            print(f"Número de salas: {cine_instance.numero_salas}")
            print(f"Clasificación: {cine_instance.clasificacion}")
            print(f"Total de ganancias: {cine_instance.total_ganancias}")

            for sala_instance in cine_instance.salas.arreglo:
                 print(f"\tSala {sala_instance.numero_sala} - Capacidad: {sala_instance.capacidad}")
                 print(f"\tFormato de pantalla: {sala_instance.formato_pantalla} - Sonido: {sala_instance.sonido} - Tipo: {sala_instance.tipo} ")
                 print(f"\tTotal de ganancias: {sala_instance.total_ganancias}")
    
    def Jsonn(self, archivo, data):
        try:
            with open(archivo, "r") as file:
                existing_data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            existing_data = []
        
        existing_data_set = set(json.dumps(item) for item in existing_data)

        for item in data:
            item_json = json.dumps(item)
            if item_json not in existing_data_set:
                existing_data.append(item)
                existing_data_set.add(item_json)
                
        with open(archivo, "w") as file:
            json.dump(existing_data, file, indent=4, default=lambda x: x.to_dict() if hasattr(x, 'to_dict') else x)

 
    def updateMongo(self, indice,columf,campof):
            
            query = {"num": indice}
            object_id = (self.mongo.find_One(self.myclient,"basededates","Cines", query))
            print (object_id)
            if object_id:
                colum = columf
                campo = campof
                print (self.mongo.update_one(self.myclient,"basededates","Cines",self.mongo.find_One(self.myclient,"basededates","Cines", query), colum, campo))
                query = {"num": indice }
                print (self.mongo.find_Oneever(self.myclient,"basededates","Cines", query))
                print("Documento actualizado exitosamente.")
            else:
                print("No se encontró ningún documento para actualizar con el índice proporcionado.")

    def updatemany(self,indice,json):
        
        self.mongo.update_manyy(self.myclient,"basededates","Cines",indice,"num",json)
        

    def deleteOneMongo (self,indice):
            self.mongo.delete_One(self.myclient,"basededates","Cines","num",indice)

    def updatecine(self,indice,documento):
        query = {"num": indice}
        object_id = (self.mongo.find_One(self.myclient,"basededates","Cines", query))
        print (object_id)
        if object_id: 
              print(self.deleteOneMongo(indice))
              self.mongo = Mongo(db="basededates")
              self.mongo.insert_one("Cines",documento.dictt())
        else:
                print("No se encontró ningún documento para actualizar con el índice proporcionado.")
  

    def deleteCollection (self):
            self.mongo.delete_many(self.myclient,"basededates","Cines")




if __name__ == '__main__':
    cine = Cines()
   
    #cine.cargar_desde_json(nombre_archivo)
    #cine.Json(data,nombre_archivo)


    funcion1 = Funciones(1,"18:00", "2 horas", "Digital", 10.5, "Spider-Man: No Way Home")
    funcion2 = Funciones(2,"20:30", "2.5 horas", "IMAX", 15.0, "Gwen Stacy: Into the Spider-Verse")
    funcion3 = Funciones(3,"22:00", "2 horas", "Digital", 10.5, "Avengers: Endgame")

    sala1 = Salas(1, 50, "3D", "Dolby Atmos", "VIP")
    sala2 = Salas(2, 40, "2D", "DTS", "Regular")
    sala3 = Salas(3, 30, "2D", "DTS", "Regular")

    cine1 = Cines(1,"CineCity", "Centro", 300, 5, "A")
    cine2 = Cines(2,"CineStar", "Sur", 200, 3, "B")


    sala1.funciones.agregar(funcion1)
    sala2.funciones.agregar(funcion2)

    cine1.salas.agregar(sala1)
    cine2.salas.agregar(sala2)

    
    cine.agregar(cine1)
    cine.agregar(cine2)

    #data = cine.dictt()
    #cine.writejson(data, nombre_archivo)
    # hola=cine.readjson("archivo.json")
    # print(hola)
    # cine.objetos_cines(hola)

    #hola=cine.readjson("archivo.json")

    # cine3 = Cines(3,"CineVicky", "Centro", 300, 5, "A")
    # sala3.funciones.agregar(funcion3)
    # cine3.salas.agregar(sala3)  
    # cine.agregar(cine3)
    # print(cine.dictt())

    # nombre_archivo = "archivo.json"
    # data = cine.dictt()
    # cine.writejson(data, nombre_archivo)
    data = cine.dictt()
    nombre_archivo = "archivo.json"
    cine.Jsonn(nombre_archivo,data)
    # Cargar desde el archivo JSON
    cine.ver() 
    
    #cine.guardar_a_json(nombre_archivo)


    # hola=cine.readjson("archivo.json")
    # print(hola)
    # cine.objetos_cines(hola)
    

    #print(f"Datos guardados en '{nombre_archivo}'.")

    # nombre_archivo = "archivo.json"
    
    # cine = Cines()
    # cine.objetos(nombre_archivo)
    # cine.ver()
    

    # nn=Cines(1,"CineVickyyys", "Centro", 300, 5, "A")
    # if cine.modificar(0, nn):
    #     print("Modificado:")
    # cine.ver()
    # if cine.eliminar(1):
    #     print("Eliminado:")
    # cine.ver()
    
pass
   

