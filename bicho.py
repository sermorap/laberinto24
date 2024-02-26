# bicho.py
class Beast:
    def __init__(self, modo):
        self.modo = modo
        self.poder = 2
        self.vida = 10

# modo.py
class Modo:
    def __init__(self):
        pass

class Agresivo(Modo):
    def print(self):
        print("Bicho agresivo")

class Perezoso(Modo):
    def print(self):
        print("Bicho perezoso")