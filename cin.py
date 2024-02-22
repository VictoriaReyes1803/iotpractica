from Salas import Salas
from Funciones import Funciones
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
        print("2. Agregar un nuevo cine")
        print("3. Modificar un cine existente")
        print("4. Eliminar un cine existente")
        print("5. Salir")


    def mostrar_lista_cines(self):
        print("\nLista de cines:")
        for cine in self.cines.arreglo:
            print(f"Cine {cine.num} - Nombre: {cine.nombre} - Ubicación: {cine.ubi}")
            print(f"Capacidad: {cine.capacidad}")
            print(f"Número de salas: {cine.numero_salas}")
            print(f"Clasificación: {cine.clasificacion}")

            # Iterar sobre todas las salas de cada cine y mostrarlas
            for sala in cine.salas.arreglo:
                print(f"\nSala {sala.numero_sala} - Capacidad: {sala.capacidad} personas")
                print(f"Formato de pantalla: {sala.formato_pantalla}")
                print(f"Sistema de sonido: {sala.sonido}")
                print(f"Tipo de sala: {sala.tipo}")

                if sala.funciones.arreglo:
                    print("\nFunciones:")
                    for funcion in sala.funciones.arreglo:
                        print(f"\nNo. Funcion {funcion.nf} - Hora de inicio: {funcion.hora_inicio} - Duración: {funcion.duracion}")
                        print(f"Tipo: {funcion.tipo_proyeccion}")
                        print(f"Precio: {funcion.precio_entrada}")
                        print(f"Película: {funcion.pelicula}")

            print("\n")

    def agregar_cine(self):
        num = input("Ingrese el nombre del cine: ")
        nombre = input("Ingrese el nombre del cine: ")
        ubi = input("Ingrese la ubicación del cine: ")
        capacidad = int(input("Ingrese la capacidad del cine: "))
        numero_salas = int(input("Ingrese el número de salas del cine: "))
        
        clasificacion = input("Ingrese la clasificación del cine: ")
        
        salas = Salas()
        sal = Sal(salas)
        sal.ciclo_menu_salas()
        salas = sal.salas
        print("salas:",salas)
        
        cine = Cines(num,nombre, ubi, capacidad, numero_salas, clasificacion, salas)
        self.cines.agregar(cine)

        if self.banderaguardar:
            self.cines.guardar_a_json("archivo.json");
        
        print("Cine agregado exitosamente.")
        return cine



    def modificar_cine(self):
        indice = int(input("Ingrese el índice del cine a modificar: "))
        if 0 <= indice < len(self.cines.arreglo):
            nombre = input("Ingrese el nuevo nombre del cine: ")
            ubi = input("Ingrese la nueva ubicación del cine: ")
            capacidad = int(input("Ingrese la nueva capacidad del cine: "))
            numero_salas = int(input("Ingrese el nuevo número de salas del cine: "))
            clasificacion = input("Ingrese la nueva clasificación del cine: ")
            cine = Cines(nombre=nombre, ubi=ubi, capacidad=capacidad, numero_salas=numero_salas, clasificacion=clasificacion)
            self.cines.modificar(indice, cine)
            print("Cine modificado exitosamente.")
        else:
            print("Índice fuera de rango. Intente nuevamente.")



    def eliminar_cine(self):
        indice = int(input("Ingrese el índice del cine a eliminar: "))
        if 0 <= indice < len(self.cines.arreglo):
            self.cines.eliminar(indice)
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
                print("¡Hasta luego!")
                break
            else:
                print("Opción no válida. Intente nuevamente.")
        print("\n")

if __name__ == "__main__":
    interfaz = Cin()
    interfaz.ejecutar()
