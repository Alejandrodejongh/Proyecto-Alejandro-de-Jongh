from Estadio import Estadio
from Equipo import Equipo


class Partido:
    def __init__(self,local,visitante,fecha,estadio,id):
        self.equipo_local=local
        self.equipo_visitante=visitante
        self.fecha=fecha 
        self.id_stadio=estadio
        self.id_partido=id
        self.mapa=[]
        self.generar_mapa()
        self.codigos=[]
        self.asistencia=0
    

    
    def get_local(self):
        return self.equipo_local
    
    def get_visitante(self):
        return self.equipo_visitante
    
    def get_estadio(self):
        return self.id_stadio
    
    def get_fecha(self):
        return self.fecha
    
    def get_id_partido(self):
        return self.id_partido
    
    def get_codigos(self):
        return self.codigos
    
    def get_asistencia(self):
        return self.asistencia
    

    
    def mostrar_partido(self):
        local=  Partido.get_local(self)
        visitante= Partido.get_visitante(self)
        equipo_local=Equipo.get_id(local)
        estadio= Partido.get_estadio(self)
        id_stadio=Estadio.get_stadium_id(estadio)
        mostrar_local= Equipo.get_nombre(local)
        mostrar_visitante= Equipo.get_nombre(visitante)
        mostrar_fecha= Partido.get_fecha(self)
        mostrar_estadio= Estadio.get_nombre_estadio(estadio)
        mostrar_id=Partido.get_id_partido(self)
        boletos_vendidos= len(self.codigos)
        relacion_asistencia_venta=0
        if boletos_vendidos !=0:
            relacion_asistencia_venta=(self.asistencia/boletos_vendidos)*100

        print("ID Partido:",self.id_partido)
        print(f"{mostrar_local} vs {mostrar_visitante}")
        print("Fecha:",mostrar_fecha)
        print("Estadio:",mostrar_estadio)
        print("Id Partido:",self.id_partido)
        print("Asistencia:",self.asistencia)
        print("Boletos vendidos:",boletos_vendidos)
        print("Relacion Venta/Asistencia:",relacion_asistencia_venta,"%")
    


#Para generar los mapas de cada partido, se utiliza la clase Estadio para obtener la capacidad del mismo. Luego
#gracias a la funcion ord(), que recibe un caracter y devuelve un numero, es posible generar las matrices y mostrar de forma
#ordenada los puestos para que el usuario los escoja.   
    def generar_mapa(self):
        capacidad=Estadio.get_capacidad(self.get_estadio())
        capacidad_fila=capacidad[0]
        capacidad_columna=capacidad[1]
        for i in range(capacidad_fila):
            self.mapa.append([])
            for j in range(ord("A"),ord("A")+capacidad_columna):
                self.mapa[i].append(str(i+1)+chr(j))

#Metodo para mostrar el mapa de forma ordenada y limpia   
    def mostrar_mapa(self):
        for fila in self.mapa:
            str_fila=""
            for asiento in fila:
                str_fila+="|"+ asiento + "|"
            print(str_fila)

  
    
#Metodo que es llamado en el main para reservar/comprar asientos. Se pide al usuario una fila y columna.
#Este mismo metodo crea el codigo de la entrada, que tiene la forma id_partido/asiento
    def reservar_asiento(self):
        fila= int(input("Ingrese la fila que quiere (numero): "))
        columna= ord(input("Ingrese la columna que quiere (letra): ").upper())
        self.mapa[fila-1][columna-65]="x"
        codigo=self.id_partido+"/"+str(fila)+chr(columna)
        self.codigos.append(codigo)
        return codigo


#Metodo llamado en el main para confirmar la asistencia a los partidos, se recibe un codigo por el usuario. 
#Se chequea si dicho codigo fue creado y se encuentra en la lista asociada al atributo self.codigos
#En caso de encontrar el codigo, se suma 1 a la asistencia del partido y se remueve el codigo de la lista    
    def confirmar_asistencia(self,codigo):
        encontrado=False
        for i in self.codigos:
            if i==codigo:
                encontrado=True
                break
        if encontrado:
            self.codigos.remove(codigo)
            self.asistencia+=1
            print("CODIGO VALIDO")
            print(f"Se ha actualizado la asistencia para el partido {self.id_partido}: {Equipo.get_nombre(Partido.get_local(self))} vs {Equipo.get_nombre(Partido.get_visitante(self))}")
            print("")
        else:
            print("CODIGO INVALIDO, es posible que el mismo no exista o ya haya sido utilizado")
            print("")
    

