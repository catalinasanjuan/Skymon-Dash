class configurations:
    def __init__(self,width, height):
        self.size =(width,height)
        self.color = (255,255,255) ##BLANCO
        self.title = "My First Program"
    size = (800.600)
    def setSize(self,ancho,alto):
        self.size =(ancho,alto)
        self.width = ancho 
        self.height = alto
    def getSize(self):
        return (self.size)
    def setcolor (self,red,green,blue):
        set.color = (red,green,blue)
    def getColor(self):
        return self.getColor
    def  setTitle (self,title):
        self.title= title
    def getTitle (self):
        return self.title
conf = configurations ()
##conf.setSize(1024,786) ##ASIGNO UN TAMAÑO
conf.setcolor (255,0,0) ##CAMBIO A ROJO
conf.setTitle = "Bienvenidos"

from tkinter import *

ventana = tkinter.Tk ()
ventana.mainloop()
