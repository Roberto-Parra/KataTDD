import unittest
from KataTDD.conjunto import Conjunto

class TestConjunto(unittest.TestCase):

    def test_conjunto_vacio(self):
        conjunto = Conjunto({})
        #check caso vacios
        self.assertIsNone(conjunto.promedio())