import unittest
from src.logica.OperacionesEnteros import OperacionesEnteros
from src.logica.OperacionesEnteros import FaltanParametros

class PruebaOperacionesEnteros(unittest.TestCase):

    def test_MCD_cincoNumerosPositivos_retornaMCD(self):
        # Arrange
        numero1 = 26
        numero2 = 28
        numero3 = 36
        numero4 = 8
        numero5 = 15
        resultadoEsperado = 1
        operacion = OperacionesEnteros([numero1, numero2, numero3, numero4, numero5])

        # Do
        resultadoActual = operacion.calcularMCD()

        # Assert
        self.assertEqual(resultadoEsperado, resultadoActual)