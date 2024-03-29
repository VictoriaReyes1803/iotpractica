from Funciones import Funciones
import json
from Ventas import Ventas
from venta import venta
from prettytable import PrettyTable
from Mongo import Mongo
from venta import venta
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

        ventas = Ventas()
        ventaa = venta(ventas)
        ventaa.consola_ventas()
        ventas = ventaa.ventas

        total_ganancias = ventas.total_ganancias()
        print("TOTAL GANANCIAS POR FUNCIONES: \n")
        print(total_ganancias)

        nueva_funcion = Funciones( nf = nf, hora_inicio=hora_inicio, duracion=duracion, tipo_proyeccion=tipo_proyeccion,
                                  precio_entrada=precio_entrada, pelicula=pelicula,total_ganancias= total_ganancias, ventas = ventas )

        self.funciones.agregar(nueva_funcion)

        print ("*************************************",nueva_funcion.to_dict())
        
        if self.banderaguardar:
            self.funciones.guardar_en_archivo("funciones.json")
            # self.mongo = Mongo(db="basededates")
            # self.mongo.insert_one("Funciones", nueva_funcion.to_dict())


        print(f"\nFunción {pelicula} agregada exitosamente!\n")
       

    def ver_funciones(self):
        if self.funciones:
            print("\nLista de funciones:")
            for funcion in self.funciones.arreglo:
                    print(f"\nNo. Funcion {funcion.nf} - Hora de inicio: {funcion.hora_inicio} - Duracion: {funcion.duracion}")
                    print(f"Tipo: {funcion.tipo_proyeccion}")
                    print(f"Precio: {funcion.precio_entrada}")
                    print(f"Pelicula: {funcion.pelicula}")
                    print(f"Total Ganancias: {funcion.total_ganancias}")
                    if funcion.ventas.arreglo:
                        print("\nVentas:")
                        for venta in funcion.ventas.arreglo:
                            print(f"\nNum Ticket {venta.num_ticket} - Cantidad de Boletos: {venta.can_boletos} - Costo por boleto: {venta.costo_boleto}")
                            print(f"Total de Venta: {venta.total_venta} - Ganancia: {venta.ganancia}")
                    
                    print("\n")
            ventas = Ventas()
            a = ventas.total_ganancias( )
            print("TOTAL GANANCIAS\n")
            print(a)

            # self.mongo = Mongo(db="basededates")
            # resultados = self.mongo.find("Funciones")
            # print("Funciones encontradas en MONGO:", resultados)
            self.funciones.ver()
        else:
            print("Error: No se han cargado las funciones.")


    def modificar_funcion(self):
        self.ver_funciones()
        indice = int(input("Ingrese el índice de la función a modificar: "))
        if 0 <= indice < len(self.funciones.arreglo):
            nueva_hora_inicio = input("Nueva hora de inicio: ") if input("Desea modificar la hora de inicio? (s/n): ") == "s" else self.funciones.arreglo[indice].hora_inicio
            nueva_duracion = input("Nueva duración: ") if input("Desea modificar la duración? (s/n): ") == "s"  else self.funciones.arreglo[indice].duracion
            nuevo_tipo_proyeccion = input("Nuevo tipo de proyección: ") if input("Desea modificar el tipo de proyección? (s/n): ") == "s" else self.funciones.arreglo[indice].tipo_proyeccion
            nuevo_precio_entrada = float(input("Nuevo precio de entrada: ")) if input("Desea modificar el precio de entrada? (s/n): ") == "s" else self.funciones.arreglo[indice].precio_entrada
            nueva_pelicula = input("Nuevo nombre de la película: ") if input("Desea modificar el nombre de la película? (s/n): ") == "s" else self.funciones.arreglo[indice].pelicula
            indice_actual = indice
            funcion_modificar = self.funciones.arreglo[indice]
            print(funcion_modificar.ventas.mostrartabla())

            ventas = Ventas()
            total_ganancias = ventas.total_ganancias()
            print("TOTAL GANANCIAS POR FUNCIONES: \n")
            print(total_ganancias)

            nueva_funcion = Funciones(nf= indice_actual,hora_inicio=nueva_hora_inicio, duracion=nueva_duracion,
                                      tipo_proyeccion=nuevo_tipo_proyeccion, precio_entrada=nuevo_precio_entrada,
                                      pelicula=nueva_pelicula,total_ganancias=total_ganancias, ventas = funcion_modificar.ventas)

            self.funciones.modificar(indice, nueva_funcion)
            print (nueva_funcion)

            print('Función modificada\n')
            modificar_ventas = input("¿Desea modificar una venta? (s/n): ")
            if modificar_ventas.lower() == 's':
                    ventaa = venta(nueva_funcion.ventas)
                    ventaa.consola_ventas()
                    nueva_funcion.ventas = ventaa.ventas

            if self.banderaguardar:
                self.funciones.guardar_en_archivo("funciones.json")
               
            return nueva_funcion
        else:
            print("Índice fuera de rango. Intente nuevamente.")

    def eliminar_funcion(self):
        self.ver_funciones()
        indice = int(input("Ingrese el índice de la función a eliminar: "))
        if 0 < indice < len(self.funciones.arreglo):
            self.funciones.eliminar(indice)
            self.funciones.nf = len(self.funciones.arreglo)
            if self.banderaguardar:
                self.funciones.guardar_en_archivo("funciones.json")
                # self.funciones.deleteOneMongo(indice)
            print(f"\nFunción eliminada exitosamente!\n")
        else:
            print("Índice fuera de rango. Intente nuevamente.")
    

    def consola(self):
        while True:
            print("Menú de funciones:")
            print("1. Ver funciones")
            print("2. Agregar función")
            print("3. Modificar función")
            print("4. Eliminar función")
            print("5. Salir")

            opcion = input("Ingrese el número de la opción deseada: ")

            if opcion == "1":
                self.ver_funciones()
            elif opcion == "2":
                self.agregar_funcion()
            elif opcion == "3":
                self.modificar_funcion()
            elif opcion == "4":
                self.eliminar_funcion()   
            elif opcion == "5":
                if self.banderaguardar:
                    # self.funciones.deleteCollection()
                    print("Hasta Luego!")
                break
            else:
                print("Opción inválida. Intente nuevamente.")

        print("\n")


if __name__ == '__main__':
    consola = fun()
    consola.consola()

   