class Juego:
    def __init__(self):
        self.laberinto = None

    def crearPared(self):
        return Pared()
    
    def crearPuerta(self, lado1, lado2):
        puerta = Puerta(lado1, lado2)
        return puerta  
    
    def crearHabitacion(self, id):
        habitacion = Habitacion(id)
        habitacion.norte = self.crearPared()
        habitacion.este = self.crearPared()
        habitacion.sur = self.crearPared()
        habitacion.oeste = self.crearPared()
        return habitacion

    def crearLaberinto(self):
        return Laberinto()
    
    def fabricarLaberinto2HabitacionesFM(self):
        self.laberinto = self.crearLaberinto()
        habitacion1 = self.crearHabitacion(1)
        habitacion2 = self.crearHabitacion(2)
        puerta = self.crearPuerta(habitacion1, habitacion2)
        habitacion1.sur = puerta
        habitacion2.norte = puerta
        self.laberinto.agregarHabitacion(habitacion1)
        self.laberinto.agregarHabitacion(habitacion2)
        return self.laberinto
    
    def fabricarLaberinto2Habitaciones(self):
        self.laberinto = Laberinto()
        habitacion1 = Habitacion(1)
        habitacion2 = Habitacion(2)
        self.laberinto.agregarHabitacion(habitacion1)
        self.laberinto.agregarHabitacion(habitacion2)

        puerta = Puerta(habitacion1, habitacion2)
        habitacion1.sur = puerta
        habitacion2.norte = puerta
        return self.laberinto

class JuegoBomba(Juego):
    def crear_pared(self):
        return ParedBomba()

class ElementoMapa:
    def __init__(self):
        pass
    def entrar(self):
        pass

class Contenedor(ElementoMapa):
    def __init__(self):
        self.hijos = []
        
    def agregarHijo(self, hijo):
        self.hijos.append(hijo)
        
    def eliminarHijo(self, hijo):
        self.hijos.remove(hijo)

class Hoja(ElementoMapa):
    def aceptar(self, visitante):
        visitante.visitarHoja(self)

class Decorator(Hoja):
    def __init__(self, componente):
        self.componente = componente

class Laberinto(Contenedor):
    def __init__(self):
        self.habitaciones = []
    
    def agregarHabitacion(self, habitacion):
        self.habitaciones.append(habitacion)
    
    def entrar(self):
        self.habitaciones[0].entrar()  

class Habitacion(Contenedor):
    def __init__(self, id):
        self.norte = None
        self.este = None
        self.oeste = None
        self.sur = None
        self.id = id
    
    def entrar(self):
        print("Entraste a la habitación", self.id)

class Puerta(ElementoMapa):
    def __init__(self, lado1, lado2):
        self.lado1 = lado1
        self.lado2 = lado2
        self.abierta = False
    def entrar(self):
        if self.abierta:
            self.lado2.entrar()
        else:
            print("La puerta está cerrada")
    
class Pared(ElementoMapa):
    def __init__(self):
        pass
    def entrar(self):
        print("No puedes atravesar paredes")

class ParedBomba(Pared):
    def __init__(self):
        self.activa = False   
    def entrar(self):
        if self.activa:
            print("La bomba ha detonado")
        else:
            return super().entrar()

juego = Juego()
juego.fabricarLaberinto2Habitaciones()
juego.laberinto.entrar()

juego = Juego()
juego.fabricarLaberinto2HabitacionesFM()

juego = JuegoBomba()
juego.fabricarLaberinto2HabitacionesFM()
juego.laberinto.entrar()