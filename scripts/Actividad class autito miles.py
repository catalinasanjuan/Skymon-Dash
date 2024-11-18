class Automovil:
    color = ""
    marca = ""
    modelo = ""
    velocidad = 0
    transmision = ""
    ___marcha = 999
    encendido = False
    def avanzar(self):
        if (self.velocidad>=0):
            self.velocidad -=10
        else:
            print ("\033[1;31m")
            print ("ATENCIÓN: El vehiculo esta detenido")
            print ("\033[0m")
    def frenar (self):
        if ()
    def retroceder(self):
        if (self.velocidad <=0):
            self.velocidad -=10
        else:
            print ("\033[1;31m")
            print ("ATENCIÓN: El vehiculo esta detenido")
            print ("\033[0m")
    def acelerar(self):
        if (self.encendido):
            velocidad = 123 #velocidad propia de la funcion 
            self.velocidad = velocidad + 10 ##sel.velocidad para llamar la velocidad inicializada en class
        else:
            print ("\033[1;31m")
            print ("ATENCIÓN: Primero debe encender el vehiculo")
            print ("\033[0m")
        pass
    def detener(self):
        pass
    def encender(self):
        if(not self.encendido) = True
    def apagar(self):
        self.encendido = False
    def girarllave(self):
        self.encendido = not self.encendido

    def getVelocidad(self):
        return self.velocidad
    def getMarcha(self):
        return self.___marcha
    def getEstado(self):
        print("Encendido: ", self.encendido)
        print("Velocidad: ", self.velocidad)

#Esto es el programa principal
autito = Automovil()
print("La velocidad del auto es: ",autito.getVelocidad())
autito.acelerar()
print("La velocidad del auto es: ",autito.getVelocidad())
print(autito.getMarcha())
## Actividad 1 (15 mins): Crea un programa en donde muestre un menú. ejemplo: 
## 1. Encender Vehículo
## 2. Acelerar Vehículo
## 3. Avanzar
## 4. Retroceder
## 5. Detener
## Por cada acción, se debe mostrar el estado del autito
## ejemplo presiona 1, el mensaje de salida será
## Estado: Encendido.  Velocidad Actual: 0, Marcha: N, etc...
def menu():
    print("\t 1. Para Encender")
    print("\t 2. Acelerar")
    print("\t 3. Avanzar vehiculo") 
    print("\t 4. Retroceder vehiculo")
    print("\t 5. Detener vehiculo")
    print("\t 0. Terminar programa")
    opcion = int(input())
    return opcion

opc = 999
while(opc!=0):
    opc = menu()
    if(opc == 1):
        autito.encender()
    elif(opc == 2):
        autito.acelerar()
    autito.getEstado()
    2