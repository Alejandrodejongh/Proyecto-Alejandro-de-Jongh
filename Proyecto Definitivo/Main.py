import requests
from Equipo import Equipo
from Estadio import Estadio
from Partido import Partido
from Persona import Persona
from Restaurante import Restaurante
from Producto import Producto,Comida,Bebida


#Estas primeras tres funciones permiten extraer toda la informacion necesaria de la API. Equipos, Estadios y Partidos.
#A partir de estos datos se crearon Objetos Equipo,Estadio y Partido, y se añadieron respectivamente a listas que se utilizaron en todo el código.

def info_api_equipos():
    lista_equipos=[]
    url_equipos= "https://raw.githubusercontent.com/Algoritmos-y-Programacion-2223-1/api-proyecto/main/teams.json"
    t=requests.get(url_equipos)
    equipos=t.json()
    
    for e in equipos:
            equipo= Equipo(e["name"],e["flag"],e["fifa_code"],e["group"],e["id"])
            lista_equipos.append(equipo)
    return lista_equipos

def info_api_estadios():
    lista_estadios=[]
    url_estadios="https://raw.githubusercontent.com/Algoritmos-y-Programacion-2223-1/api-proyecto/main/stadiums.json"
    m=requests.get(url_estadios)
    estadios=m.json()
    
    for es in estadios:
        estadio=Estadio(es["id"],es["name"],es["capacity"],es["location"],es["restaurants"])
        lista_estadios.append(estadio)
    return lista_estadios

#Para la creación de Partidos, los atributos correspondientes a self.equipo_local y self.equipo_visitante son Objetos Equipo, correspondientes a los equipos que jugarán el encuentro.
#Del mismo modo el atributo self.estadio es un Objeto Estadio

def info_api_partidos(equipos,estadios):
    lista_partidos=[]
    url_partidos= "https://raw.githubusercontent.com/Algoritmos-y-Programacion-2223-1/api-proyecto/main/matches.json"
    r= requests.get(url_partidos)
    partidos= r.json()
   
    for p in partidos:
        for e in equipos:
            if Equipo.get_nombre(e)==p["home_team"]:
                local=e
            elif Equipo.get_nombre(e)==p["away_team"]:
                visitante=e
        for es in estadios:
            if Estadio.get_stadium_id(es)==p["stadium_id"]:
                estadio=es
        partido= Partido(local,visitante,p["date"],estadio,p["id"])
        lista_partidos.append(partido)
    return lista_partidos


#Esta función corresponde al primer módulo del proyecto. 
#Es un filtro que permite buscar partidos por País, Estadio o Fecha.

def filtro_partidos(partidos):
    filtro= input("Seleccione un filtro:\n1-Pais\n2-Estadio\n3-Fecha\n-> ")
    while not filtro.isnumeric() or int(filtro) not in range(1,4):
        filtro= input("ERROR, ingrese una opcion valida: ")
        print("")
    else:
        if filtro=="1":
            print("")
            print("1-Qatar\n2-Ecuador\n3-Senegal\n4-Netherlands\n5-England\n6-Iran\n7-United States\n8-Wales\n9-Argentina\n10-Saudi Arabia\n11-Denmark\n12-Tunisia\n13-Mexico\n14-Poland\n15-France\n16-Australia\n17-Morocco\n18-Croatia\n19-Germany\n20-Japan\n21-Spain\n22-Costa Rica\n23-Belgium\n24-Canada\n25-Brazil\n26-Serbia\n27-Portugal\n28-Ghana\n29-Uruguay\n30-South Korea\n31-Switzerland\n32-Cameroon")
            print("")
            pais= int(input("Ingrese el id del pais que quiere buscar: "))
            print("")
            while pais not in range(1,33):
                pais=int(input("ERROR, ingrese un id valido: "))
                print("")
            else:
                if pais>=1 and pais<=32:
                    for partido in partidos:
            #A modo de poder mostrar los partidos de manera adecuado (tomando en cuenta que algunos de los atributos de Partido son Objetos)
            #fue necesario llamar a los distintos metodos get de los Objetos 

                        local=  Partido.get_local(partido)
                        visitante= Partido.get_visitante(partido)
                        equipo_local=Equipo.get_id(local)
                        equipo_visitante= Equipo.get_id(visitante)
                        mostrar_local= Equipo.get_nombre(local)
                        mostrar_visitante= Equipo.get_nombre(visitante)
                        mostrar_fecha= Partido.get_fecha(partido)
                        estadio= Partido.get_estadio(partido)
                        mostrar_estadio= Estadio.get_nombre_estadio(estadio)
                        mostrar_id=Partido.get_id_partido(partido)

                        if pais==int(equipo_local) or pais==int(equipo_visitante):
                            print(f"{mostrar_local} vs {mostrar_visitante}")
                            print("Fecha:",mostrar_fecha)
                            print("Estadio:",mostrar_estadio)
                            print("Id Partido:",mostrar_id)
                            print("")
        
#Filtro para buscar partidos usando el id del estadio
        
        elif filtro=="2":
            print("")
            print("ESTADIOS QATAR 2022")
            print("1-Al Bayt Stadium\n2-Lusail Stadium\n3-Ahmad Bin Ali Stadium\n4-Al Janoub Stadium\n5-Al Thumama Stadium\n6-Education City Stadium\n7-Khalifa International Stadium\n8-Stadium 974")
            print("")
            id_estadio= input("Ingrese el id del estadio: ")
            print("")
            while not id_estadio.isnumeric() and int(id_estadio) not in range(1,8):
                id_estadio= input("ERROR, ingrese un id valido: ")
            else:
                id_estadio=int(id_estadio)
                for partido in partidos:
                    local=  Partido.get_local(partido)
                    visitante= Partido.get_visitante(partido)
                    equipo_local=Equipo.get_id(local)
                    estadio= Partido.get_estadio(partido)
                    id_stadio=Estadio.get_stadium_id(estadio)
                    mostrar_local= Equipo.get_nombre(local)
                    mostrar_visitante= Equipo.get_nombre(visitante)
                    mostrar_fecha= Partido.get_fecha(partido)
                    mostrar_estadio= Estadio.get_nombre_estadio(estadio)
                    mostrar_id=Partido.get_id_partido(partido)
                    
                    if id_estadio==id_stadio:
                        print(mostrar_estadio)
                        print(f"{mostrar_local} vs {mostrar_visitante}")
                        print("Fecha:",mostrar_fecha)
                        print("Id Partido:",mostrar_id)
                        print("")

#Filtro para buscar partidos a partir de una fecha dada por el usuario
       
        elif filtro=="3":
            fecha=input("Ingrese la fecha deseada en formato m/d/yyyy: ")
            print("")
            while not len(fecha)<=10:
                fecha=input("ERROR, ingrese una fecha valida:")
            else:
                for partido in partidos:
                    local=  Partido.get_local(partido)
                    visitante= Partido.get_visitante(partido)
                    equipo_local=Equipo.get_id(local)
                    estadio= Partido.get_estadio(partido)
                    id_stadio=Estadio.get_stadium_id(estadio)
                    mostrar_local= Equipo.get_nombre(local)
                    mostrar_visitante= Equipo.get_nombre(visitante)
                    mostrar_fecha= Partido.get_fecha(partido)
                    mostrar_estadio= Estadio.get_nombre_estadio(estadio)
                    mostrar_id=Partido.get_id_partido(partido)

                    if fecha in Partido.get_fecha(partido):
                        print(f"{mostrar_local} vs {mostrar_visitante}")
                        print("Fecha:",mostrar_fecha)
                        print("Estadio:",mostrar_estadio)
                        print("Id Partido:",mostrar_id)
                        print("")

#Esta función permite retornar una Persona tomando como dato su número de cédula, para así comprobar 
#si ya compró entradas

def buscar_persona_cedula(lista_personas,cedula):
    for persona in lista_personas:
        if cedula==Persona.get_cedula(persona):
            return persona
    return None

#Estas proximas tres funciones hacen referencia al descuento, la factura y el proceso de compra que se ejecuta 
#siempre que el usuario decida adquirir una entrada

def descuento(cedula,entrada):
    divisores=[]
    discount=0
    for i in range(1,cedula):
        if cedula%i==0:
            divisores.append(i)
    if sum(divisores)==cedula:
        discount+=entrada*0.50
        precio_def=entrada-discount
        return precio_def,discount
    else:
        return entrada,0


def factura_partido(partido,persona,entrada,precio_entrada,discount,precio_def,codigo):
    print("")
    print("***FACTURA****")
    print("")
    print("NOMBRE:",Persona.get_nombre(persona))
    print("CEDULA:",Persona.get_cedula(persona))
    print("PARTIDO:",Equipo.get_nombre(Partido.get_local(partido)),"vs",Equipo.get_nombre(Partido.get_visitante(partido)))
    print("PRECIO ENTRADA:",entrada,"$")
    print("DESCUENTO:",discount,"$")
    print("PRECIO CON DESCUENTO:",precio_entrada,"$")
    print("PRECIO A CANCELAR (INCLUYE IVA): ",round(precio_def,1),"$")
    print("CODIGO:",codigo)




def comprar_entradas(partidos,personas):
    print("")
    cedula=int(input("Ingrese su cedula de identidad: "))
#Se pide primero la cedula y se utiliza la misma para comprobar si esta en el sistema. 
#En caso de no estar, se proceden a pedir los demas datos. Si esta, quiere decir que el usuario ya compro
#anteriormente, por lo que no se piden los datos y la entrada se guarda en el Objeto Persona
    persona=buscar_persona_cedula(personas,cedula)
    if persona==None:

#Datos del cliente
        nombre=input("Ingrese su nombre: ")
        edad= int(input("Ingrese su edad: "))
        persona= Persona(nombre,cedula,edad)
        personas.append(persona)

#Escoger Equipo por Id
    print("")
    print("1-Qatar\n2-Ecuador\n3-Senegal\n4-Netherlands\n5-England\n6-Iran\n7-United States\n8-Wales\n9-Argentina\n10-Saudi Arabia\n11-Denmark\n12-Tunisia\n13-Mexico\n14-Poland\n15-France\n16-Australia\n17-Morocco\n18-Croatia\n19-Germany\n20-Japan\n21-Spain\n22-Costa Rica\n23-Belgium\n24-Canada\n25-Brazil\n26-Serbia\n27-Portugal\n28-Ghana\n29-Uruguay\n30-South Korea\n31-Switzerland\n32-Cameroon")
    print("")
    id_equipo= int(input("Ingrese el id del equipo que quiere ver: "))
    
    for partido in partidos:
        local=  Partido.get_local(partido)
        visitante= Partido.get_visitante(partido)
        equipo_local=Equipo.get_id(local)
        equipo_visitante= Equipo.get_id(visitante)
        mostrar_local= Equipo.get_nombre(local)
        mostrar_visitante= Equipo.get_nombre(visitante)
        mostrar_fecha= Partido.get_fecha(partido)
        estadio= Partido.get_estadio(partido)
        id_stadio=Estadio.get_stadium_id(estadio)
        mostrar_estadio= Estadio.get_nombre_estadio(estadio)
        mostrar_id=Partido.get_id_partido(partido)

        if id_equipo==int(equipo_local) or id_equipo==int(equipo_visitante):
            print(f"{mostrar_local} vs {mostrar_visitante}")
            print("Fecha:",mostrar_fecha)
            print("Estadio:",mostrar_estadio)
            print("Id Partido:",mostrar_id)
            print("")
    
    print("")
    id_partido= int(input("Ingrese el id del partido que desea ver: "))
    print("")
    entrada=0

#Seleccion de partido y Tipo de Entrada
    for partido in partidos:
        if id_partido==int(Partido.get_id_partido(partido)):
            tipo_entrada= int(input("Que tipo de entrada quiere comprar: \n1-General\n2-VIP\n-> "))
            if tipo_entrada==1:
                entrada=50
            elif tipo_entrada==2:
                entrada=120

#Mapa, Facturacion                
            Partido.mostrar_mapa(partido)
            print("")
            codigo=Partido.reservar_asiento(partido)
            precio_con_descuento,discount=descuento(cedula,entrada)
            precio_con_iva=precio_con_descuento*1.16
            factura_partido(partido,persona,entrada,precio_con_descuento,discount,precio_con_iva,codigo)
            print("")
            confirmar_compra= int(input("Desea confirmar su compra: \n1-Si\n2-No\n-> "))
            
            if confirmar_compra==1:
                #Se agrega el codigo generado y el tipo de entrada adquirido al Objeto Persona y al Objeto Partido
                Persona.agregar_entradas(persona,codigo,tipo_entrada==2)

                print("")
                print("FELICIDADES, SU COMPRA HA SIDO REGISTRADA")
            
            elif confirmar_compra==2:
                continue

#Funcion que permite filtrar los productos de un restaurante segun su nombre, tipo o precio.
#Se hace uso de metodos de la Clase Restaurante
def filtro_restaurante(restaurante):
    filtro=int(input("Que filtro desea usar:\n1-Nombre\n2-Tipo\n3-Precio\n-> "))
    if filtro==1:
        nombre=input("Indique el nombre del alimento: ")
        Restaurante.mostrar_por_nombre(restaurante,nombre)
    elif filtro==2:
        tipo=input("Indique el tipo de alimento que quiere mostrar: \n-Food\n-Beverages\n-> ").lower()
        Restaurante.mostrar_por_tipo(restaurante,tipo)
    elif filtro==3:
        inicio=int(input("Indique el inicio del rango de precio: "))
        final= int(input("Indique el final del rango de precio: "))
        Restaurante.mostrar_por_precio(restaurante,inicio,final)


#Funcion que permite a los clientes VIP comprar productos en el Restaurante asociado al Estadio del Partido
#para el cual compraron entrada
def comprar_productos(restaurante):
    lista_productos_comprados=[]
    while True:
        print("")
        #Se pide nombre del producto y cantidad del mismo
        producto=input("Ingrese el nombre del producto que quiere: ").capitalize()
        objeto_producto=Restaurante.get_producto_por_nombre(restaurante,producto)
        if objeto_producto:
            cantidad=int(input("Ingrese la cantidad del producto: "))
            if cantidad<=Producto.get_inventario(objeto_producto):
                #Se añade al producto (cantidad,Objeto) como diccionario a una lista de productos comprados
                lista_productos_comprados.append({"cantidad":cantidad,"producto":objeto_producto})
                #Se actualiza el inventario, restando la cantidad que pidio el cliente
                Producto.actualizar_inventario(objeto_producto,cantidad)
        else:
            print("PRODUCTO NO ENCONTRADO")

        #Si el usuario decide comprar más el bucle sigue, de lo contrario se retorna la lista de productos comprados
        continuar= int(input("Desea continuar comprando: \n1-Si\n2-No\n-> "))
        if continuar==1:
            print("")
            continue
        elif continuar==2:
                return lista_productos_comprados


def estadisticas(partidos,personas):
    opcion=int(input("Que estadistica desea ver:\n1-General Partidos\n2-Mayor Asistencia \n3-Mas Boletos Vendidos\n4-Promedio de Gasto VIP\n5-Productos mas vendidos\n6-Top 3 Clientes\n-> "))
    if opcion==1:
        for partido in partidos:
            Partido.mostrar_partido(partido)
            print("")
    
    elif opcion==2:
        max_asistencia=0
        for partido in partidos:
            print(Partido.get_asistencia(partido))
            #if asistencia>max_asistencia:
                #max_asistencia=partido
        #print("EL PARTIDO CON MAYOR ASISTENCIA FUE: ")
        #Partido.mostrar_partido(partido)
    
    elif opcion==3:
        max_boletos=0
        for partido in partidos:
            codigos=Partido.get_codigos(partido)
            if len(codigos)>max_boletos:
                max_boletos=partido
        print("EL PARTIDO CON MAYOR VENTA DE BOLETOS FUE: ")
        Partido.mostrar_partido(partido)
    
    elif opcion==4:
        pass

    elif opcion==5:
        pass
    
    elif opcion==6:
        cliente_max_boletos=0
        for persona in personas:
            boletos_comprados=Persona.get_codigos(persona)
            if len(boletos_comprados)>cliente_max_boletos:
                cliente_max_boletos=persona
        Persona.mostrar_persona(persona)

            







def main():
#Llamada de Funciones Iniciales para tomar los datos de la API
    lista_personas=[]
    lista_equipos=info_api_equipos()
    lista_estadios=info_api_estadios()
    lista_partidos= info_api_partidos(lista_equipos,lista_estadios)

#Menu Principal
    while True:
        print("")
        print("*** BIENVENIDOS AL MUNDIAL QATAR 2022***")
        print("")
        opcion= int(input("Que desea hacer:\n1-Buscar Partidos\n2-Comprar Entradas\n3-Gestion Asistencia\n4-Gestion Restaurantes\n5-Comprar en Restaurante\n6-Estadisticas\n-> "))
        
        if opcion==1:
#Filtro de Partidos
            print("")
            filtro_partidos(lista_partidos)
        

        elif opcion==2:
#Comprar Entradas
            comprar_entradas(lista_partidos,lista_personas)
        

        elif opcion==3:
#Gestion de Asistencia
            print("")
#Se pide al usuario el codigo que quiere validar
            codigo= input("Ingrese el codigo a validar idpartido/asiento: ")
            id_partido=int(codigo.split("/")[0])
            
            for partido in lista_partidos:
                if id_partido==int(Partido.get_id_partido(partido)):
                    #Se llama al metodo confirmar asistencia de la Clase Partido para realizar la operacion
                    Partido.confirmar_asistencia(partido,codigo)
                    break


        

        elif opcion==4:
#Se muestran los Estadios por Id
            print("")
            print("ESTADIOS QATAR 2022")
            print("1-Al Bayt Stadium\n2-Lusail Stadium\n3-Ahmad Bin Ali Stadium\n4-Al Janoub Stadium\n5-Al Thumama Stadium\n6-Education City Stadium\n7-Khalifa International Stadium\n8-Stadium 974")
            print("")
            id_estadio= int(input("Ingrese el id del estadio: "))
            print("")

            for estadio in lista_estadios:
                if id_estadio== Estadio.get_stadium_id(estadio):
#El usuario escoge que Restaurante de dicho Estadio quiere ver
                    Estadio.mostrar_restaurantes(estadio)
                    restaurante=int(input("Ingrese el numero del restaurante que quiere: "))
                    print("")
#Se muestra el menu y se procede a filtrar los resultados si asi lo quiere el usuario
                    Estadio.mostrar_menu(estadio,restaurante)
                    #objeto_restaurante=Estadio.get_restaurante_por_id(estadio,restaurante)
                    filtro_restaurante(estadio)
                

        
        elif opcion==5:
#Compra en Restaurantes para Aficionados VIP
#Se pide la cedula para acceder a la Persona y el codigo de la entrada
            cedula= int(input("Ingrese su cedula: "))
            code= input("Ingrese el codigo de su entrada: ")
            print("")
            persona=buscar_persona_cedula(lista_personas,cedula)
            if persona !=None:
#Se revisa si el codigo que ingreso el usuario corresponde a una entrada VIP, llamando a dicho metodo de la
#Clase Persona
                if Persona.revisar_vip(persona,code):
                    id_partido=int(code.split("/")[0])
                    for partido in lista_partidos:
#Si el codigo efectivamente es VIP, se muestran los restaurantes asociados al Estadio donde se juega el partido
#para el cual el cliente VIP compro entrada
                        if id_partido== int(Partido.get_id_partido(partido)):
                            estadio= Partido.get_estadio(partido)
                            Estadio.mostrar_restaurantes(estadio)
                            restaurante=int(input("Ingrese el numero del restaurante que quiere: "))
                            Estadio.mostrar_menu(estadio,restaurante)
                            objeto_restaurante=Estadio.get_restaurante_por_id(estadio,restaurante)
#El usuario escoge el restaurante, compra sus productos y se le muestra la respectiva factura
                            productos_comprados=comprar_productos(objeto_restaurante)
                            Persona.agregar_compras(persona,productos_comprados)
                            print("")
                            Restaurante.factura_restaurante(objeto_restaurante,persona,productos_comprados)
                            break
                            
                else:
                    print("ERROR, el codigo introducido no es VIP")
        

        elif opcion==6:
#Estadisticas
            estadisticas(lista_partidos,lista_personas)
                        





                
main()