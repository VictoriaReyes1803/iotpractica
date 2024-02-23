from Sal import Sal
from fun import fun
from cin import Cin
class Menu:
    
    def main_menu():
        funcion = fun()
        sala = Sal()
        cine = Cin()
        while True:
            print("1. Funcion")
            print("2. Sala")
            print("3. Cine")
            print("4. Salir")
            opcion = input("Ingrese la opcion: ")
            if opcion == "1":
                funcion.consola()
            elif opcion =="2":
                sala.ciclo_menu_salas()
            elif opcion == "3":
                cine.ejecutar()
            elif opcion == "4":
                break
            else:
                print("Opcion invalida")

if __name__ == '__main__':
    Menu.main_menu()