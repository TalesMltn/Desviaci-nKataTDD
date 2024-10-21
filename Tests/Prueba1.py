import unittest
from src.Logica.Logica import Conjunto, NoSePuedeCalcular

class TestConjunto(unittest.TestCase):
    def test_conjunto_vacio_lanzaExcepcion_desviacionEstandar(self):
        conjunto = Conjunto([])
        with self.assertRaises(NoSePuedeCalcular):
            conjunto.desviacion_estandar()

    def test_conjunto_unElemento_retornaCero_desviacionEstandar(self):
        conjunto = Conjunto([5])
        self.assertEqual(0, conjunto.desviacion_estandar())

    def test_conjunto_dosElementos_retornaDesviacionEstandar(self):
        conjunto = Conjunto([5, 7])
        promedio = (5 + 7) / 2
        # Cálculo de la desviación estándar directamente
        std_dev = ((5 - promedio) ** 2 + (7 - promedio) ** 2) / 2  # Population standard deviation
        self.assertAlmostEqual(std_dev ** 0.5, conjunto.desviacion_estandar(), places=2)

    def test_conjunto_nElementos_retornaDesviacionEstandar(self):
        conjunto = Conjunto([2, 4, 8, 9, 10, 15])
        # Cálculo del promedio
        promedio = sum(conjunto.elementos) / len(conjunto.elementos)
        # Cálculo de la varianza
        varianza = sum((x - promedio) ** 2 for x in conjunto.elementos) / len(conjunto.elementos)  # Population variance
        expected_std_dev = varianza ** 0.5  # Standard deviation
        self.assertAlmostEqual(expected_std_dev, conjunto.desviacion_estandar(), places=2)

if __name__ == "__main__":
    unittest.main()
