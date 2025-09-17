import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Calculadora')))

from calculadora import somar, subtrair, multiplicar, dividir

class TestCalculadora(unittest.TestCase):

    def test_somar(self):
        self.assertEqual(somar(3, 2), 5)
        self.assertEqual(somar(-1, 1), 0)

    def test_subtrair(self):
        self.assertEqual(subtrair(5, 2), 3)

    def test_multiplicar(self):
        self.assertEqual(multiplicar(3, 4), 12)

    def test_dividir(self):
        self.assertEqual(dividir(10, 2), 5)
        self.assertEqual(dividir(5, 0), "Erro: divisão por zero!")

if __name__ == '__main__':
    unittest.main()
