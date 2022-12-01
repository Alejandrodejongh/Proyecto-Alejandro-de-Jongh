from Producto import Producto,Comida,Bebida
from Persona import Persona


class Restaurante:
    def __init__(self,nombre,productos):
        self.nombre=nombre 
        self.productos= []
        self.crear_productos(productos)
    
    def get_nombre(self):
        return self.nombre

#Cada Restaurante tiene productos, por lo que se utiliza la Clase Producto y sus hijas para crear Objetos Producto y añadirlos
#a una lista de productos que tiene cada restaurante    
    def crear_productos(self,productos):
        for p in productos:
            if p["type"]=="food":
                alimento=Comida(p["name"],p["quantity"],p["price"],p["type"],p["adicional"])
            elif p["type"]=="beverages":
                alimento= Bebida(p["name"],p["quantity"],p["price"],p["type"],p["adicional"])
            
            self.productos.append(alimento)
    
#Metodo para mostrar los atributos de cada producto    
    def mostrar_menu(self):
        for producto in self.productos:
            producto.mostrar_producto()

#Las proximas tres funciones se utilizan para el filtro que el usuario puede hacer de los productos del restaurante.
#Se comprueba si el valor que da el usuario coincide con los atributos de los Objeto Producto asociados a esos Restaurantes.

    def mostrar_por_nombre(self,nombre):
        for producto in self.productos:
            if nombre==Producto.get_nombre(producto):
                producto.mostrar_producto()
    
    def mostrar_por_tipo(self,tipo):
        for producto in self.productos:
            if tipo==Producto.get_tipo(producto):
                producto.mostrar_producto()
    
    def mostrar_por_precio(self,inicio,final):
        for producto in self.productos:
            if Producto.get_precio(producto) in range(inicio,final+1):
                producto.mostrar_producto()



    def get_productos(self):
        return self.productos
    

    def get_producto_por_nombre(self,nombre):
        for producto in self.productos:
            if Producto.get_nombre(producto)==nombre:
                return producto
        return None

#Metodo de Numeros Perfectos para calcular el descuento en la factura de restaurante
    def perfectos(self,persona):
        cedula=Persona.get_cedula(persona)
        divisores=[]
        for i in range(1,cedula):
            if cedula%i==0:
                divisores.append(i)
        if sum(divisores)==cedula:
            return True
        return False

    

    def descuento_restaurante(self,persona,subtotal):
        discount=0
        if self.perfectos(persona):
            discount+=subtotal*0.15
        total=subtotal-discount
        return total,discount

#Factura del Restaurante    
    def factura_restaurante(self,persona,lista_productos):
        print("***FACTURA***")
        print("NOMBRE:",Persona.get_nombre(persona))
        print("CEDULA:",Persona.get_cedula(persona))
        subtotal=0
         #Se accede a lista de diccionarios de productos que compro el cliente, que tiene la forma
            #{"producto":nombre_producto,"cantidad":int(cantidad de producto comprada)}
            #A partir del nombre se puede acceder al precio del Objeto producto y calcular la cantidad a pagar
            #por cada cosa
        for d in lista_productos:
            nombre=Producto.get_nombre(d["producto"])
            cantidad=d["cantidad"]
            precio=Producto.get_precio(d["producto"])
            print(f"{nombre} x {cantidad} = {(precio*cantidad)}$")
            subtotal+=precio*cantidad

        total,discount=self.descuento_restaurante(persona,subtotal)
        print("SUBTOTAL:",subtotal,"$")
        print("DESCUENTO:",discount,"$")
        print("TOTAL:",total,"$")
        print("")

#Metodo para mostrar el inventario del Restaurante
    def mostrar_inventario(self):
        for p in self.productos:
            print(f"{Producto.get_nombre(p)}-{Producto.get_inventario(p)}")
