import json
from Funciones import Funciones
from Arreglo import Arreglo

class Salas(Arreglo):
    def __init__(self, numero_sala=None, capacidad=None, formato_pantalla=None, sonido=None, tipo=None, funciones=None):
        super().__init__()
        self.numero_sala = numero_sala
        self.capacidad = capacidad
        self.formato_pantalla = formato_pantalla
        self.sonido = sonido
        self.tipo = tipo
        self.funciones = funciones
        if self.funciones is None:
             self.funciones = Funciones()

            


    def to_dictt(self):
        funciones_data = [funcion.to_dict() for funcion in self.funciones.arreglo]
        
        return {
            "arreglo": [],  # Aquí debes proporcionar los datos necesarios para serializar Salas
            "numero_sala": self.numero_sala,
            "capacidad": self.capacidad,
            "formato_pantalla": self.formato_pantalla,
            "sonido": self.sonido,
            "tipo": self.tipo,
            "funciones": funciones_data
        }
    
    
    def guardar_en_archivo(self):
        nombre_archivo = "salas.json"   
        data = self.dictt()
         
        self.writejson(data, nombre_archivo)
        print(f"\nDatos guardados en '{nombre_archivo}'\n")    

    
    def cargar_desde_archivo(self):
        nombre_archivo = "salas.json"
        try:
            data = self.readjson(nombre_archivo)
            self.cargar_desde_diccionario(data)
            print(f"\nDatos cargados desde '{nombre_archivo}'\n")
        except FileNotFoundError:
            print(f"Archivo '{nombre_archivo}' no encontrado. Iniciando con lista vacía.\n")
   

    def cargar_desde_diccionario(self, diccionario):
        for sala_data in diccionario:
            nueva_sala = Salas(
                numero_sala=sala_data['numero_sala'],
                capacidad=sala_data['capacidad'],
                formato_pantalla=sala_data['formato_pantalla'],
                sonido=sala_data['sonido'],
                tipo=sala_data['tipo']
            )

            # Verificamos si hay funciones en los datos
            funciones_data = sala_data.get('funciones', [])
            funciones = Funciones()
            funciones.objetos(funciones_data)

            nueva_sala.funciones = funciones
            self.arreglo.append(nueva_sala)


 
    # def cargar_desde_archivo(self):
    #     nombre_archivo = "salas.json"
    #     try:
    #         data = self.readjson(nombre_archivo)
    #         self.objetos_salas(data)
    #         print(f"\nDatos cargados desde '{nombre_archivo}'\n")
    #     except FileNotFoundError:
    #         print(f"Archivo '{nombre_archivo}' no encontrado. Iniciando con lista vacía.\n")

    def __str__(self):
        if []== self.arreglo:
                                                return f"Sala {self.numero_sala} - Capacidad: {self.capacidad} personas\n" \
                                                f"Formato de pantalla: {self.formato_pantalla}\n" \
                                                f"Sistema de sonido: {self.sonido}\n" \
                                                f"Tipo de sala: {self.tipo}\n" 
        else:
                                                
                result = f"Es un arreglo de({len(self.arreglo)} elementos)"
                
                return result
        
    def dictt(self):
            if len(self.arreglo) <= 0:
                return self.to_dict()
            else:
                result = []
            for elemento in self.arreglo:
                sala_dict = elemento.to_dict()  
                sala_dict['funciones'] = [funcion.to_dict() for funcion in elemento.funciones.arreglo]
                result.append(sala_dict)
            return result

    def to_dict(self):
            return {k: v.to_dict() if k == 'funciones' else v for k, v in vars(self).items()} 
    

    def objetos_salas(self,data):
        sala_list = []
        for sala_data in data:
                sala_instance = Salas(
                numero_sala=sala_data['numero_sala'],
                capacidad=sala_data['capacidad'],
                formato_pantalla=sala_data['formato_pantalla'],
                sonido=sala_data['sonido'],
                tipo=sala_data['tipo']
                )
                funciones=Funciones()
                funciones.objetos(sala_data["funciones"])
                sala_instance.funciones=funciones 
                sala_list.append(sala_instance)
                self.arreglo = sala_list 

        for sala_instance in sala_list:
            print(f"\tSala {sala_instance.numero_sala} - Capacidad: {sala_instance.capacidad}")
            print(f"\tFormato de pantalla: {sala_instance.formato_pantalla} - Sonido: {sala_instance.sonido} - Tipo: {sala_instance.tipo}")

            if hasattr(sala_instance, 'funciones'):
                print("Funciones:")
                sala_instance.funciones.ver()
            # for funcion_instance in sala_instance.funciones.arreglo:
            #     print(f"\t\tFunción {funcion_instance.nf}")
            #     print(f"\t\tHora de inicio: {funcion_instance.hora_inicio}")
            #     print(f"\t\tDuración: {funcion_instance.duracion}")
            #     print(f"\t\tTipo de proyección: {funcion_instance.tipo_proyeccion}")
            #     print(f"\t\tPrecio de entrada: {funcion_instance.precio_entrada}")
            #     print(f"\t\tPelícula: {funcion_instance.pelicula}")

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