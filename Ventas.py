import json
from Arreglo import Arreglo

class Ventas(Arreglo):
    def __init__(self, num_ticket = None,can_boletos = None,costo_boleto = None,total_venta = None,ganancia = None):
            super().__init__()
            self.banderaLista= num_ticket==None and can_boletos==None and costo_boleto==None 
            if self.banderaLista:  
                self.arreglo=[]
            else:
                self.arreglo=None

            self.num_ticket=num_ticket
            self.can_boletos = can_boletos
            self.costo_boleto = costo_boleto
            self.total_venta = total_venta
            self.ganancia = ganancia


    def mostrartabla(self):
            s=""
            for venta in self.arreglo:
                    s+=f'venta: {venta}'
            return s 
    def cargar_desde_archivo(self,nombre_archivo):
        try:
            data = self.readjson(nombre_archivo)
            self.objetos_ventas(data)
            print(f"\nDatos cargados desde '{nombre_archivo}'\n")
        except FileNotFoundError:
            print(f"Archivo '{nombre_archivo}' no encontrado. Iniciando con lista vacía.\n")

    def guardar_en_archivo(self,nombre_archivo):
        data = self.to_dict()
         
        self.writejson(data, nombre_archivo)
        print(f"\nDatos guardados en '{nombre_archivo}'\n")    

    def objetos_ventas(self,data):  
        self.arreglo=[] 
        if not data:
                print("No hay ventas para mostrar")
                return False
        for venta_data in data:
            venta_instance = Ventas(
                num_ticket=venta_data['num_ticket'],
                can_boletos=venta_data['can_boletos'],
                costo_boleto=venta_data['costo_boleto'],
                total_venta=venta_data['total_venta'],
                ganancia=venta_data['ganancia'],
                
            )
            self.agregar(venta_instance)
            

    def to_dict(self):
    
        if self.banderaLista: 
            arreglo_dict=[]
            for e in self.arreglo:
                arreglo_dict.append(e.to_dict())
            return arreglo_dict 
        return {
            'num_ticket': self.num_ticket,
            'can_boletos': self.can_boletos,
            'costo_boleto': self.costo_boleto,
            'total_venta': self.total_venta,
            'ganancia': self.ganancia,
           
        }


    def total_ganancias(self):
        ganancia_total= 0
        for venta in self.arreglo:
            print( "ganancia: ", venta.ganancia)
            ganancia_total += venta.ganancia
        return ganancia_total

    def __str__(self):
        if not self.banderaLista:
            return  f"Venta {self.num_ticket} - Cantidad de boletos: {self.can_boletos}\n" \
                    f"Costo boleto: {self.costo_boleto}\n" \
                    f"total de Venta: {self.total_venta}\n" \
                    f"Gancia: {self.ganancia}\n" 
        else:
                                                
            result = f"Es un arreglo de({len(self.arreglo)} elementos)"
            
            return result
