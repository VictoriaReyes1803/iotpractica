import json


class Arreglo:
    def __init__ (self):
        self.arreglo = []
        

    def agregar(self, instancia):
            if instancia == None:
                return False
            else:
              
                nf = len(self.arreglo)
                num = len(self.arreglo)
                numero_sala = len(self.arreglo)
                self.arreglo.append(instancia)
                return True,nf,num,numero_sala

    def modificar(self, indice, instancia):
        if 0 <= indice < len(self.arreglo):
            self.arreglo[indice] = instancia
            return True
        else:
             return False

    def eliminar(self, indice):
        if 0 <= indice < len(self.arreglo):
            del self.arreglo[indice]
            return True
        else:
            return False

    def ver(self):
        if len(self.arreglo) <= 0:
            return "No hay elementos para mostrar"
        else:
            cadena=""
            for i, elemento in enumerate(self.arreglo):
                cadena+=(f"{i + 1}:\n{elemento}\n")
            return cadena

    def dictt(self):
            if not self.arreglo:
                return self.to_dict()
            else:
             a=[]
             for elemento in self.arreglo:
                a.append(elemento.to_dict())
              

            return a
    
    def write_json(self, archivo, data):
        added = False
        try:
            with open(archivo, "r") as file:
                existing_data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            existing_data = []

        existing_data_set = set(json.dumps(item) for item in existing_data)

        for item in data:
            item_json = json.dumps(item)
            if item_json not in existing_data_set:
                existing_data.append(item)
                existing_data_set.add(item_json)
                added = True

        with open(archivo, "w") as file:
            json.dump(existing_data, file, indent=4, default=lambda x: x.to_dict() if hasattr(x, 'to_dict') else x)

        return added
    
    def read_json(self, file):
        with open(file, 'r') as file:
            data = json.load(file)
        return data 

    def to_dict(self):
        return vars(self) 
    
    def writejson (self,data, nombre_archivo):
         with open(nombre_archivo, 'w') as archivo:
            json.dump(data, archivo,indent=4)
    
    def readjson (self,nombre_archivo):
        with open(nombre_archivo, 'r') as archivo:
            data = json.load(archivo)
        return data
    

pass