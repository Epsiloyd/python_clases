#Programacion orientada a objetos (poo o opp)
#Definir una clase (molde para crear mas objetos de ese tipo)
#(Coche)Con caracteristicas similares

class Coche:

#Atributos o propiedades (variables)
#Caracteristicas del coche

    color = "Rojo"
    marca = "Ferrari"
    modelo = "Aventador"
    velocidad = 300
    caballaje = 500
    plazas = 2

    soy_publico = "Hola, Soy un atributo publico"
    __soy__Privado = "Hola, Soy un atributo privado"
#Consructor
    def __init__(self,color, marca, modelo, velocidad, caballaje, plazas):
         self.color = color
         self.marca = marca
         self.modelo = modelo
         self.velocidad = velocidad
         self.caballaje = caballaje
         self.plazas = plazas


#Metodos, son acciones que hace el objeto (coche) (funciones)
    def getPrivado(self):
          return self.__soy__Privado

    def setColor(self,color):
        self.color = color
    
    def getColor(self):
            return self.color
    
    def setModelo(self,modelo):
        self.modelo = modelo

    def getModelo(self):
            return self.modelo
    
    def getMarca(self,marca):
         self.marca = marca

    def getMarca(self):
            return self.marca
         
    def acelerar(self):
        self.velocidad += 1

    def frenar(self):
        self.velocidad -= 1

    def getVelocidad(self):
            return self.velocidad
      
    def getInfo(self):

        info = "_____Informacion del Coche____"  

        info += "\n Color: " + self.getColor()
        info += "\n Marca: " + self.getMarca()
        info += "\n Modelo: " + self.getModelo() 
        info += "\n Velocidad: " + str (self.getVelocidad())

        return info

