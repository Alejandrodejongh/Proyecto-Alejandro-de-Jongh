class Persona:
    def __init__(self,nombre,cedula,edad):
        self.nombre=nombre 
        self.cedula=int(cedula)
        self.edad=int(edad)
        self.codigos=[]
        self.vips={}
        self.compras=[]
    
    def mostrar_persona(self):
        print("NOMBRE:",self.nombre)
        print("CEDULA:",self.cedula)
        print("EDAD:",self.edad)
        print("CODIGOS COMPRADOS:",self.codigos)
        print("CANTIDAD COMPRADA:",len(self.codigos))
        print("")

#Metodo llamado en el main para agregar las compras hechas por el usuario al Objeto Persona    
    def agregar_compras(self,compra):
        self.compras.append(compra)

#Metodo utilizado en el main para agregar el codigo y tipo de entrada comprada al objeto Persona   
    def agregar_entradas(self,codigo,vip):
        self.codigos.append(codigo)
        self.vips[codigo]=vip
    
    def get_cedula(self):
        return self.cedula

#Metodo utilizado en el main para revisar si el usuario puede acceder al restaurante, a traves de un codigo 
#introducido por el mismo. Se revisa si el tipo de entrada es VIP.   
    def revisar_vip(self,code):
        return self.vips[code]
    
    def get_nombre(self):
        return self.nombre
    
    def get_codigos(self):
        return self.codigos