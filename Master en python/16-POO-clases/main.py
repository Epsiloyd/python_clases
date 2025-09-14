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

#Metodos, son acciones que hace el objeto (coche) (funciones)
    def setColor(self,color):
        self.color = color
    
    def getColor(self):
        return self.color
    
    def setModelo(self,modelo):
        self.modelo = modelo

    def getModelo(self):
            return self.modelo

    def acelerar(self):
        self.velocidad += 1

    def frenar(self):
        self.velocidad -= 1

    def getVelocidad(self):
        return self.velocidad    

#Fin definicin clase

#Crear un objeto / instaciar la clase

coche =  Coche()
print("Coche #1")

coche.setColor("Amarillo")
coche.setModelo("Murcielago")

print(coche.marca,coche.getColor(),coche.getModelo())
print("Velocidad actual: ", coche.getVelocidad())

coche.acelerar()
coche.acelerar()
coche.acelerar()
coche.acelerar()
coche.frenar()

print("Velocidad nueva: ", coche.getVelocidad())

print("\n##################################################")

#Crear mas objetos

coche2 = Coche()

coche2.setColor("Verde")
coche2.setModelo("Gallardo")

print("\nCoche #2")

print(coche2.marca,coche2.getColor(),coche2.getModelo())
print(type(coche2))