from Salas import Salas
from Mongo import Mongo
from Funciones import Funciones
import jsonpickle
from Cines import Cines
from Sal import Sal
from fun import fun


class Cin:
    def __init__(self, cines = None):
        super().__init__()
        if cines is None:
            self.cines = Cines()
            self.banderaguardar = True 
            self.cines.cargar_desde_archivo()
        else:
            self.cines = cines
            self.banderaguardar = False
        

    def mostrar_menu(self):
        print("\nMenu:")
        print("1. Ver lista de cines")
        print("2. Agregar un cine")
        print("3. Modificar un cine")
        print("4. Eliminar un cine")
        print("5. Salir")


    def mostrar_lista_cines(self):
        print("\nLista de cines:")
        for cine in self.cines.arreglo:
            print(f"Cine {cine.num} - Nombre: {cine.nombre} - Ubicación: {cine.ubi}")
            print(f"Capacidad: {cine.capacidad}")
            print(f"Número de salas: {cine.numero_salas}")
            print(f"Clasificación: {cine.clasificacion}")

           
            for sala in cine.salas.arreglo:
                print(f"\nSala {sala.numero_sala} - Capacidad: {sala.capacidad} personas")
                print(f"Formato de pantalla: {sala.formato_pantalla}")
                print(f"Sistema de sonido: {sala.sonido}")
                print(f"Tipo de sala: {sala.tipo}")
                print(f"Total de ganancias: {sala.total_ganancias}")

                if sala.funciones.arreglo:
                    print("\nFunciones:")
                    for funcion in sala.funciones.arreglo:
                        print(f"\nNo. Funcion {funcion.nf} - Hora de inicio: {funcion.hora_inicio} - Duración: {funcion.duracion}")
                        print(f"Tipo: {funcion.tipo_proyeccion}")
                        print(f"Precio: {funcion.precio_entrada}")
                        print(f"Película: {funcion.pelicula}")
                        print(f"Total Ganancias: {funcion.total_ganancias}")
                        print(f"Ventas: {funcion.ventas}")
                        if funcion.ventas.arreglo:
                            print("\nVentas:")
                            for venta in funcion.ventas.arreglo:
                                print(f"\nNum Ticket {venta.num_ticket} - Cantidad de Boletos: {venta.can_boletos} - Costo por boleto: {venta.costo_boleto}")
                                print(f"Total de Venta: {venta.total_venta} - Ganancia: {venta.ganancia}")

            print("\n")

    def agregar_cine(self):
        num = len(self.cines.arreglo)
        nombre = input("Ingrese el nombre del cine: ") 
        ubi = input("Ingrese la ubicación del cine: ")
        capacidad = int(input("Ingrese la capacidad del cine: "))
        numero_salas = int(input("Ingrese el número de salas del cine: "))
        clasificacion = input("Ingrese la clasificación del cine: ")

        salas = Salas()
        sal = Sal(salas)
        sal.ciclo_menu_salas()
        salas = sal.salas

        total_ganancias = salas.Total_ganancias_salas()
        print("TOTAL GANANCIAS\n")
        print(total_ganancias)

        cine = Cines(num,nombre, ubi, capacidad, numero_salas, clasificacion, salas, total_ganancias=total_ganancias)
        self.cines.agregar(cine)
        print ("********",cine.dictt())
        
        if self.banderaguardar:
            self.cines.guardar_a_json("archivo.json");
            # self.mongo = Mongo(db="basededates")
            # self.mongo.insert_one("Cines", cine.dictt())
            
        
        print("Cine agregado exitosamente.")
        return cine



    def modificar_cine(self):
        if []== self.cines.arreglo:
            print('No hay salas\n')
        else:
            self.mostrar_lista_cines()
            indice = int(input("Ingrese el índice del cine a modificar: "))
            if 0 <= indice < len(self.cines.arreglo):
                nuevo_nombre = input("Ingrese el nuevo nombre del cine: ") if input("Desea modificar el nombre? (s/n): ") == "s" else self.cines.arreglo[indice].nombre
                nueva_ubi = input("Ingrese la nueva ubicación del cine: ") if input("Desea modificar la ubicación? (s/n): ") == "s" else self.cines.arreglo[indice].ubi
                nueva_capacidad = int(input("Ingrese la nueva capacidad del cine: ")) if input("Desea modificar la capacidad? (s/n): ") == "s" else self.cines.arreglo[indice].capacidad
                nuevo_numero_salas = int(input("Ingrese el nuevo número de salas del cine: ")) if input("Desea modificar el número de salas? (s/n): ") == "s" else self.cines.arreglo[indice].numero_salas
                nueva_clasificacion = input("Ingrese la nueva clasificación del cine: ") if input("Desea modificar la clasificación? (s/n): ") == "s" else self.cines.arreglo[indice].clasificacion
                num_cine = indice 
                cine_modificar = self.cines.arreglo[indice]

                print(cine_modificar.salas.mostrartabla())

                salas = Salas()
                total_ganancias = salas.Total_ganancias_salas()
                print("TOTAL GANANCIAS\n")
                print(total_ganancias) 

                cine = Cines(num_cine,nuevo_nombre, nueva_ubi, nueva_capacidad, nuevo_numero_salas, nueva_clasificacion, cine_modificar.salas, total_ganancias=total_ganancias)  
                self.cines.modificar(indice, cine)
                print (cine)
               
                print("Cine modificado exitosamente.")

                modifica_salas = input("¿Desea modificar una sala? (s/n): ")
                if modifica_salas.lower() == "s":
                        sal = Sal(cine_modificar.salas)
                        sal.ciclo_menu_salas()
                        cine.salas = sal.salas
                
                if self.banderaguardar:
                        self.cines.guardar_a_json("archivo.json");
                        print("*****",cine.dictt())
                        # self.cines.updatemany(indice,cine.dictt())
                return cine
            else:
                print("Índice fuera de rango. Intente nuevamente.")



    def eliminar_cine(self):
        indice = int(input("Ingrese el índice del cine a eliminar: "))
        if 0 <= indice < len(self.cines.arreglo):
            self.cines.eliminar(indice)
            if self.banderaguardar:
                self.cines.guardar_a_json("archivo.json");
                # self.cines.deleteOneMongo(indice)
        
            print("Cine eliminado exitosamente.")
        else:
            print("Índice fuera de rango. Intente nuevamente.")

    def ejecutar(self):
        while True:
            self.mostrar_menu()
            opcion = input("Ingrese su opción: ")

            if opcion == "1":
                self.mostrar_lista_cines()
            elif opcion == "2":
                self.agregar_cine()
            elif opcion == "3":
                self.modificar_cine()
            elif opcion == "4":
                self.eliminar_cine()
            elif opcion == "5":
                # if self.banderaguardar:
                #     self.cines.deleteCollection()
                print("¡Hasta luego!")
                break
            else:
                print("Opción no válida. Intente nuevamente.")
        print("\n")

if __name__ == "__main__":
    interfaz = Cin()
    interfaz.ejecutar()
