import json
from Funciones import Funciones
from Arreglo import Arreglo
import pymongo
from Mongo import Mongo

class Salas(Arreglo):
    def __init__(self, numero_sala=None, capacidad=None, formato_pantalla=None, sonido=None, tipo=None, funciones=None, total_ganancias=None):
        super().__init__()
        self.banderaLista= numero_sala==None and capacidad==None and formato_pantalla==None 
        if self.banderaLista:  
            self.arreglo=[]
        else:
            self.arreglo=None

        self.numero_sala = numero_sala
        self.capacidad = capacidad
        self.formato_pantalla = formato_pantalla
        self.sonido = sonido
        self.tipo = tipo
        self.funciones = funciones
        self.total_ganancias = total_ganancias
        
        if self.funciones is None:
             self.funciones = Funciones()
        #self.myclient = pymongo.MongoClient( "mongodb+srv://VictoriaReyes:1234567$@cluster0.ti3duhj.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

    def Total_ganancias_salas(self):
        ganancia_total= 0
        for sala in self.arreglo:
            print( "ganancia: ", sala.total_ganancias)
            ganancia_total += sala.total_ganancias
        return ganancia_total
    
    def guardar_en_archivo(self):
        nombre_archivo = "salas.json"   
        data = self.to_dict()
         
        self.writejson(data, nombre_archivo)
        print(f"\nDatos guardados en '{nombre_archivo}'\n")    

    
    def cargar_desde_archivo(self):
        nombre_archivo = "salas.json"
        try:
            data = self.readjson(nombre_archivo)
            # self.mongo = Mongo(db="basededates")
            # for sala_data in data:
            #         self.mongo.insert_one("Salas", sala_data)
            self.cargar_desde_diccionario(data)
            print(f"\nDatos cargados desde '{nombre_archivo}'\n")
        except FileNotFoundError:
            print(f"Archivo '{nombre_archivo}' no encontrado. Iniciando con lista vacía.\n")

    def mostrartabla(self):
            x=""
            for sala in self.arreglo:
                    x+=f'Sala: {sala}'
            return x
   
    def to_dict(self):
    
        if self.banderaLista: 
            arreglo_dict=[]
            for s in self.arreglo:
                arreglo_dict.append(s.to_dict())
            return arreglo_dict 
        return {
            "numero_sala": self.numero_sala,
            "capacidad": self.capacidad,
            "formato_pantalla": self.formato_pantalla,
            "sonido": self.sonido,
            "tipo": self.tipo,
            "total_ganancias": self.total_ganancias,
            "funciones":self.funciones.to_dict()
        }
        
    def updateMongo(self, indice,columf,campof):
            
            query = {"numero_sala": indice}
            object_id = (self.mongo.find_One(self.myclient,"basededates","Salas", query))
            print (object_id)
            if object_id:
                colum = columf
                campo = campof
                print (self.mongo.update_one(self.myclient,"basededates","Salas",self.mongo.find_One(self.myclient,"basededates","Salas", query), colum, campo))
                query = {"numero_sala": indice }
                print (self.mongo.find_Oneever(self.myclient,"basededates","Salas", query))
                print("Documento actualizado exitosamente.")
            else:
                print("No se encontró ningún documento para actualizar con el índice proporcionado.")

    def deleteOneMongo (self,indice):
            self.mongo.delete_One(self.myclient,"basededates","Salas","numero_sala",indice)

    def updatesala(self,indice,documento):
        query = {"numero_sala": indice}
        object_id = (self.mongo.find_One(self.myclient,"basededates","Salas", query))
        print (object_id)
        if object_id: 
              print(self.deleteOneMongo(indice))
              self.mongo = Mongo(db="basededates")
              self.mongo.insert_one("Salas",documento.to_dict())
        else:
                print("No se encontró ningún documento para actualizar con el índice proporcionado.")
  

    def deleteCollection (self):
            self.mongo.delete_many(self.myclient,"basededates","Salas")



    def cargar_desde_diccionario(self, diccionario):
        for sala_data in diccionario:
            nueva_sala = Salas(
                numero_sala=sala_data['numero_sala'],
                capacidad=sala_data['capacidad'],
                formato_pantalla=sala_data['formato_pantalla'],
                sonido=sala_data['sonido'],
                tipo=sala_data['tipo'],
                total_ganancias=sala_data['total_ganancias']
            )

            # Verificamos si hay funciones en los datos
            funciones_data = sala_data.get('funciones', [])
            funciones = Funciones()
            funciones.objetos(funciones_data)

            nueva_sala.funciones = funciones
            self.arreglo.append(nueva_sala)

    def __str__(self):
        if not self.banderaLista:
            return  f"Sala {self.numero_sala} - Capacidad: {self.capacidad} personas\n" \
                    f"Formato de pantalla: {self.formato_pantalla}\n" \
                    f"Sistema de sonido: {self.sonido}\n" \
                    f"Tipo de sala: {self.tipo}\n"\
                    f"Total de ganancias: {self.total_ganancias}\n"
        else:
                                                
            result = f"Es un arreglo de({len(self.arreglo)} elementos)"
            
            return result

      

    def objetos_salas(self,data):
        sala_list = []
        for sala_data in data:
                sala_instance = Salas(
                numero_sala=sala_data['numero_sala'],
                capacidad=sala_data['capacidad'],
                formato_pantalla=sala_data['formato_pantalla'],
                sonido=sala_data['sonido'],
                tipo=sala_data['tipo'],
                total_ganancias=sala_data['total_ganancias']
                )
                funciones=Funciones()
                funciones.objetos(sala_data["funciones"])
                sala_instance.funciones=funciones 
                sala_list.append(sala_instance)
                self.arreglo = sala_list 

        for sala_instance in sala_list:
            print(f"\tSala {sala_instance.numero_sala} - Capacidad: {sala_instance.capacidad}")
            print(f"\tFormato de pantalla: {sala_instance.formato_pantalla} - Sonido: {sala_instance.sonido} - Tipo: {sala_instance.tipo}")
            print(f"\tTotal de ganancias: {sala_instance.total_ganancias}") 

            if hasattr(sala_instance, 'funciones'):
                print("Funciones:")
                sala_instance.funciones.ver()
        print("\n")  


    
if __name__ == '__main__':
    sala = Salas() 
    sala1 = Salas(1,50,'3D','Dolby Atmos','VIP')
    sala2 = Salas(2, 40,'2D','DTS','VIPVicky')
 
    funcion1 = Funciones(1,"18:00", "2 horas", "Digital", 10.5, "Spider-Man: No Way Home")
    funcion2 = Funciones(1,"20:30", "2.5 horas", "IMAX", 15.0, "Gwen Stacy: Into the Spider-Verse")
    funcion3 = Funciones(2,"20:30", "2.5 horas", "IMAX", 15.0, "Gwen Stacy: Into the Spider-Verse")
    
    sala.agregar(sala1)
    sala.agregar(sala2)
    sala1.funciones.agregar(funcion1)
    sala2.funciones.agregar(funcion2)
    sala2.funciones.agregar(funcion3)

    data=sala.dictt()

    # sala.ver()
    # print(sala.dictt())
#     nn = Salas(1,60, '3D', 'HUMBEEE','VIP')
#     if sala.modificar(0, nn):
#         print("Modificado:") 
#     sala.ver()

#     if sala.eliminar(1):
#         print("Eliminado:")

    
    # data=sala.readjson("salas.json")
    # sala.objetos_salas(data)
    sala.ver()
    sala.writejson(data,"salas.json")
pass