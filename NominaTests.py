# Todas las prueba sunitarias importan la biblioteca unittest
import unittest
from nomina1 import CalcularLiquidacion 

class NominaTestCase(unittest.TestCase):

    def testLiquidacion1(self):
        salario_base = 1000000
        dias_trabajados = 30

        # Cálculo del salario proporcional
        salario_proporcional = salario_base  # Porque trabajó todos los días del mes

        # Cálculo de las prestaciones sociales
        vacaciones = salario_proporcional * dias_trabajados / 720

        # Cálculo del resultado esperado total
        resultado_esperado = salario_proporcional +  vacaciones
        resultado = CalcularLiquidacion(salario_base, dias_trabajados)
        self.assertEqual(round(resultado, 2), round(resultado_esperado, 2))

    def testLiquidacion2(self):
        salario_base = 1200000
        dias_trabajados = 30
        auxilio_transporte = 106454
        salario_proporcional = salario_base * dias_trabajados / 30
        vacaciones = salario_proporcional * dias_trabajados / 720
        resultado_esperado = salario_proporcional + auxilio_transporte + vacaciones
        
        resultado = CalcularLiquidacion(salario_base, dias_trabajados, auxilio_transporte)
        self.assertEqual(round(resultado, 2), round(resultado_esperado, 2))

    def testLiquidacion3(self):
        salario_base = 900000
        dias_trabajados = 15
        
        # Cálculo esperado manual que incluya todos los componentes
        salario_proporcional = (salario_base / 30) * dias_trabajados
        vacaciones = salario_proporcional * dias_trabajados / 720
        resultado_esperado = salario_proporcional +  vacaciones
        
        resultado = CalcularLiquidacion(salario_base, dias_trabajados)
        
        self.assertEqual(round(resultado, 2), round(resultado_esperado, 2))

    def testLiquidacion4(self):
        with self.assertRaises(Exception):
            CalcularLiquidacion('mil', 30)

    def testLiquidacion5(self):
        salario_base = 1000000
        dias_trabajados = 370
        with self.assertRaises(Exception):
            CalcularLiquidacion(salario_base, dias_trabajados)


# Este fragmento de codigo permite ejecutar la prueb individualmente
# Va fijo en todas las pruebas
if __name__ == '__main__':
    unittest.main()