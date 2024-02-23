import unittest
from laberinto import Juego, Laberinto, Habitacion, Puerta

class TestJuegoLaberinto(unittest.TestCase):

    def test_crear_laberinto(self):
        juego = Juego()
        laberinto = juego.fabricarLaberinto2HabitacionesFM()
        
        self.assertIsInstance(laberinto, Laberinto)
        
        habitaciones = laberinto.habitaciones
        self.assertEqual(len(habitaciones), 2)
        
        habitacion1, habitacion2 = habitaciones
        
        self.assertIsInstance(habitacion1, Habitacion)
        self.assertIsInstance(habitacion2, Habitacion)
        
        # Verificamos puertas y paredes
        self.assertIsNotNone(habitacion1.norte) 
        self.assertIsNotNone(habitacion1.sur)
        self.assertIsNotNone(habitacion1.este)
        self.assertIsNotNone(habitacion1.oeste)
        
        self.assertIsNotNone(habitacion2.norte)
        self.assertIsNotNone(habitacion2.sur)
        self.assertIsNotNone(habitacion2.este)
        self.assertIsNotNone(habitacion2.oeste)  
        
        # Verificar que las paredes sean distintas instancias
        self.assertIsNot(habitacion1.norte, habitacion2.norte)
        self.assertIsNot(habitacion1.sur, habitacion2.sur)
        
        # Verificar que al sur de habitacion1 hay un objeto de tipo puerta
        self.assertIsInstance(habitacion1.sur, Puerta)

    def test_crear_laberinto_habitaciones_diferentes(self):
        juego = Juego()
        laberinto = juego.fabricarLaberinto2HabitacionesFM()
        
        habitaciones = laberinto.habitaciones
        habitacion1, habitacion2 = habitaciones

        # Verificar que las habitaciones son distintas instancias
        self.assertIsNot(habitacion1, habitacion2)

if __name__ == '__main__':
    unittest.main()
