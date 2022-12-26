# importar el marco de prueba de Python
import unittest
# nuestra "unidad"
# esto es en lo que estamos ejecutando nuestra prueba
def isEven(n):
    if n % 2 == 0:
       return True
    else:
       return False
class IsEvenTests(unittest.TestCase):
    def testTwo(self):
        self.assertEqual(isEven(2), True)
        self.assertTrue(isEven(2))
    def testThree(self):
        self.assertEqual(isEven(3), False)
        self.assertFalse(isEven(3))
    def setUp(self):
        print("running setUp")
    def tearDown(self):
        print("running tearDown tasks")
if __name__ == '__main__':
    unittest.main() # esto ejecuta nuestras pruebas

