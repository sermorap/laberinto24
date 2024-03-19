import unittest
from laberinto import Habitacion
from juego import Juego

class TestGame(unittest.TestCase):

    def test_create4Room4BeastFM(self):
        juego = Juego()
        juego.fabricarLaberinto4Habitaciones4BichosFM()
        
        # Verificar numero de habitaciones
        self.assertEqual(len(juego.laberinto.hijos), 4)
        self.assertEqual(len(juego.bichos), 4)
        
        # Verificar las conexopnes de las habitaciones
        h1 = juego.laberinto.agregarHabitacion(1)
        h2 = juego.laberinto.agregarHabitacion(2) 
        h3 = juego.laberinto.agregarHabitacion(3)
        h4 = juego.laberinto.agregarHabitacion(4)

        
        self.assertIs(h1.sur, h2.norte)
        self.assertIs(h1.este, h3.oeste)
        self.assertIs(h2.este, h4.oeste)
        self.assertIs(h3.sur, h4.norte)
        
        # Verificar las posiciones de los bichos
        self.assertTrue(juego.bichos[0].posicion.esHabitacion)
        self.assertTrue(juego.bichos[1].posicion.esHabitacion)
        self.assertTrue(juego.bichos[2].posicion.esHabitacion)
        self.assertTrue(juego.bichos[3].posicion.esHabitacion)
        
        self.assertIs(juego.bichos[0].posicion, h1)
        self.assertIs(juego.bichos[1].posicion, h2)
        self.assertIs(juego.bichos[2].posicion, h3)
        self.assertIs(juego.bichos[3].posicion, h4)
        
        self.assertTrue(juego.bichos[0].esAgresivo())
        self.assertTrue(juego.bichos[1].esPerezoso())
        self.assertTrue(juego.bichos[2].esAgresivo())
        self.assertTrue(juego.bichos[3].esPerezoso())

       
if __name__ == '__main__':
    unittest.main()