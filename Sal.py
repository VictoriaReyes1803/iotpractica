from Salas import Salas
from Funciones import Funciones
from fun import fun
from prettytable import PrettyTable
class Sal():
    def __init__(self, salas = None):
        
        if salas is None:
            self.salas = Salas()
            self.banderaguardar = True 
            self.salas.cargar_desde_archivo()
        else:
            self.salas = salas
            self.banderaguardar = False

    def ver_salas(self):
        print("\nLista de Salas:")
        for sala in self.salas.arreglo:
            print(f"\nSala {sala.numero_sala} - Capacidad: {sala.capacidad} personas")
            print(f"Formato de pantalla: {sala.formato_pantalla}")
            print(f"Sistema de sonido: {sala.sonido}")
            print(f"Tipo de sala: {sala.tipo}")

            if sala.funciones.arreglo:
                print("\nFunciones:")
                for funcion in sala.funciones.arreglo:
                    print(f"\nNo. Funcion {funcion.nf} - Hora de inicio: {funcion.hora_inicio} - Duracion: {funcion.duracion}")
                    print(f"Tipo: {funcion.tipo_proyeccion}")
                    print(f"Precio: {funcion.precio_entrada}")
                    print(f"Pelicula: {funcion.pelicula}")

        print("\n")


    def ciclo_menu_salas(self):
        while True:
            self.menu_salas()
            opcion = int(input("Opción: "))

            if opcion == 1:
                self.agregar_sala()
            elif opcion == 2:
                self.ver_salas()
            elif opcion == 3:
                self.eliminar_sala()
            elif opcion == 4:
                self.modificar_sala()
            elif opcion == 6:
                print('Hasta Luego\n')
                break
            else:
                print('Opción no válida')
        print("\n")

    def menu_salas(self):
        print("Menú salas:")
        print("1. Agregar")
        print("2. Ver")
        print("3. Eliminar")
        print("4. Modificar")
        print("6. salir")

    def agregar_sala(self):
        print("Ingrese los detalles de la nueva Sala:")
        
        capacidad = int(input("Capacidad: "))
        formato_pantalla = input("Formato de pantalla: ")
        sonido = input("Sistema de sonido: ")
        tipo = input("Tipo de sala: ")
        numero_sala =  input("Tipo de sala: ")

        funciones = Funciones()
        Fun = fun(funciones)
        Fun.consola()
        funciones = Fun.funciones


        newsala = Salas(numero_sala,capacidad, formato_pantalla, sonido, tipo, funciones)

        print("newsala:",newsala)

        print("self.salas.agregar:",self.salas.agregar(newsala)) 
    
        self.ver_salas()

        if self.banderaguardar:
            self.salas.guardar_en_archivo()

        print("\n Sala agregada exitosamente!")
        return newsala 

    def eliminar_sala(self):
        self.ver_salas()
        i = int(input("Eliminar sala: "))
        bool = self.salas.eliminar(i)
        if bool:
            print('Eliminado\n')
        if self.banderaguardar:
            self.salas.guardar_en_archivo()
        else:
            print('No se pudo eliminar\n')


    def modificar_sala(self):
        if []== self.salas.arreglo:
            print('No hay salas\n')
        else:
            self.ver_salas()
            i = int(input("Modificar sala: "))
            nueva_capacidad = int(input("Nueva capacidad: "))
            nuevo_formato_pantalla = input("Nuevo formato de pantalla: ")
            nuevo_sonido = input("Nuevo sistema de sonido: ")
            nuevo_tipo = input("Nuevo tipo de sala: ")

            sala_modificar = self.salas.arreglo[i]

            # Obtener las funciones asociadas a la sala y convertirlas a una lista de diccionarios
            funciones_sala = [funcion.__dict__ for funcion in sala_modificar.funciones.arreglo]

            # Aquí puedes hacer algo con las funciones, como mostrarlas
            for funcion in funciones_sala:
                print(f'Función: {funcion}')
        
            sala = Salas(nueva_capacidad, nuevo_formato_pantalla, nuevo_sonido, nuevo_tipo, funciones_sala)
            bool = self.salas.modificar(i, sala)
            if self.banderaguardar:
                self.salas.guardar_en_archivo()
            if bool:
                print('Modificado\n')
                modificar_funciones = input("¿Desea modificar una funcion? (s/n): ")
                if modificar_funciones.lower() == 's':
                    
                    Fun = fun(sala.funciones)
                    Fun.consola()
                    sala.funciones = Fun.funciones
                    if self.banderaguardar:
                        self.salas.guardar_en_archivo()
                        
                return sala
            else:
                print('No se pudo modificar\n')

if __name__ == '__main__':
    sal = Sal()
    sal.ciclo_menu_salas()
