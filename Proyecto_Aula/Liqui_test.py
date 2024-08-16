import unittest
import Liquida_nomina1

class Liqui_test(unittest.TestCase):

    # Pruebas normales (casos esperados)
    def test1_liquidacion_basica(self):
        resultado = Liquida_nomina1.CalcularLiquidacion(salario=1500000, semanas_trabajadas = 24)
        self.assertEqual(resultado, 6773040.0)

    def test_liquidacion_complet(self):
        resultado = Liquida_nomina1.CalcularLiquidacion(salario=1300000, semanas_trabajadas = 7, Horas_Extras_Diu=13,
                                                        Horas_Extras_Noc=3, tiempo_festivo_lab=8, dias_licencia=7, dias_incapacidad=3)
        self.assertEqual(resultado, 1653725.0)


    def test2_liquidacion_con_extras(self):
        resultado = Liquida_nomina1.CalcularLiquidacion(salario=2200000, semanas_trabajadas=26, 
                                                        Horas_Extras_Diu=10, Horas_Extras_Noc=5)
        self.assertEqual(resultado, 10853048.33)
    
    ##########################
    #AQUI ABAJO 
    #   |
    #   |
    #   |
    #   V
    def test_liquidacion_normal_1(self):
        resultado = Liquida_nomina1.CalcularLiquidacion(salario= 3000000, semanas_trabajadas=4, tiempo_festivo_lab=8, 
                                        Horas_Extras_Diu=5, Horas_Extras_Noc=3, Horas_Extras_Fes=2, 
                                        dias_incapacidad=5)
        print(f"Resultado de la liquidación: {resultado} COP")
        self.assertEqual(resultado, 2380750.00)  # Ejemplo de resultado esperado
        

    def test_liquidacion_normal_2(self):
        resultado = Liquida_nomina1.CalcularLiquidacion(salario=2000000, semanas_trabajadas= 14,  tiempo_festivo_lab=5, 
                                        Horas_Extras_Diu=2, Horas_Extras_Noc=1, Horas_Extras_Fes=1, 
                                        dias_incapacidad=3)
        print(f"Resultado de la liquidación: {resultado} COP")
        self.assertEqual(resultado, 5349440.0)

    def test_liquidacion_normal_3(self):
        resultado = Liquida_nomina1.CalcularLiquidacion(salario=2600000, semanas_trabajadas=4, tiempo_festivo_lab=8, 
                                        Horas_Extras_Diu=4, Horas_Extras_Noc=2, Horas_Extras_Fes=1)
        print(f"Resultado de la liquidación: {resultado} COP")
        self.assertEqual(resultado, 2306823.33)

    # PRUEBAS EXTRAORDINARIAS (casos límites o inusuales)
    def test3_liquidacion_con_incapacidad(self):
        resultado = Liquida_nomina1.CalcularLiquidacion(salario=4000000, semanas_trabajadas=20, dias_incapacidad=15)
        self.assertEqual(resultado, 14054000.0)

    def test_liquidacion_con_retencion(self):
        resultado = Liquida_nomina1.CalcularLiquidacion(salario=7000000, semanas_trabajadas=8, dias_incapacidad=1)
        self.assertEqual(resultado, 9554300.0)

    def test4_liquidacion_sin_transporte(self):
        resultado = Liquida_nomina1.CalcularLiquidacion(salario=3000000, semanas_trabajadas=10)
        self.assertEqual(resultado, 5520000.00)
    
    def test_licencia_(self):
        salario=1000000
        semanas_trabajadas=3
        dias_licencia = 6
        resultado = Liquida_nomina1.CalcularLiquidacion(salario, semanas_trabajadas, dias_licencia)
        self.assertEqual(resultado, 741290.0)

    def test_liquidacion_salario_bajo(self):
        resultado = Liquida_nomina1.CalcularLiquidacion(salario=900000, semanas_trabajadas=2,)
        self.assertEqual(resultado, 480240.0)  # Salario bajo
    
    def test_licencia_menor_a5(self):
        resultado = Liquida_nomina1.CalcularLiquidacion(salario=1900000, semanas_trabajadas=12, 
        dias_licencia= 3)
        self.assertEqual(resultado, 4344240.0)


    # PRUEBAS DE ERROR (manejo de errores)
    def test5_salario_negativo(self):
        try: 
            resultado = Liquida_nomina1.CalcularLiquidacion(salario=-1000000, semanas_trabajadas=20)
            print(resultado)
        except Exception:
                print("\n * * * * * * * * * * * * * * * * ")
                print ("SE PRESENTÓ UN ERROR: El salario no puede ser negativo ***")
    def test6_semanastrabajas_cero(self):
        salario=2000000
        semanas_trabajadas=0
        try: 
            resultado = Liquida_nomina1.CalcularLiquidacion(salario, semanas_trabajadas)
            print(resultado)
        except Exception:
            print("\n * * * * * * * * * * * * * * * * ")
            print("*** SE PRESENTÓ UN ERROR: Las semanas deben ser un numero mayor a cero***")
            
    def test7_horas_extras_diurnas_negativas(self):
        salario=1300000
        semanas_trabajadas=4
        Horas_Extras_Diu =-3
        try: 
            resultado = Liquida_nomina1.CalcularLiquidacion(salario, semanas_trabajadas, Horas_Extras_Diu)
            print(resultado)
        except Exception:
            print("\n * * * * * * * * * * * * * * * * ")
            print("*** SE PRESENTÓ UN ERROR: Las horas extras diurnas no pueden ser negativas***")

    def test_liquidacion_festivo_mas_de_8h(self):
        try:
            resultado = Liquida_nomina1.CalcularLiquidacion(salario= 3000000, semanas_trabajadas=4, tiempo_festivo_lab=10, 
                                        Horas_Extras_Diu=5, Horas_Extras_Noc=3, Horas_Extras_Fes=2, 
                                        dias_incapacidad=5)
            print(resultado)
        except Exception:
            print("\n * * * * * * * * * * * * * * * * ")
            print("*** SE PRESENTÓ UN ERROR: Las horas laboradas en festivo no puede ser mayor a 8 horas.***")
     
    def test_liquidacion_error_dias_incapacidad_negativos(self):
            try:
                resultado = Liquida_nomina1.CalcularLiquidacion(salario=3000000, semanas_trabajadas=4, tiempo_festivo_lab=6, 
                                Horas_Extras_Diu=5, Horas_Extras_Noc=3, 
                                dias_incapacidad=-5)
                print(resultado)
            except Exception:
                print("\n * * * * * * * * * * * * * * * * ")
                print("*** SE PRESENTÓ UN ERROR: Los dias de incapacidad no pueden ser negativos.***")
                
            
    def test_liquidacion_error_salario_no_numerico(self):
        try:
            resultado= Liquida_nomina1.CalcularLiquidacion(salario="tres millones", semanas_trabajadas=7,  tiempo_festivo_lab=10, 
                                Horas_Extras_Diu=5, Horas_Extras_Noc=3, Horas_Extras_Fes=2, 
                                dias_incapacidad=5)
            print(resultado)
        except Exception:
            print("\n * * * * * * * * * * * * * * * * ")
            print("*** SE PRESENTÓ UN ERROR: Solo se permiten valores númericos en los campos. (Salario)***")
            

    def test_liquidacion_error_horas_extras_no_numerico(self):
        try:
            resultado = Liquida_nomina1.CalcularLiquidacion(salario=3000000, semanas_trabajadas=4 , tiempo_festivo_lab=10, 
                                Horas_Extras_Diu="cinco", Horas_Extras_Noc=3, Horas_Extras_Fes=2, dias_incapacidad=5)
            print(resultado)
        except Exception:
            print("\n * * * * * * * * * * * * * * * * ")
            print("*** SE PRESENTÓ UN ERROR: Solo se permiten valores numéricos en los campos.(Horas extras)***")
    
    def test_liquidacion_error_tiempo_festivo_negativo(self):
        try:
            Liquida_nomina1.CalcularLiquidacion(salario=3000000, semanas_trabajadas=4, tiempo_festivo_lab=-10, 
                                Horas_Extras_Diu=5, Horas_Extras_Noc=3, Horas_Extras_Fes=2, 
                                dias_incapacidad=5)
        except Exception:
            print("\n * * * * * * * * * * * * * * * * ")
            print("*** SE PRESENTÓ UN ERROR: Las hors laboradas en festivos no pueden ser valores negativos.***")
            


if __name__ == '__main__':
    unittest.main()
