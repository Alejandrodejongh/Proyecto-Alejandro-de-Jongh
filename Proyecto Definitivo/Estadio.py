from Restaurante import Restaurante


class Estadio:
    def __init__(self,id,nombre,capacidad,locacion,restaurantes):
        self.id=id 
        self.nombre=nombre
        self.capacidad=capacidad 
        self.locacion=locacion 
        self.restaurantes=[]
        self.crear_restaurantes(restaurantes)
    

#Se importa la Clase Restaurante para poder crear de una vez los Restaurantes asociados a cada Estadio y meterlos
#en una lista de Restaurantes    
    def crear_restaurantes(self,restaurantes):
        for r in restaurantes:
            restaurante= Restaurante(r["name"], r["products"])
            self.restaurantes.append(restaurante)
       


    def mostrar(self):
        print("Id:",self.id)
        print("Nombre:",self.nombre)
        print("Capacidad:",self.capacidad)
        print("Locacion:",self.locacion)
        print("Restaurante:",self.restaurantes)
    
    def get_stadium_id(self):
        return self.id
    
    def get_nombre_estadio(self):
        return self.nombre
    
    def get_capacidad(self):
        return self.capacidad

#Metodo para mostrar de forma enumerada los Restaurantes de cada Estadio    
    def mostrar_restaurantes(self):
        for i in range(len(self.restaurantes)):
            nombre=Restaurante.get_nombre(self.restaurantes[i])
            print(f"{i+1}-{nombre}")

#A partir de la Clase Restaurante, se crea este metodo para poder mostrar el menu de los Restaurantes de cada Estadio   
    def mostrar_menu(self,id):
        restaurante=self.restaurantes[id-1]
        Restaurante.mostrar_menu(restaurante)
    
    def get_restaurante_por_id(self,id):
        #print(self.restaurantes)
        return self.restaurantes[id-1]