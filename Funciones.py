from Arreglo import Arreglo
import json
from Mongo import Mongo
class Funciones(Arreglo):
    def __init__(self,nf=None, hora_inicio=None, duracion=None, tipo_proyeccion=None, precio_entrada=None, pelicula=None):
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
        # self.mongo = Mongo(db="basededates")
    
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
            'pelicula': self.pelicula
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

    def objetos(self,data):  
        self.arreglo=[] 
        if not data:
                print("No hay funciones para mostrar")
                return False
        for funcion_data in data:
            funcion_instance = Funciones(
                nf=funcion_data['nf'],
                hora_inicio=funcion_data['hora_inicio'],
                duracion=funcion_data['duracion'],
                tipo_proyeccion=funcion_data['tipo_proyeccion'],
                precio_entrada=funcion_data['precio_entrada'],
                pelicula=funcion_data['pelicula']
            )
            self.agregar(funcion_instance)
            

        for funcion_instance in self.arreglo:
            print(f"\t\tFunción {funcion_instance.nf}")
            print(f"\t\tHora de inicio: {funcion_instance.hora_inicio}")
            print(f"\t\tDuración: {funcion_instance.duracion}")
            print(f"\t\tTipo de proyección: {funcion_instance.tipo_proyeccion}")
            print(f"\t\tPrecio de entrada: {funcion_instance.precio_entrada}")
            print(f"\t\tPelícula: {funcion_instance.pelicula}")

    print("\n")  
  
    def cargar_desde_archivo(self,nombre_archivo):
            # nombre_archivo = "funciones.json"
        try:
            data = self.readjson(nombre_archivo)
            # for cine_data in data:
            #         self.mongo.insert_one("Funciones", cine_data)
            self.objetos(data)
            print(f"\nDatos cargados desde '{nombre_archivo}'\n")
        except FileNotFoundError:
            print(f"Archivo '{nombre_archivo}' no encontrado. Iniciando con lista vacía.\n")


    # def to_dictt(self):
    #     return {
    #         "arreglo": [],  # Aquí debes proporcionar los datos necesarios para serializar Funciones
    #         "nf": self.nf,
    #         "hora_inicio": self.hora_inicio,
    #         "duracion": self.duracion,
    #         "tipo_proyeccion": self.tipo_proyeccion,
    #         "precio_entrada": self.precio_entrada,
    #         "pelicula": self.pelicula,
    #         "numero_sala": self.numero_sala
    #     }

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