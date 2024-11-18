#Vehiculo.py

from abc import ABC, abstractmethod
class MedioTransporte(ABC):
    @abstractmethod #Aplico Abstracción
    def __init__(self) -> None:
        print("Se ha creado un medio de transporte")
        self.traccion = "" #Humana, Animal, Mecánica
        self.capacidad = 0 #Cantidad de ocupantes
        self.velocidad = 0
        self.aceleracion = 0.0
        self.vector = {"x" : 0.0, "y": 0.0, "z": 0.0}
        self.energia = "" #Diesel, Calorías, ...
        self.__encapsulado = 0 #Aplico Encapsulamiento
        self.imagen = "test.png"
        self.color = ""
    def getCapacidad(self) -> int:
        return self.capacidad
    def getVector(self) -> dict:
        return self.vector
    def setCapacidad(self, c = 0) -> None: #Aplico Polimorfismo
        self.capacidad = c
    #@abstractmethod
    def subir(self):
        self.vector["z"] = self.vector["z"] + 30
    def bajar(self):
        self.vector["z"] = self.vector["z"] - 30
    def avanzar(self):
        self.vector["x"] = self.vector["x"] + 30
    def retroceder(self):
        self.vector["x"] = self.vector["x"] - 30
    def izquierda(self):
        self.vector["y"] = self.vector["y"] + 30
    def derecha(self):
        self.vector["y"] = self.vector["y"] - 30

   
class Maritimo(MedioTransporte):
    pass

class Aereo(MedioTransporte):
    pass
        
class Terrestre(MedioTransporte):
    pass

class Automovil(Terrestre): #Aplico Herencia
    def __init__(self) -> None:
        super().__init__()
        print("Se ha creado un Automovil")
        self.ruedas = 0

class Avion(Aereo): #Aplico Herencia
    def __init__(self) -> None:
        super().__init__()
        print("Se ha creado un Avión")
        self.ruedas = 0



class Animal(MedioTransporte):
    pass
