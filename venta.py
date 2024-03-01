
from Arreglo import Arreglo
from Ventas import Ventas
class venta():
    def __init__(self, ventas = None):
        
        if ventas is None:
            self.ventas = Ventas()
            self.banderaguardar = True 
            self.ventas.cargar_desde_archivo("ventas.json")
        else:
            self.ventas = ventas
            self.banderaguardar = False

    def ver_ventas(self):
            print("\nLista de Ventas:")
            for venta in self.ventas.arreglo:
                print(f"\nNum Ticket {venta.num_ticket} - Cantidad de Boletos: {venta.can_boletos} - Costo por boleto: {venta.costo_boleto}")
                print(f"Total de Venta: {venta.total_venta} - Ganancia: {venta.ganancia}")
            print("\n")



    def agregar_venta(self):
            print("Ingrese los detalles de la nueva venta:")
            can_boletos = int(input("Cantidad de boletos: "))
            costo_boleto = float(input("Costo por boleto: "))
            total_venta = can_boletos * costo_boleto
            ganancia = total_venta * 0.1
            num_ticket = len(self.ventas.arreglo)
            nueva_venta = Ventas(num_ticket = num_ticket, can_boletos=can_boletos, costo_boleto=costo_boleto, total_venta=total_venta, ganancia=ganancia)

            self.ventas.agregar(nueva_venta)
            if self.banderaguardar:
                self.ventas.guardar_en_archivo("ventas.json")
            print(f"\nVenta {num_ticket} agregada exitosamente!\n")


    def modificar_venta(self):
        #modificar venta
        self.ver_ventas()
        indice = int(input("Ingrese el índice de la Venta a modificar: "))
        if 0 <= indice < len(self.ventas.arreglo):
            nueva_can_boletos = int(input("Nueva cantidad de Boletos")) if input("Desea modificar la cantidad de Boletos? (s/n): ") == "s" else self.ventas.arreglo[indice].can_boletos
            nuevo_costo_boleto = float(input("Nuevo costo por boleto: ")) if input("Desea modificar el costo de boleto? (s/n): ") == "s" else self.ventas.arreglo[indice].costo_boleto
            nuevo_total_venta = nueva_can_boletos * nuevo_costo_boleto
            nueva_ganancia = nuevo_total_venta * 0.1
            num_ticket = indice
            venta_modificar = self.ventas.arreglo[indice]

            nueva_venta = Ventas(num_ticket = num_ticket, can_boletos=nueva_can_boletos, costo_boleto=nuevo_costo_boleto, total_venta=nuevo_total_venta, ganancia=nueva_ganancia)
            self.ventas.modificar(indice, nueva_venta)
            if self.banderaguardar:
                self.ventas.guardar_en_archivo("ventas.json")
            print(f"\nVenta {num_ticket} modificada exitosamente!\n")
        else:
            print("Error: No se han cargado las ventas.")


    def eliminar_venta(self):
        self.ver_ventas()
        indice = int(input("Ingrese el num Ticket de la venta a eliminar: "))
        if 0 <= indice < len(self.ventas.arreglo):
            self.ventas.eliminar(indice)
            if self.banderaguardar:
                self.ventas.guardar_en_archivo("ventas.json")
            print(f"\nVenta {indice} eliminada exitosamente!\n")
        else:
            print("Error: No se han cargado las ventas.")

    def consola_ventas(self):
        while True:
                print("Menú de Ventas:")
                print("1. Ver ventas")
                print("2. Agregar venta")
                print("3. Modificar Venta")
                print("4. Eliminar Venta")
                print("5. Salir")
                
                opcion = input("Ingrese el número de la opción deseada: ")

                if opcion == "1":
                        self.ver_ventas()
                elif opcion == "2":
                        self.agregar_venta()
                elif opcion == "3":
                        self.modificar_venta()
                elif opcion == "4":
                        self.eliminar_venta()   
                elif opcion == "5":
                    print("Hasta Luego!")
                    break
                else:
                        print("Opción inválida. Intente nuevamente.")

                print("\n")

  
if __name__ == '__main__':
    ventaa = venta()
    ventaa.consola_ventas()