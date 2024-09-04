import unittest
import sys
sys.path.append("src")
from LiquidacionNomina import Liquida_nomina1

class Liquidacion_test(unittest.TestCase):

    # Pruebas normales (casos esperados)
    def test_liquidacion_basica(self):
        resultado = Liquida_nomina1.CalcularLiquidacion(salario_mensual=1500000, semanas_trabajadas = 24)
        self.assertEqual(resultado, 6773040.0)

    def test_liquidacion_completa(self):
        resultado = Liquida_nomina1.CalcularLiquidacion(salario_mensual=1300000, semanas_trabajadas = 7, horas_extras_diurnas=13,
                                                        horas_extras_nocturnas=3, tiempo_festivo_laborado=8, dias_licencia=7, dias_incapacidad=3)
        self.assertEqual(resultado, 1653725.0)


    def test_liquidacion_con_extras(self):
        resultado = Liquida_nomina1.CalcularLiquidacion(salario_mensual=2200000, semanas_trabajadas=26, 
                                                        horas_extras_diurnas=10, horas_extras_nocturnas=5)
        self.assertEqual(resultado, 10853048.33)
    
    def test_liquidacion_normal(self):
        resultado = Liquida_nomina1.CalcularLiquidacion(salario_mensual= 3000000, semanas_trabajadas=4, tiempo_festivo_laborado=8, 
                                        horas_extras_diurnas=5, horas_extras_nocturnas=3, horas_extras_festivos=2, 
                                        dias_incapacidad=5)
        self.assertEqual(resultado, 2380750.00) 
        

    def test_liquidacion_regular(self):
        resultado = Liquida_nomina1.CalcularLiquidacion(salario_mensual=2000000, semanas_trabajadas= 14,  tiempo_festivo_laborado=5, 
                                        horas_extras_diurnas=2, horas_extras_nocturnas=1, horas_extras_festivos=1, 
                                        dias_incapacidad=3)
        self.assertEqual(resultado, 5349440.0)

    def test_liquidacion_natural(self):
        resultado = Liquida_nomina1.CalcularLiquidacion(salario_mensual=2600000, semanas_trabajadas=4, tiempo_festivo_laborado=8, 
                                        horas_extras_diurnas=4, horas_extras_nocturnas=2, horas_extras_festivos=1)
        self.assertEqual(resultado, 2306823.33)

    # PRUEBAS EXTRAORDINARIAS (casos límites o inusuales)
    def test_liquidacion_con_incapacidad(self):
        resultado = Liquida_nomina1.CalcularLiquidacion(salario_mensual=4000000, semanas_trabajadas=20, dias_incapacidad=15)
        self.assertEqual(resultado, 14054000.0)

    def test_liquidacion_con_retencion(self):
        resultado = Liquida_nomina1.CalcularLiquidacion(salario_mensual=7000000, semanas_trabajadas=8, dias_incapacidad=1)
        self.assertEqual(resultado, 9554300.0)

    def test_liquidacion_sin_transporte(self):
        resultado = Liquida_nomina1.CalcularLiquidacion(salario_mensual=3000000, semanas_trabajadas=10)
        self.assertEqual(resultado, 5520000.00)
    
    def test_con_dias_de_licencia_(self):
        salario_mensual=1000000
        semanas_trabajadas=3
        dias_licencia = 6
        resultado = Liquida_nomina1.CalcularLiquidacion(salario_mensual, semanas_trabajadas, dias_licencia)
        self.assertEqual(resultado, 741290.0)

    def test_liquidacion_salario_bajo(self):
        resultado = Liquida_nomina1.CalcularLiquidacion(salario_mensual=900000, semanas_trabajadas=2)
        self.assertEqual(resultado, 480240.0)  # Salario bajo
    
    def test_un_dia_de_licencia(self):
        resultado = Liquida_nomina1.CalcularLiquidacion(salario_mensual=1900000, semanas_trabajadas=12, 
        dias_licencia= 1)
        self.assertEqual(resultado, 4280906.67)

    # PRUEBAS DE ERROR (manejo de errores)
    def test_salario_negativo(self):
        salario_mensual=-1000000
        semanas_trabajadas=20
        with self.assertRaises(Liquida_nomina1.ValorNegativo):
            resultado = Liquida_nomina1.CalcularLiquidacion(salario_mensual, semanas_trabajadas)
           
    def test_semanas_trabajas_cero(self):
        salario_mensual=2000000
        semanas_trabajadas=0 
        with self.assertRaises(Liquida_nomina1.SemanaCero):
            resultado = Liquida_nomina1.CalcularLiquidacion(salario_mensual, semanas_trabajadas)
            
    def test_horas_extras_diurnas_negativas(self):
        salario_mensual=1300000
        semanas_trabajadas=4
        horas_extras_diurnas =-3
        with self.assertRaises(Liquida_nomina1.ValorNegativo):
            resultado = Liquida_nomina1.CalcularLiquidacion(salario_mensual, semanas_trabajadas, horas_extras_diurnas)

    def test_liquidacion_festivo_mas_de_8h(self):
        salario_mensual= 3000000
        semanas_trabajadas=4
        tiempo_festivo_laborado=10
        horas_extras_diurnas=5
        horas_extras_nocturnas=3
        horas_extras_festivos=2
        dias_incapacidad=5
        with self.assertRaises(Liquida_nomina1.MasDe8HorasFestivoLaboradas):
            resultado = Liquida_nomina1.CalcularLiquidacion(salario_mensual, semanas_trabajadas, tiempo_festivo_laborado, 
                                        horas_extras_diurnas, horas_extras_nocturnas, horas_extras_festivos, 
                                        dias_incapacidad)
      
    def test_liquidacion_dias_incapacidad_negativos(self):
        salario_mensual=3000000
        semanas_trabajadas=4
        tiempo_festivo_laborado=6 
        horas_extras_diurnas=5
        horas_extras_nocturnas=3 
        dias_incapacidad=-5
        with self.assertRaises(Liquida_nomina1.ValorNegativo):
            resultado = Liquida_nomina1.CalcularLiquidacion(salario_mensual, semanas_trabajadas, tiempo_festivo_laborado, 
                                horas_extras_diurnas, horas_extras_nocturnas, 
                                dias_incapacidad)
            
    def test_liquidacion_salario_no_numerico(self):
        salario_mensual="tres millones"
        semanas_trabajadas=7
        tiempo_festivo_laborado=10
        horas_extras_diurnas=5
        horas_extras_nocturnas=3
        horas_extras_festivos=2
        dias_incapacidad=5
        with self.assertRaises(Liquida_nomina1.ValorInvalido):
            resultado= Liquida_nomina1.CalcularLiquidacion(salario_mensual, semanas_trabajadas,  tiempo_festivo_laborado, 
                                horas_extras_diurnas, horas_extras_nocturnas, horas_extras_festivos, 
                                dias_incapacidad)

    def test_liquidacion_horas_extras_no_numerico(self):
        with self.assertRaises(Liquida_nomina1.ValorInvalido):
            resultado = Liquida_nomina1.CalcularLiquidacion(salario_mensual=3000000, semanas_trabajadas=4 , tiempo_festivo_laborado=10, 
                                horas_extras_diurnas="cinco", horas_extras_nocturnas=3, horas_extras_festivos=2, dias_incapacidad=5)
           
    def test_liquidacion_tiempo_festivo_negativo(self):
        with self.assertRaises(Liquida_nomina1.ValorNegativo):
            resultado = Liquida_nomina1.CalcularLiquidacion(salario_mensual=3000000, semanas_trabajadas=4, tiempo_festivo_laborado=-10, 
                                horas_extras_diurnas=5, horas_extras_nocturnas=3, horas_extras_festivos=2, 
                                dias_incapacidad=5)

if __name__ == '__main__':
    unittest.main()
