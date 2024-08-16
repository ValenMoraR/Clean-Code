# Todas las prueba sunitarias importan la biblioteca unittest
import unittest
from    Nomina import CalcularLiquidacion 

class CalcularLiquidacionTest(unittest.TestCase):

    # Pruebas Normales
    def test_liquidacion_normal_1(self):
        resultado = CalcularLiquidacion(salario= 3000000, semanas_trabajadas=4, 
                                        auxilio_transporte=162000, tiempo_festivo_lab=10, 
                                        Horas_Extras_Diu=5, Horas_Extras_Noc=3, Horas_Extras_Fes=2, 
                                        dias_incapacidad=5, porcentaje_incapacidad=0.66)
        print(f"Resultado de la liquidación: {resultado} COP")
        self.assertEqual(resultado, 2789000.0)  # Ejemplo de resultado esperado
        

    def test_liquidacion_normal_2(self):
        resultado = CalcularLiquidacion(salario=2000000, semanas_trabajadas=4, 
                                        auxilio_transporte=162000, tiempo_festivo_lab=5, 
                                        Horas_Extras_Diu=2, Horas_Extras_Noc=1, Horas_Extras_Fes=1, 
                                        dias_incapacidad=3, porcentaje_incapacidad=0.66)
        self.assertEqual(resultado, 1914773.33)

    def test_liquidacion_normal_3(self):
        resultado = CalcularLiquidacion(salario=2600000, semanas_trabajadas=4, 
                                        auxilio_transporte=0, tiempo_festivo_lab=8, 
                                        Horas_Extras_Diu=4, Horas_Extras_Noc=2, 
                                        Horas_Extras_Fes=1, 
                                        dias_incapacidad=0, porcentaje_incapacidad=0.66)
        self.assertEqual(resultado, 2625756.67)

    def test_liquidacion_normal_4(self):
        resultado = CalcularLiquidacion(salario=1800000, semanas_trabajadas=4, 
                                        auxilio_transporte=162000, tiempo_festivo_lab=0, 
                                        Horas_Extras_Diu=0, Horas_Extras_Noc=0, Horas_Extras_Fes=0, 
                                        dias_incapacidad=0, porcentaje_incapacidad=0.66)
        self.assertEqual(resultado, 1694640.0)

    def test_liquidacion_normal_5(self):
        resultado = CalcularLiquidacion(salario=2500000, semanas_trabajadas=4, 
                                        auxilio_transporte=162000, tiempo_festivo_lab=12, 
                                        Horas_Extras_Diu=6, Horas_Extras_Noc=3, Horas_Extras_Fes=2, 
                                        dias_incapacidad=4, porcentaje_incapacidad=0.66)
        self.assertEqual(resultado, 2546477.5)

    def test_liquidacion_normal_6(self):
        resultado = CalcularLiquidacion(salario=3500000, semanas_trabajadas=4, 
                                        auxilio_transporte=0, tiempo_festivo_lab=15, 
                                        Horas_Extras_Diu=7, Horas_Extras_Noc=4, Horas_Extras_Fes=3, 
                                        dias_incapacidad=0, porcentaje_incapacidad=0.66)
        self.assertEqual(resultado, 3649333.33)

    #Pruebas Extraordinarias
    def test_liquidacion_extrordinaria_1(self):
        resultado = CalcularLiquidacion(salario=4300000, semanas_trabajadas=4, 
                                        auxilio_transporte=0, tiempo_festivo_lab=0, 
                                        Horas_Extras_Diu=0, Horas_Extras_Noc=0, Horas_Extras_Fes=0, 
                                        dias_incapacidad=0, porcentaje_incapacidad=0.66)
        self.assertEqual(resultado, 3652133.33)  # Salario mayor a 4 SMLMV

    def test_liquidacion_extrordinaria_2(self):
        resultado = CalcularLiquidacion(salario=1200000, semanas_trabajadas=52, 
                                        auxilio_transporte=140606, tiempo_festivo_lab=0, 
                                        Horas_Extras_Diu=0, Horas_Extras_Noc=0, Horas_Extras_Fes=0, 
                                        dias_incapacidad=0, porcentaje_incapacidad=0.66)
        self.assertEqual(resultado, 13544240.0)  # Año completo de trabajo

    def test_liquidacion_extrordinaria_3(self):
        resultado = CalcularLiquidacion(salario=900000, semanas_trabajadas=2, 
                                        auxilio_transporte=140606, tiempo_festivo_lab=0, 
                                        Horas_Extras_Diu=0, Horas_Extras_Noc=0, Horas_Extras_Fes=0, 
                                        dias_incapacidad=0, porcentaje_incapacidad=0.66)
        self.assertEqual(resultado, 535440.0)  # Salario bajo

    def test_liquidacion_extrordinaria_4(self):
        resultado = CalcularLiquidacion(salario=5000000, semanas_trabajadas=4, 
                                        auxilio_transporte=0, tiempo_festivo_lab=40, 
                                        Horas_Extras_Diu=20, Horas_Extras_Noc=10, Horas_Extras_Fes=5, 
                                        dias_incapacidad=0, porcentaje_incapacidad=0.66)
        self.assertEqual(resultado, 6208125.0)  # Muchas horas extras

    def test_liquidacion_extrordinaria_5(self):
        resultado = CalcularLiquidacion(salario=2600000, semanas_trabajadas=1, 
                                        auxilio_transporte=0, tiempo_festivo_lab=1, 
                                        Horas_Extras_Diu=1, Horas_Extras_Noc=1, Horas_Extras_Fes=1, 
                                        dias_incapacidad=1, porcentaje_incapacidad=0.66)
        self.assertEqual(resultado, 745588.33)  # Trabajó solo una semana

    def test_liquidacion_extrordinaria_6(self):
        resultado = CalcularLiquidacion(salario=4200000, semanas_trabajadas=2, 
                                        auxilio_transporte=0, tiempo_festivo_lab=0, 
                                        Horas_Extras_Diu=0, Horas_Extras_Noc=0, Horas_Extras_Fes=0, 
                                        dias_incapacidad=15, porcentaje_incapacidad=0.66)
        self.assertEqual(resultado, 1084300.0)  # Muchos días de incapacidad

    # Casos de Error (Excepciones)
    def test_liquidacion_error_salario_negativo(self):
        with self.assertRaises(ValueError):
            CalcularLiquidacion(salario=-3000000, semanas_trabajadas=4, 
                                auxilio_transporte=62000, tiempo_festivo_lab=10, 
                                Horas_Extras_Diu=5, Horas_Extras_Noc=3, Horas_Extras_Fes=2, 
                                dias_incapacidad=5, porcentaje_incapacidad=0.66)

    def test_liquidacion_error_semanas_negativas(self):
        with self.assertRaises(ValueError):
            CalcularLiquidacion(salario=3000000, semanas_trabajadas=-4, 
                                auxilio_transporte=162000, tiempo_festivo_lab=10, 
                                Horas_Extras_Diu=5, Horas_Extras_Noc=3, Horas_Extras_Fes=2, 
                                dias_incapacidad=5, porcentaje_incapacidad=0.66)

    def test_liquidacion_error_tiempo_festivo_negativo(self):
        with self.assertRaises(ValueError):
            CalcularLiquidacion(salario=3000000, semanas_trabajadas=4, 
                                auxilio_transporte=62000, tiempo_festivo_lab=-10, 
                                Horas_Extras_Diu=5, Horas_Extras_Noc=3, Horas_Extras_Fes=2, 
                                dias_incapacidad=5, porcentaje_incapacidad=0.66)

    def test_liquidacion_error_horas_extras_negativas(self):
        with self.assertRaises(ValueError):
            CalcularLiquidacion(salario=3000000, semanas_trabajadas=4, 
                                auxilio_transporte=62000, tiempo_festivo_lab=10, 
                                Horas_Extras_Diu=-5, Horas_Extras_Noc=3, Horas_Extras_Fes=2, 
                                dias_incapacidad=5, porcentaje_incapacidad=0.66)

    def test_liquidacion_error_dias_incapacidad_negativos(self):
        with self.assertRaises(ValueError):
            CalcularLiquidacion(salario=3000000, semanas_trabajadas=4, 
                                auxilio_transporte=62000, tiempo_festivo_lab=10, 
                                Horas_Extras_Diu=5, Horas_Extras_Noc=3, Horas_Extras_Fes=2, 
                                dias_incapacidad=-5, porcentaje_incapacidad=0.66)

    def test_liquidacion_error_porcentaje_incapacidad_negativo(self):
        with self.assertRaises(ValueError):
            CalcularLiquidacion(salario=3000000, semanas_trabajadas=4, 
                                auxilio_transporte=62000,tiempo_festivo_lab=10, 
                                Horas_Extras_Diu=5, Horas_Extras_Noc=3, Horas_Extras_Fes=2, 
                                dias_incapacidad=5, porcentaje_incapacidad=-0.66)

    def test_liquidacion_error_salario_no_numerico(self):
        with self.assertRaises(ValueError):
            CalcularLiquidacion(salario="tres millones", semanas_trabajadas=4, 
                                auxilio_transporte=62000, tiempo_festivo_lab=10, 
                                Horas_Extras_Diu=5, Horas_Extras_Noc=3, Horas_Extras_Fes=2, 
                                dias_incapacidad=5, porcentaje_incapacidad=0.66)

    def test_liquidacion_error_horas_extras_no_numerico(self):
        with self.assertRaises(ValueError):
            CalcularLiquidacion(salario=3000000, semanas_trabajadas=4, auxilio_transporte=62000, tiempo_festivo_lab=10, Horas_Extras_Diu="cinco", Horas_Extras_Noc=3, Horas_Extras_Fes=2, dias_incapacidad=5, porcentaje_incapacidad=0.66)




# Este fragmento de codigo permite ejecutar la prueb individualmente
# Va fijo en todas las pruebas
if __name__ == '__main__':
    unittest.main()

