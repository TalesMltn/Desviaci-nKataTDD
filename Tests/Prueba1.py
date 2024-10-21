# tests/test_conjunto.py
import unittest
from src.logica.Conjunto import Conjunto, NoSePuedeCalcular


class TestConjunto(unittest.TestCase):

    def test_conjunto_vacio_lanzaExcepcion_promedio(self):
        conjunto = Conjunto([])
        with self.assertRaises(NoSePuedeCalcular):
            conjunto.promedio()

    def test_conjunto_unElemento_retornaValorUnicoElemento(self):
        conjunto = Conjunto([5])
        self.assertEqual(5, conjunto.promedio())

    def test_conjunto_dosElementos_retornaPromedioElementos(self):
        conjunto = Conjunto([5, 7])
        self.assertEqual(6, conjunto.promedio
