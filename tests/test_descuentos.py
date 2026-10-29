import unittest
from src.descuentos import calcular_total

class PruebasDescuentos(unittest.TestCase):
    def test_descuento_10(self):
        self.assertEqual(calcular_total(1000, 10), 900)

    def test_descuento_15(self):
        self.assertEqual(calcular_total(1000, 15), 850)

    def test_descuento_16(self):
        self.assertEqual(calcular_total(1000, 16), "Descuento no permitido")

    def test_descuento_negativo(self):
        self.assertEqual(calcular_total(1000, -5), "Descuento no permitido")

if __name__ == "__main__":
    unittest.main()
