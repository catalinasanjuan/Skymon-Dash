##control + F5 = ejecutar
class automvil:
    color = ""
    marca = ""
    modelo = ""
    velocidad = 0
    transmicion = ""
    marcha = 0
    def avanzar (self):
        #        print("avanza")
        pass
    def retroceder (self):
        pass
    def acelerar (self):
        velocidad = 123 #velocidad propia de la funcion 
        self.velocidad = velocidad + 10 ##sel.velocidad para llamar la velocidad inicializada en class
        pass
    def deterner(self):
        pass
    def getVelocidad (self): ##obtener valor de una class
        return self.velocidad
    
autito = automvil () # autito es un objeto
print ("La velocidad del auto es :",  autito.getVelocidad())
autito.acelerar ()
print ("La velocidad del auto es :",  autito.getVelocidad())

## Para encapsular o privatizar 
___marcha = 999
def getMarcha (self):
    return self.___marcha

#ACTIVIDAD: Crea un programa en donde te muestre un Menú:
##1. Encender vehiculo
##2. acelerar vehiculo
##1. avanzar vehiculo
##1. retroceder vehiculo
##1. detener vehiculo
## Por cad accción se debe mostrar el estado del autito
##Ej, presiona 1 el mensaje de salida será , Estado: Encendido. Velocidad actual: 0, Marcha: N

class auto:
    color = ""
    marca = ""
    modelo = ""
    velocidad = 0
    transmicion = ""
    marcha = 0
    def avanzar (self):
        #        print("avanza")
        pass
    def retroceder (self):
        pass
    def acelerar (self):
        velocidad = 123 #velocidad propia de la funcion 
        self.velocidad = velocidad + 10 ##sel.velocidad para llamar la velocidad inicializada en class
        pass
    def deterner(self):
        pass
    def getVelocidad (self): ##obtener valor de una class
        return self.velocidad
    
def Menú ():
    print("1. Encender vehiculo")
    print("2. Acelerar vehiculo")
    print("3. Avanzar vehiculo") 
    print("4. Retroceder vehiculo")
    print("5. Detener vehiculo")
    print("6. Salir")
    print("")
    opcion = int(input("Selecione una opción: "))
    return opcion
while True:
    opcion = Menú()
    if opcion == 1:
        print("1. Encender vehiculo")
        print ("Estado: Encendido. Velocidad actual: 0, Marcha: N")
    elif opcion == 2:
        print("2. Acelerar vehiculo")
        print ("Estado: Encendido. Velocidad actual:"self.velocidad ",Marcha: N")
    elif opcion == 3:
        print("3. Avanzar vehiculo")
        print ("Estado: Encendido. Velocidad actual: 0, Marcha: N")
    elif opcion == 4:
        print("4. Retroceder vehiculo")
        print ("Estado: Encendido. Velocidad actual: 0, Marcha: N")
    elif opcion == 5:
        print("5. Detener vehiculo")
        print ("Estado: Detenido. Velocidad actual: 0, Marcha: N")
    elif opcion == 6:
        print("Salir")
    break
