class Producto:
    def __init__(self,nombre,inventario,precio,tipo):
        self.nombre=nombre
        self.inventario=inventario
        self.price=precio + precio*0.16
        self.tipo=tipo
        
    
    def get_nombre(self):
        return self.nombre
    
    def get_inventario(self):
        return self.inventario
    
    def get_precio(self):
        return self.price
    
    def get_tipo(self):
        return self.tipo

#Metodo que recibe la cantidad de un producto que el usuario compro, que se resta del inventario asociado al producto    
    def actualizar_inventario(self,cantidad):
        self.inventario-=cantidad

class Comida(Producto):
    def __init__(self, nombre, inventario, precio, tipo,clasificacion):
        super().__init__(nombre, inventario, precio, tipo)
        self.clasificacion=clasificacion
    
    def mostrar_producto(self):
        print("Nombre:",self.nombre)
        print("Precio:",self.price)
        print("Tipo:",self.tipo)
        print("Clasificacion:",self.clasificacion)
        print("Inventario:",self.inventario)
        print("")


class Bebida(Producto):
    def __init__(self, nombre,inventario, precio, tipo,clasificacion):
        super().__init__(nombre,inventario, precio, tipo)
        self.clasificacion=clasificacion
    
    def mostrar_producto(self):
        print("Nombre:",self.nombre)
        print("Precio:",self.price)
        print("Tipo:",self.tipo)
        print("Clasificacion:",self.clasificacion)
        print("Inventario:",self.inventario)
        print("")
    

    

