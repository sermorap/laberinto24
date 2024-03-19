# bicho.pyclass Bicho:
import time

class Bicho:
    def __init__(self, modo):
        self.modo = modo
        self.poder = 2
        self.vida = 10
        self.posicion = None
        self.num = 0
    
    def __str__(self):
        plantilla = 'Bicho-{0.modo}{0.num}'
        return plantilla.format(self)
    
    def esAgresivo(self):
        return self.modo.esAgresivo()

    def esPerezoso(self):
        return self.modo.esPerezoso()
    
    def actuar(self):
        self.modo.actuar(self)
    
    def irAleatorio(self):
        self.posicion.irAleatorio(self)
    
    def irNorte(self):
        self.posicion.irNorte(self)

    def irEste(self):
        self.posicion.irEste(self)
    
    def irSur(self):
        self.posicion.irSur(self)
    
    def irOeste(self):
        self.posicion.irOeste(self)
    
    def start(self):
        self.actuar()
    
    def stop(self):
        print(self , " ha sido detenido")
        exit(0)

class Modo:
    def __init__(self):
        pass
    
    def __str__(self):    
        pass
    
    def esAgresivo(self):
        return False
    
    def esPerezoso(self):
        return False
    
    def actuar(self, bicho):
        self.dormir(bicho)
        self.caminar(bicho)
    
    def caminar(self, bicho):
        bicho.caminarAleatoriamente()
    
    def dormir(self, bicho):
        print(bicho," está durmiendo")
        time.sleep(3)

class Agresivo(Modo):
    def __init__(self):
        super().__init__()

    def __str__(self):
        return "Agresivo"
    
    def esAgresivo(self):
        return True

    def imprimir(self):
        print("Bicho agresivo")

class Perezoso(Modo):
    def __init__(self):
        super().__init__()
    
    def __str__(self):    
        return "Perezoso"

    def esPerezoso(self):
        return True
    
    def imprimir(self):
        print("Bicho perezoso")

