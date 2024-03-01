from Arreglo import Arreglo
import json
from Ventas import Ventas
from Mongo import Mongo
import pymongo
class Funciones(Arreglo):
    def __init__(self,nf=None, hora_inicio=None, duracion=None, tipo_proyeccion=None, precio_entrada=None, pelicula=None, ventas = None, total_ganancias = None):
        super().__init__()
        self.banderaLista= nf==None and hora_inicio==None and duracion==None 
        if self.banderaLista:  
            self.arreglo=[]
        else:
            self.arreglo=None

            self.nf=nf
            self.hora_inicio = hora_inicio
            self.duracion = duracion
            self.tipo_proyeccion = tipo_proyeccion
            self.precio_entrada = precio_entrada
            self.pelicula = pelicula
            self.total_ganancias = total_ganancias
        self.ventas = ventas
        
        
        if self.ventas is None:
             self.ventas = Ventas()
        #self.myclient = pymongo.MongoClient( "mongodb+srv://VictoriaReyes:1234567$@cluster0.ti3duhj.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

    
    def Total_ganancias(self):
        ganancia_total= 0
        for funcion in self.arreglo:
            print( "ganancia: ", funcion.total_ganancias)
            ganancia_total += funcion.total_ganancias
        return ganancia_total
    
    def to_dict(self):

        if self.banderaLista: 
            arreglo_dict=[]
            for e in self.arreglo:
                arreglo_dict.append(e.to_dict())
            return arreglo_dict 
        return {
            'nf': self.nf,
            'hora_inicio': self.hora_inicio,
            'duracion': self.duracion,
            'tipo_proyeccion': self.tipo_proyeccion,
            'precio_entrada': self.precio_entrada,
            'pelicula': self.pelicula,
            'total_ganancias': self.total_ganancias,
            'ventas': self.ventas.to_dict()
        }
    

    def __str__(self):
        if not self.banderaLista:
            return f"No. Funcion {self.nf} - Funcion {self.hora_inicio} - Duracion: {self.duracion}\n" \
               f"Tipo: {self.tipo_proyeccion}\n" \
               f"Precio: {self.precio_entrada}\n" \
               f"Pelicula: {self.pelicula}\n" 
        else:
            
            result = f"Es un arreglo de({len(self.arreglo)} elementos)"
            
            return result
    def verr(self):
        if not self.arreglo:
            print("No hay funciones disponibles.")
        else:
            for i, funcion in enumerate(self.arreglo, start=1):
                print(f"Función {i}: {funcion}")

    def guardar_en_archivo(self,nombre_archivo):
        data = self.to_dict()
         
        self.writejson(data, nombre_archivo)
        print(f"\nDatos guardados en '{nombre_archivo}'\n")    

    def updateMongo(self, indice,columf,campof):
        
        query = {"nf": indice}
        object_id = (self.mongo.find_One(self.myclient,"basededates","Funciones", query))
        print (object_id)
        if object_id:
            colum = columf
            campo = campof
            print (self.mongo.update_one(self.myclient,"basededates","Funciones",self.mongo.find_One(self.myclient,"basededates","Funciones", query), colum, campo))
            query = {"nf": indice }
            print (self.mongo.find_Oneever(self.myclient,"basededates","Funciones", query))
            print("Documento actualizado exitosamente.")
        else:
            print("No se encontró ningún documento para actualizar con el índice proporcionado.")

    def deleteOneMongo (self,indice):
        self.mongo.delete_One(self.myclient,"basededates","Funciones","nf",indice)

    def deleteCollection (self):
        self.mongo.delete_many(self.myclient,"basededates","Funciones")

    def mostrartabla(self):
            s=""
            for funcion in self.arreglo:
                    s+=f'Función: {funcion}'
            return s 
    

    def objetos(self,data):  
        self.arreglo=[] 
        if not data:
                print("No hay funciones para mostrar")
                return False
        fun_list = []
        for funcion_data in data:
                funcion_instance = Funciones(
                nf=funcion_data['nf'],
                hora_inicio=funcion_data['hora_inicio'],
                duracion=funcion_data['duracion'],
                tipo_proyeccion=funcion_data['tipo_proyeccion'],
                precio_entrada=funcion_data['precio_entrada'],
                pelicula=funcion_data['pelicula'],
                total_ganancias=funcion_data['total_ganancias']
                )
                ventas=Ventas()
                ventas.objetos_ventas(funcion_data["ventas"])
                funcion_instance.ventas=ventas
                fun_list.append(funcion_instance)
                self.arreglo = fun_list 

        for funcion_instance in fun_list:
            print(f"\t\tFunción {funcion_instance.nf}")
            print(f"\t\tHora de inicio: {funcion_instance.hora_inicio}")
            print(f"\t\tDuración: {funcion_instance.duracion}")
            print(f"\t\tTipo de proyección: {funcion_instance.tipo_proyeccion}")
            print(f"\t\tPrecio de entrada: {funcion_instance.precio_entrada}")
            print(f"\t\tPelícula: {funcion_instance.pelicula}")
            print(f"\t\tTotal de ganancias: {funcion_instance.total_ganancias}")

            if hasattr(funcion_instance, 'ventas'):
                print("Ventas:")
                funcion_instance.ventas.ver()

    print("\n")  
  
    def cargar_desde_archivo(self,nombre_archivo):
        try:
            data = self.readjson(nombre_archivo)
            # self.mongo = Mongo(db="basededates")
            # for cine_data in data:
            #         self.mongo.insert_one("Funciones", cine_data)
            self.objetos(data)
            print(f"\nDatos cargados desde '{nombre_archivo}'\n")
        except FileNotFoundError:
            print(f"Archivo '{nombre_archivo}' no encontrado. Iniciando con lista vacía.\n")


if __name__ == '__main__':
    
    funcion1 = Funciones(1,"18:00", "2 horas", "Digital", 10.5, "Spider-Man: No Way Home")
    funcion2 = Funciones(2,"20:30", "2.5 horas", "IMAX", 15.0, "Gwen Stacy: Into the Spider-Verse")

    funcion=Funciones()
    funcion = Funciones(nf=3, hora_inicio="22:00", duracion="2 horas", tipo_proyeccion="digital", precio_entrada=1000, pelicula="Avengers: Endgame")


    arreglo_dict = funcion.to_dict()
    #print(arreglo_dict)
    funcion.dictt()

    funcion.agregar(funcion1)
    funcion.agregar(funcion2)

    # print("Ver:")
    # funcion.ver()
    #print(funcion.dictt())

    # new = Funciones(1,"22:00", "2 horas", "Digital", 12.0, "Avengers: Endgame")
    # funcion.modificar(0, new)

    # print("\nModificado:")
    # funcion.ver()
    # funcion.eliminar(0)
    # print("\nEliminado:")
    # funcion.ver()
    # print(funcion)
    # print(funcion1)
    # funcio=funcion.writejson(funcion.dictt(), "funciones.json")
    # print(funcio)
    hola=funcion.readjson( "funciones.json")
    print(hola)
    funcion.objetos(hola)

   
    
pass