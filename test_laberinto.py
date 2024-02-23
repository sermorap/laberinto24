import unittest
from laberinto import Juego, JuegoBomba, ParedBomba

class TestJuego(unittest.TestCase):
    
    def test_crearHabitacion_returns_habitacion_con_paredes(self):
        juego = Juego()
        habitacion = juego.crearHabitacion(1)
        self.assertIsNotNone(habitacion.norte)
        self.assertIsNotNone(habitacion.sur)
        self.assertIsNotNone(habitacion.este)
        self.assertIsNotNone(habitacion.oeste)

    def test_crearHabitacion_returns_habitacion_con_id_correcto(self):
        juego = Juego()
        habitacion = juego.crearHabitacion(5)
        self.assertEqual(habitacion.id, 5)
        
    def test_crearHabitacion_returns_habitacion_con_paredes_bomba(self):
        juego = JuegoBomba()
        hab = juego.crearHabitacion(1)
        self.assertIsInstance(hab.norte, ParedBomba)
        self.assertIsInstance(hab.sur, ParedBomba)
        self.assertIsInstance(hab.este, ParedBomba)
        self.assertIsInstance(hab.oeste, ParedBomba)
    
    def test_crearHabitacion_returns_habitacion_con_paredes_diferentes(self):
        juego = Juego()
        habitacion = juego.crearHabitacion(1)
        self.assertNotEqual(habitacion.norte, habitacion.sur)
        self.assertNotEqual(habitacion.norte, habitacion.este)
        self.assertNotEqual(habitacion.norte, habitacion.oeste)
        self.assertNotEqual(habitacion.sur, habitacion.este)
        self.assertNotEqual(habitacion.sur, habitacion.oeste)
        self.assertNotEqual(habitacion.este, habitacion.oeste)
    
if __name__ == '__main__':
    unittest.main()