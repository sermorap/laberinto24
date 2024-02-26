# mapelement.py
class ElementoMapa:
    def __init__(self):
        pass
    def entrar(self):
        pass

    def print(self):
        print("ElementoMapa")

class Contenedor(ElementoMapa):
    #Composite
    def __init__(self):
        self.hijos = []
        
    def agregarHijo(self, hijo):
        self.hijos.append(hijo)
        
    def eliminarHijo(self, hijo):
        self.hijos.remove(hijo)
    
    def print(self):
        print("Contenedor")

class Laberinto(Contenedor):
    def __init__(self):
        super().__init__()

    def agregarHabitacion(self, habitacion):
        self.hijos.append(habitacion)

    def entrar(self):
        self.hijos[0].entrar()

    def print(self):
        print("Laberinto") 

class Habitacion(Contenedor):
    def __init__(self, id):
        self.norte = None
        self.este = None
        self.oeste = None
        self.sur = None
        self.id = id

    def enter(self):
        print("Entraste a la habitación", self.id)

    def print(self):
        print("Habitacion")
    
class Hoja(ElementoMapa):
    def __init__(self):
        super().__init__()
    
    def print(self):
        print("Hoja")

class Decorator(Hoja):
    def __init__(self):
        super().__init__()
        self.comp = None
    
    def print(self):
        print("Decorator")

class Bomba(Decorator):
    pass


# laberinto.py

class Laberinto(Contenedor):
    def __init__(self):
        self.habitaciones = []

    def agregarHabitacion(self, habitacion):
        self.habitaciones.append(habitacion)
    
    def entrar(self):
        self.habitaciones[0].entrar()
    
    def print(self):
        print("Laberinto")

# habitacion.py

class Habitacion(ElementoMapa):
    def __init__(self, id):
        self.norte = None
        self.sur = None
        self.este = None
        self.oeste = None
        self.id = id
    
    def enter(self):
        print("Entraste a la habitación", self.id)

    def print(self):
        print("Habitacion")

# pared.py

class Pared(ElementoMapa):
    def __init__(self):
        pass
    
    def print(self):
        print("Pared")

# paredbomba.py

class ParedBomba(Pared):
    def __init__(self):
        super().__init__()
        self.activa = False
    
    def print(self):
        print("ParedBomba")

# puerta.py

class Puerta(ElementoMapa):
    def __init__(self, lado1, lado2):
        self.lado1 = lado1
        self.lado2 = lado2
        self.abierta = False
    
    def entrar(self):
        if self.abierta:
            self.side2.entrar()
        else:
            print("La puerta está cerrada")

    def print(self):
        print("Puerta")