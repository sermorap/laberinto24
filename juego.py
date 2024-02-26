from maze import Laberinto, Habitacion, Pared, Puerta, ParedBomba, Bomba
from bicho import Bicho, Modo, Agresivo, Perezoso

class Juego:
    def __init__(self):
        self.laberinto = None
        self.bichos = []

    def crearPared(self):
        return Pared()
    
    def crearPuerta(self, habitacion1, habitacion2):
        puerta = Puerta(habitacion1, habitacion2)
        return puerta

    def crearHabitacion(self, id):
        habitacion = Habitacion(id)
        habitacion.norte = self.crearPared()
        habitacion.este = self.crearPared()
        habitacion.sur = self.crearPared()
        habitacion.oeste = self.crearPared()
        return habitacion

    def fabricarLaberinto2Habitaciones(self):
        laberinto = Laberinto()
        self.laberinto = laberinto
        habitacion1 = Habitacion(1)
        habitacion2 = Habitacion(2)

        puerta = Puerta(habitacion1, habitacion2)

        habitacion1.sur = puerta
        habitacion2.norte = puerta

        self.laberinto.agregarHabitacion(habitacion1)
        self.laberinto.agregarHabitacion(habitacion2)

    def fabricarLaberinto2HabitacionesFM(self):
        habitacion1 = self.crearHabitacion(1)
        habitacion2 = self.crearHabitacion(2)
        puerta = self.crearPuerta(habitacion1, habitacion2)
        laberinto = Laberinto()
        self.laberinto = laberinto
        self.laberinto.agregarHabitacion(habitacion1)
        self.laberinto.agregarHabitacion(habitacion2)
      
        habitacion1.sur = puerta
        habitacion2.norte = puerta
    
    def agregarBicho(self, bicho):
        self.bichos.append(bicho)

    def eliminarBicho(self, bicho):
        self.bichos.remove(bicho)
    
    def crearBichoAgresivo(self):
        bicho = Bicho(Agresivo())
        bicho.poder = 5
        return bicho
    
    def crearBichoPerezoso(self):
        bicho = Bicho(Perezoso())
        bicho.poder = 1
        return bicho
    
    def imprimir(self):
        print("Juego")

# JuegoBomba.py
class JuegoConBombas(Juego):
    def crearPared(self):
        return ParedBomba()

    def imprimir(self):
        print("Juego con Bombas")

juego = Juego()
juego.fabricarLaberinto2Habitaciones()
juego.laberinto.entrar()

juego = Juego()
juego.fabricarLaberinto2HabitacionesFM()

juego = JuegoConBombas()
juego.fabricarLaberinto2HabitacionesFM()
juego.laberinto.entrar()
