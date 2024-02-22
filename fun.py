from Funciones import Funciones
import json
from prettytable import PrettyTable

class fun():
    def __init__(self, funciones=None ):
        if funciones is None:
                self.funciones = Funciones()
                self.banderaguardar = True 
                self.funciones.cargar_desde_archivo("funciones.json")
        else:
                self.funciones = funciones
                self.banderaguardar = False
           
    def agregar_funcion(self):
        print("Ingrese los detalles de la nueva función:")
        hora_inicio = input("Hora de inicio: ")
        duracion = input("Duración: ")
        tipo_proyeccion = input("Tipo de proyección: ")
        precio_entrada = float(input("Precio de entrada: "))
        pelicula = input("Nombre de la película: ")
        nf = len(self.funciones.arreglo) 
        
        nueva_funcion = Funciones( nf = nf, hora_inicio=hora_inicio, duracion=duracion, tipo_proyeccion=tipo_proyeccion,
                                  precio_entrada=precio_entrada, pelicula=pelicula)

        self.funciones.agregar(nueva_funcion)


        if self.banderaguardar:
    
            self.funciones.guardar_en_archivo("funciones.json")
            


        print(f"\nFunción {pelicula} agregada exitosamente!\n")

    def ver_funciones(self):
        if self.funciones:
            print("\nLista de funciones:")
            self.funciones.ver()
        else:
            print("Error: No se han cargado las funciones.")


    def modificar_funcion(self):
        self.funciones.ver()
        indice = int(input("Ingrese el índice de la función a modificar: "))
        if 0 <= indice < len(self.funciones.arreglo):
            nueva_hora_inicio = input("Nueva hora de inicio: ")
            nueva_duracion = input("Nueva duración: ")
            nuevo_tipo_proyeccion = input("Nuevo tipo de proyección: ")
            nuevo_precio_entrada = float(input("Nuevo precio de entrada: "))
            nueva_pelicula = input("Nuevo nombre de la película: ")
            indice_actual = len(self.funciones.arreglo)

            nueva_funcion = Funciones(nf= indice_actual,hora_inicio=nueva_hora_inicio, duracion=nueva_duracion,
                                      tipo_proyeccion=nuevo_tipo_proyeccion, precio_entrada=nuevo_precio_entrada,
                                      pelicula=nueva_pelicula)

            self.funciones.modificar(indice, nueva_funcion)
            if self.banderaguardar:
        
                self.funciones.guardar_en_archivo("funciones.json")
            print(f"\nFunción modificada exitosamente!\n")
        else:
            print("Índice fuera de rango. Intente nuevamente.")

    def eliminar_funcion(self):
        indice = int(input("Ingrese el índice de la función a eliminar: "))
        if 0 <= indice < len(self.funciones.arreglo):
            self.funciones.eliminar(indice)
            if self.banderaguardar:
                self.funciones.guardar_en_archivo("funciones.json")
            print(f"\nFunción eliminada exitosamente!\n")
        else:
            print("Índice fuera de rango. Intente nuevamente.")
    


    def consola(self):
        while True:
            print("Menú de funciones:")
            print("1. Agregar función")
            print("2. Ver funciones")
            print("3. Modificar función")
            print("4. Eliminar función")
            print("5. Salir")

            opcion = input("Ingrese el número de la opción deseada: ")

            if opcion == "1":
                self.agregar_funcion()
            elif opcion == "2":
                self.ver_funciones()
            elif opcion == "3":
                self.modificar_funcion()
            elif opcion == "4":
                self.eliminar_funcion()
            elif opcion == "5":
                print("Hasta Luego!")
                break
            else:
                print("Opción inválida. Intente nuevamente.")

        print("\n")


if __name__ == '__main__':
    consola = fun()
    consola.consola()

   