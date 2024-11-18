class Automovil:
    color = ""
    marca = ""
    modelo = ""
    velocidad = 0
    transmision = ""
    ___marcha = 999
    encendido = False
    def avanzar(self):
        pass
    def frenar(self):
        if(self.velocidad > 0):
            self.velocidad -= 10
        elif(self.velocidad<0):
            self.velocidad += 10
        elif(self.velocidad == 0):
            print("El vehículo ya está detenido")
    def retroceder(self):
        if(self.velocidad<=0):
            self.velocidad -= 10
        else:
            print("El vehículo está avanzando. Detenga el vehículo primero")
    def acelerar(self):
        if(self.encendido and self.velocidad >=0):
            velocidad = 123 #Esta variable es de la funcion acelerar
            self.velocidad = self.velocidad + 10 # Esta velocidad es de la clase
        else:
            print("\033[1;31m")
            print("ATENCIÓN: Encienda el vehículo primero o verifique que no está retrocediendo")
            print("\033[0m")
    def detener(self):
        self.velocidad = 0
    def encender(self):
        if(not self.encendido):
            self.encendido = True
        else:
            print("El vehículo ya ha sido encendido. No se puede volver a encender")
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
    #2
    # print(chr(27)+"[2J")
    autito.getEstado()
    print("\033[1;2;7m")
    print("*"*30)
    print("|\t 1. Para Encender")
    print("|\t 2. Acelerar")
    print("|\t 3. Frenar")
    print("|\t 4. Detenerse")
    print("|\t 5. Retroceder")
    print("|\t 0. Terminar programa")
    print("*"*30)
    print("\033[0m")
    opcion = int(input())
    return opcion

opc = 999
while(opc!=0):
    opc = menu()
    if(opc == 1):
        autito.encender()
    elif(opc == 2):
        autito.acelerar()
    elif(opc == 3):
        autito.frenar()
    elif(opc == 4):
        autito.detener()
    elif(opc == 5):
        autito.retroceder()
    elif(opc== 0):
        exit()
