from laberinto import Laberinto, Habitacion, Pared, Puerta, ParedBomba, Bomba, Norte, Este, Sur, Oeste
from bicho import Bicho, Modo, Agresivo, Perezoso
from threadManager import ThreadManager
import time

class Juego:
    def __init__(self):
        self.laberinto = None
        self.bichos = []
        self.threadManager = ThreadManager()
    
    def launchThreds(self):
        for beast in self.beasts:
            self.threadManager.addThread(beast)
        self.threadManager.start()

    def stopThreds(self):
        self.threadManager.stop()
        self.threadManager.join()

    def crearPared(self):
        return Pared()
    
    def crearPuerta(self, habitacion1, habitacion2):
        puerta = Puerta(habitacion1, habitacion2)
        return puerta

    def crearHabitacion(self, id):
        habitacion = Habitacion(id)
        habitacion.agregarOrientacion(self.crearNorte())
        habitacion.agregarOrientacion(self.crearEste())
        habitacion.agregarOrientacion(self.crearSur())
        habitacion.agregarOrientacion(self.crearOeste())
        habitacion.norte = self.crearPared()
        habitacion.este = self.crearPared()
        habitacion.sur = self.crearPared()
        habitacion.oeste = self.crearPared()
        return habitacion
    
    def crearNorte(self):
        return Norte().get_instance()

    def crearSur(self):
        return Sur.get_instance()
    
    def crearEste(self):
        return Este().get_instance()
    
    def crearOeste(self):
        return Oeste().get_instance()

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
    
    def fabricarLaberinto4Habitaciones4BichosFM(self):
        habitacion1 = self.crearHabitacion(1)
        habitacion2 = self.crearHabitacion(2)
        habitacion3 = self.crearHabitacion(3)
        habitacion4 = self.crearHabitacion(4)
        
        puerta12 = self.crearPuerta(habitacion1, habitacion2)
        puerta13 = self.crearPuerta(habitacion1, habitacion3)
        puerta24 = self.crearPuerta(habitacion2, habitacion4)
        puerta34 = self.crearPuerta(habitacion3, habitacion4)
        
        habitacion1.sur = puerta12
        habitacion2.norte = puerta12
        
        habitacion1.este = puerta13
        habitacion3.oeste = puerta13
        
        habitacion2.este = puerta24
        habitacion4.oeste = puerta24
        
        habitacion3.sur = puerta34
        habitacion4.norte = puerta34
        
        laberinto = Laberinto()
                
        laberinto.agregarHabitacion(habitacion1)
        laberinto.agregarHabitacion(habitacion2)
        laberinto.agregarHabitacion(habitacion3)
        laberinto.agregarHabitacion(habitacion4)
        self.laberinto = laberinto

        bestia1 = self.crearBestiaAgresiva(habitacion1)
        bestia2 = self.crearBestiaPerezosa(habitacion2)  
        bestia3 = self.crearBestiaAgresiva(habitacion3)
        bestia4 = self.crearBestiaPerezosa(habitacion4)
    
        self.agregarBestia(bestia1)
        self.agregarBestia(bestia2)
        self.agregarBestia(bestia3)
        self.agregarBestia(bestia4)

        return laberinto

    
    def agregarBicho(self, bicho):
        bicho.num=len(self.bichos)+1
        self.bichos.append(bicho)

    def eliminarBicho(self, bicho):
        self.bichos.remove(bicho)
    
    def crearBichoAgresivo(self,habitacion):
        bicho = Bicho(Agresivo())
        bicho.poder = 5
        bicho.posicion=habitacion
        return bicho
    
    def crearBichoPerezoso(self,habitacion):
        bicho = Bicho(Perezoso())
        bicho.poder = 1
        bicho.posicion=habitacion
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
