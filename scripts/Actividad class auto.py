class auto:
    color = ""
    marca = ""
    modelo = ""
    velocidad = 0
    transmicion = ""
    marcha = 0
    encendido= False
    def emcender (self):
        self.encendido = True
    def apagado (self):
        self.encendido = False
    def avanzar (self):
        pass
    def retroceder (self):
        pass
    def acelerar (self):
        if (self.encendido):
            velocidad = 123 #velocidad propia de la funcion 
            self.velocidad = velocidad + 10 ##sel.velocidad para llamar la velocidad inicializada en class
        else:
            print ("\033[1;1m")
            print ("ATENCIÓN: Primero debe encender el vehiculo")
        pass
    def getVelocidad (self): ##obtener valor de una class
        return self.velocidad
    def detener (self):
        pass
    def Estado ():
        print ("Encendido: ", self.encendido)
autito = auto ()
def Menú ():
    ##print (chr(27)+"[2J") ##CÓDIGO ANSI
    print ("\033[2J")
    print ("\033[1m")
    print ("\033[1;2;7m")
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
        autito = auto.encendido ()
        print("Encender vehiculo")
        print("Estado: Encendido. Velocidad actual: 0, Marcha: N")
    elif opcion == 2:
        autito = auto.acelerar ()
        print("Acelerar vehiculo")
        print("Estado: Encendido. Velocidad actual: ,Marcha: N")
    elif opcion == 3:
        autito = auto.avanzar ()
        print("Avanzar vehiculo")
        print("Estado: Encendido. Velocidad actual: 0, Marcha: N")
    elif opcion == 4:
        autito = auto.retroceder ()
        print("Retroceder vehiculo")
        print("Estado: Encendido. Velocidad actual: 0, Marcha: N")
    elif opcion == 5:
        print("Detener vehiculo")
        autito = auto.detener ()
        print("Estado: Detenido. Velocidad actual: 0, Marcha: N")
    elif opcion == 6:
        print("Salir")
    break
