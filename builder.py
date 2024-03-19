import json
from laberinto import Laberinto, Habitacion, Puerta, Pared, Bomba, Norte, Este, Sur, Oeste

class Director:
    def __init__(self):
        self.dict = None
        self.builder = ConstructorLaberinto()

    def procesar(self, filename):
        self.leer_archivo(filename)
        self.crear_laberinto()

    def leer_archivo(self, filename):
        try:
            with open(filename) as f:
                datos = json.load(f)
                self.dict = datos
        except FileNotFoundError:
            print(f"El archivo {filename} no existe")
            return None

    def crear_laberinto(self):
        self.builder.crearLaberinto()

        for each in self.dict['laberinto']:
            self.crear_laberinto_recursivo(each, 'raiz')

        for each in self.dict['puertas']:
            n1 = each[0]
            or1 = each[1]
            n2 = each[2]
            or2 = each[3]
            self.builder.crearPuerta(n1, or1, n2, or2)

    def crear_laberinto_recursivo(self, un_dic, padre):

        if un_dic['tipo'] == 'habitacion':
            con = self.builder.crearHabitacion(un_dic['num'])

        if un_dic['tipo'] == 'bomba':
            self.builder.crearBombaEn(padre)

        if 'hijos' in un_dic:
            for elemento in un_dic['hijos']:
                self.crear_laberinto_recursivo(elemento, con)

class ConstructorLaberinto:
    def __init__(self):
        self.juego = None
        self.laberinto = None

    def crearLaberinto(self):
        self.laberinto = Laberinto()

    def crearPared(self):
        return Pared()

    def crearPuerta(self, habitacion1, habitacion2):
        puerta = Puerta(habitacion1, habitacion2)
        return puerta

    def crearBombaEn(self, habitacion):
        bomba = Bomba()
        habitacion.agregarHijo(bomba)
        return bomba

    def crearHabitacion(self, id):
        habitacion = Habitacion(id)
        habitacion.agregarOrientacion(self.crearNorte())
        habitacion.agregarOrientacion(self.crearEste())
        habitacion.agregarOrientacion(self.crearSur())
        habitacion.agregarOrientacion(self.crearOeste())
        for orientacion in habitacion.orientaciones:
            orientacion.establecerEMinOr(self.crearPared, self)
        self.laberinto.agregarHabitacion(habitacion)
        return habitacion

    def crearNorte(self):
        return Norte.obtener_instancia()

    def crearEste(self):
        return Este.obtener_instancia()

    def crearSur(self):
        return Sur.obtener_instancia()

    def crearOeste(self):
        return Oeste.obtener_instancia()

    def crearPuerta(self, numero1, orientacion1, numero2, orientacion2):

        lado1 = self.laberinto.obtenerHabitacion(numero1)
        lado2 = self.laberinto.obtenerHabitacion(numero2)

        or1 = getattr(self, 'crear'+orientacion1)()
        or2 = getattr(self, 'crear'+orientacion2)()

        puerta = Puerta(lado1, lado2)

        lado1.setEMinOr(puerta, or1)
        lado2.setEMinOr(puerta, or2)


director = Director()
director.procesar('/Users/34722/Documentos/Esiiab/TERCERO/2 CUATRIMESTRE/Diseño de Software/Proyecto/laberintos/laberinto2Rroom.json')

director.dict
