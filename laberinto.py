# mapelement.py
import random

class ElementoMapa:
    def __init__(self):
        pass
    def entrar(self):
        pass

    def print(self):
        print("ElementoMapa")
    
    def esHabitacion(self):
        return False

class Contenedor(ElementoMapa):
    #Composite
    def __init__(self):
        super().__init__()
        self.hijos = []
        self.orientaciones=[]
        
    def agregarHijo(self, hijo):
        self.hijos.append(hijo)
        
    def eliminarHijo(self, hijo):
        self.hijos.remove(hijo)
    
    def print(self):
        print("Contenedor")
    
    def irAleatorio(self, someone):
        pass

    def agregarOrientacion(self, orientacion):
        self.orientaciones.append(orientacion)

    def eliminarOrientacion(self, orientacion):
        self.orientaciones.remove(orientacion)

    def irAleatorio(self, someone):        
        orientacion = self.getOrientacionAleatoria()
        orientacion.caminarAleatoriamente(someone)

    def getOrientacionAleatoria(self):
        return random.choice(self.orientaciones)

    def irNorte(self, someone):
        self.norte.entrar(someone)
    def irEste(self, someone):
        self.este.entrar(someone)
    def irSur(self, someone):
        self.sur.entrar(someone)
    def irOeste(self, someone):
        self.oeste.entrar(someone)
    def setEMinOr(self, em, orientacion):
        orientacion.establecerEMinOr(em, self)


class Laberinto(Contenedor):
    def __init__(self):
        super().__init__()

    def agregarHabitacion(self, habitacion):
        self.hijos.append(habitacion)

    def entrar(self):
        self.hijos[0].entrar()

    def print(self):
        print("Laberinto") 
    
    def getHabitacion(self, id):
        for habitacion in self.hijos:
            if habitacion.id == id:
                return habitacion
        return None

class Habitacion(Contenedor):
    def __init__(self, id):
        super().__init__()
        self.norte = None
        self.este = None
        self.oeste = None
        self.sur = None
        self.id = id

    def entrar(self, someone):
        print(someone + "entro a la habitación", self.id)

    def print(self):
        print("Habitacion")

    def esHabitacion(self):
        return True
    
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
    def __init__(self):
        super().__init__()
        self.activa = False

    def print(self):
        print("Bomba")

    def entrar(self, someone):
        print(someone + " chocó contra una bomba")

class Pared(ElementoMapa):
    def __init__(self):
        pass
    
    def imprimir(self):
        print("Pared")

    def entrar(self, someone):
        print(someone, "chocó contra una pared")

# paredbomba.py

class ParedBomba(Pared):
    def __init__(self):
        super().__init__()
        self.activa = False
    
    def imprimir(self):
        print("Pared bomba")

# puerta.py

class Puerta(ElementoMapa):
    def __init__(self, lado1, lado2):
        self.lado1 = lado1
        self.lado2 = lado2
        self.abierta = False
    
    def entrar(self, alguien):
        if self.abierta:
            self.lado2.entrar()
        else:
            print("La puerta está cerrada")

    def imprimir(self):
        print("Puerta")

class Orientacion:
    def __init__(self):
        pass
    def irAleatorio(self, someone):
        pass
    def setEMinOr(self, em, unContenedor):
        pass

class Norte(Orientacion):
    _instancia = None
    def __init__(self):
        if not Norte._instancia:
            super().__init__()
            Norte._instancia = self
    def setEMinOr(self, em, unContenedor):
        unContenedor.norte = em

    @classmethod
    def obtener_instancia(cls):
        if not cls._instancia:
            cls._instancia = Norte()
        return cls._instancia

    def imprimir(self):
        print("Norte")
    
    def irAleatotio(self, someone):
        someone.irNorte()


class Sur(Orientacion):
    _instancia = None
    def __init__(self):
        if not Sur._instancia:
            super().__init__()  
            Sur._instancia = self

    @staticmethod 
    def obtener_instancia():
        if not Sur._instancia:
            Sur()
        return Sur._instancia
    
    def imprimir(self):
        print("Sur")
    
    def irAleatorio(self, someone):
        someone.irSur()
    
    def setEMinOr(self, em, unContenedor):
        unContenedor.sur = em

class Este(Orientacion):
    _instancia = None
    def __init__(self):
        raise RuntimeError('Llame a obtener_instancia() en su lugar')
        

    @classmethod
    def obtener_instancia(cls):
        if cls._instancia is None:
            print('Creando nueva instancia')
            cls._instancia = cls.__new__(cls)
            # Put any initialization here.
        return cls._instancia
    
    def irAleatorio(self, someone):
        someone.irEste()
    
    def setEMinOr(self, em, unContenedor):
        unContenedor.este = em
    
        
class Oeste(Orientacion):
    _instancia = None
    def __init__(self):
        if not Oeste._instancia:
            super().__init__()
            Oeste._instancia = self

    @staticmethod
    def obtener_instancia():
        if not Oeste._instancia:
            Oeste()
        return Oeste._instancia
    
    def imprimir(self):
        print("Oeste")
    
    def irAleatorio(self, someone):
        someone.irOeste()

    def setEMinOr(self, em, unContenedor):
        unContenedor.oeste = em
