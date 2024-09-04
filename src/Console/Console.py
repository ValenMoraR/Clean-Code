import sys
sys.path.append("src")
from LiquidacionNomina import Liquida_nomina1

def validar_vacios(valor):
    return valor if valor else "0"

print("<<< PROGRAMA EN EJECUCUION >>>")
print("::::::::::::::::::::::::::::::::")
print("**NOTA: Para los datos que no aplique su perfil por favor dejar vacío, solo presione ENTER y continue con el siguiente dato")
print("----------------------------------------------------------------------")
salario_mensual= validar_vacios(input("Ingrese el valor su ingreso mensual ($COP):"))
semanas_trabajadas= validar_vacios(input("Ingrese el valor de las SEMANAS trabajadas a liquidar :"))
tiempo_festivo_laborado = validar_vacios(input("Ingrese las horas trabajadas en festivo (SOLO SI APLICA):"))
horas_extras_diurnas = validar_vacios(input("Ingrese las horas extras diurnas trabajadas (SOLO SI APLICA):"))
horas_extras_nocturnas = validar_vacios(input("Ingrese las horas extras nocturnas trabajadas (SOLO SI APLICA):"))
horas_extras_festivos = validar_vacios(input("Ingrese las horas extras trabajadas en día festivo (SOLO SI APLICA):"))
dias_licencia = validar_vacios(input("Ingrese los días que tuvo de licencia en el periodo laborado (SOLO SI APLICA):"))
dias_incapacidad = validar_vacios(input("Si tuvo incapacidad en el periodo laborado, ingrese los días, (SOLO SI APLICA):"))

try:
    resultado= Liquida_nomina1.CalcularLiquidacion(salario_mensual, semanas_trabajadas,  tiempo_festivo_laborado, 
                                horas_extras_diurnas, horas_extras_nocturnas, horas_extras_festivos, dias_licencia,
                                dias_incapacidad)
    print(f"El valor total a su liquidación es de : {resultado}")
except Exception as up_error:
    print("****HUBO UN ERROR***")
    print(str(up_error))
