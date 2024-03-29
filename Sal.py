from Salas import Salas
from Funciones import Funciones
from fun import fun
from prettytable import PrettyTable
import jsonpickle
from Mongo import Mongo
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
            print(f"Total de ganancias: {sala.total_ganancias}")
            print(f"Funciones: {sala.funciones}")

            if sala.funciones.arreglo:
                print("\nFunciones:")
                for funcion in sala.funciones.arreglo:
                    print(f"\nNo. Funcion {funcion.nf} - Hora de inicio: {funcion.hora_inicio} - Duracion: {funcion.duracion}")
                    print(f"Tipo: {funcion.tipo_proyeccion}")
                    print(f"Precio: {funcion.precio_entrada}")
                    print(f"Pelicula: {funcion.pelicula}")
                    print(f"Total Ganancias: {funcion.total_ganancias}")
                    print(f"Ventas: {funcion.ventas}")
                    if funcion.ventas.arreglo:
                        print("\nVentas:")
                        for venta in funcion.ventas.arreglo:
                            print(f"\nNum Ticket {venta.num_ticket} - Cantidad de Boletos: {venta.can_boletos} - Costo por boleto: {venta.costo_boleto}")
                            print(f"Total de Venta: {venta.total_venta} - Ganancia: {venta.ganancia}")

        print("\n")


    def ciclo_menu_salas(self):
        while True:
            self.menu_salas()
            opcion = int(input("Opción: "))

            if opcion == 1:
                self.ver_salas()
                
            elif opcion == 2:
                self.agregar_sala()
            elif opcion == 3:
                self.modificar_sala()
            elif opcion == 4:
                self.eliminar_sala()
            elif opcion == 5:
                # if self.banderaguardar:
                #     self.salas.deleteCollection()
                print('Hasta Luego\n')
                break
            else:
                print('Opción no válida')
        print("\n")

    def menu_salas(self):
        print("Menú salas:")
        print("1. Ver")
        print("2. Agregar")
        print("3. Modificar")
        print("4. Eliminar")
        print("5. salir")

    def agregar_sala(self):
        print("Ingrese los detalles de la nueva Sala:")
        
        capacidad = int(input("Capacidad: "))
        formato_pantalla = input("Formato de pantalla: ")
        sonido = input("Sistema de sonido: ")
        tipo = input("Tipo de sala: ")
        numero_sala =  len(self.salas.arreglo) + 1

        funciones = Funciones()
        Fun = fun(funciones)
        Fun.consola()
        funciones = Fun.funciones

        total_ganancias = funciones.Total_ganancias()
        print("TOTAL GANANCIAS\n")
        print(total_ganancias)

        newsala = Salas(numero_sala,capacidad, formato_pantalla, sonido, tipo, funciones,total_ganancias = total_ganancias,)
        print("self.salas.agregar:",self.salas.agregar(newsala)) 
        
        print ("*************************************",newsala.to_dict())
    
        if self.banderaguardar:
            self.salas.guardar_en_archivo()
            # self.mongo = Mongo(db="basededates")
            # self.mongo.insert_one("Salas", newsala.to_dict())

        print("\n Sala agregada exitosamente!")
        return newsala 

    def eliminar_sala(self):
        self.ver_salas()
        i = int(input("Eliminar sala: "))
        if 0 < i < len(self.salas.arreglo):
         self.salas.eliminar(i)
        # self.salas.deleteOneMongo(i)
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
            i = int(input("Numero de la sala a modificar: "))
            if 0 <= i < len(self.salas.arreglo):
                nueva_capacidad = int(input("Nueva capacidad: ")) if input("Desea modificar la capacidad? (s/n): ").lower() == 's' else self.salas.arreglo[i].capacidad
                nuevo_formato_pantalla = input("Nuevo formato de pantalla: ") if input("Desea modificar el formato de pantalla? (s/n): ").lower() == 's' else self.salas.arreglo[i].formato_pantalla    
                nuevo_sonido = input("Nuevo sistema de sonido: ") if input("Desea modificar el sistema de sonido? (s/n): ").lower() == 's' else self.salas.arreglo[i].sonido
                nuevo_tipo = input("Nuevo tipo de sala: ") if input("Desea modificar el tipo de sala? (s/n): ").lower() == 's' else self.salas.arreglo[i].tipo
                numero_sala =  i
                sala_modificar = self.salas.arreglo[i]

                print(sala_modificar.funciones.mostrartabla()) 

                funciones = Funciones()
                total_ganancias = funciones.Total_ganancias()
                print("TOTAL GANANCIAS\n")
                print(total_ganancias)

                newsala = Salas(numero_sala,nueva_capacidad, nuevo_formato_pantalla, nuevo_sonido, nuevo_tipo, sala_modificar.funciones,total_ganancias=total_ganancias)
                self.salas.modificar(i, newsala)
                print (newsala)

                print('Sala Modificada\n')
                modificar_funciones = input("¿Desea modificar una funcion? (s/n): ")
                if modificar_funciones.lower() == 's':
                        Fun = fun(sala_modificar.funciones)
                        Fun.consola()
                        newsala.funciones = Fun.funciones
                    
                if self.banderaguardar:
                    self.salas.guardar_en_archivo()
                    # self.salas.updatesala(i,newsala)

                return newsala
            else:
                print('No se pudo modificar\n')

if __name__ == '__main__':
    sal = Sal()
    sal.ciclo_menu_salas()
