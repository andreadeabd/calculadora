import unittest
from calculadora import Calculadora

class TestCalculadora(unittest.TestCase):
    def test_multiplicar(self):
        self.assertEqual(Calculadora.multiplicar(2, 3), 6)
        self.assertEqual(Calculadora.multiplicar(-2, 3), -6)
        self.assertEqual(Calculadora.multiplicar(0, 100), 0)
        self.assertEqual(Calculadora.multiplicar(5, 1.5), 7.5)

if __name__ == "__main__":
    unittest.main()
