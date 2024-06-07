import unittest
from factorial import factorial
class TestFactorial(unittest.TestCase):
    def test_factorial_positive(self):
    # Define un método de prueba para verificar factoriales de números positivos
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(3), 6)

    def test_factorial_zero_one(self):
    # Define un método de prueba para verificar el caso base del factorial
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(1), 1)

    def test_factorial_negative(self):
    # Define un método de prueba para verificar el comportamiento con números negativos
        with self.assertRaises(ValueError):
            factorial(-1)

if __name__ == '__main__':
    unittest.main()