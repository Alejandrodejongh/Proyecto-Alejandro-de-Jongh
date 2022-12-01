class Equipo:
    def __init__(self,nombre,bandera,codigo,grupo,id):
        self.nombre=nombre
        self.bandera=bandera
        self.codigo=codigo
        self.grupo=grupo
        self.id=id
    
    def mostrar(self):
        print("Nombre:",self.nombre)
        print("Bandera:",self.bandera)
        print("Codigo:",self.codigo)
        print("Grupo:",self.grupo)
        print("Id:",self.id)
    
    def get_nombre(self):
        return self.nombre
    
    def get_id(self):
        return self.id
        