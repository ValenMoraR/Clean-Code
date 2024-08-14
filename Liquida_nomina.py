import re

def CalcularLiquidacion(salario: float, dias_trabajados: int, auxilio_transporte: float = 0):
    """
    Calcula la liquidación de nómina básica en Colombia.
    ----------------------------------------------
    salario: Salario base mensual del empleado
    dias_trabajados: Días laborados durante el período
    auxilio_transporte: Auxilio de transporte mensual (opcional)
    """
    
    # Validación de entrada
    patron = '^[0-9.]+$'
    if all(re.match(patron, str(var)) for var in [salario, dias_trabajados, auxilio_transporte]):
        salario = float(salario)
        dias_trabajados = int(dias_trabajados)
        auxilio_transporte = float(auxilio_transporte)
    else:
        raise Exception("ERROR: Los valores ingresados solo pueden contener números")

    if salario <= 0 or dias_trabajados < 0 or auxilio_transporte < 0:
        raise Exception("VALOR INVÁLIDO: Los valores ingresados deben ser positivos")
    if dias_trabajados > 360:
        raise Exception("VALOR INVÁLIDO: Los días trabajados no pueden superar 360 días")

    # Cálculo de salario proporcional
    salario_diario = salario / 30
    salario_proporcional = salario_diario * dias_trabajados
    
    # Cálculo de prestaciones sociales
    prima = salario_proporcional * dias_trabajados / 360
    cesantias = salario_proporcional * dias_trabajados / 360
    intereses_cesantias = cesantias * 0.12
    vacaciones = salario_proporcional * dias_trabajados / 720

    liquidacion_total = salario_proporcional + auxilio_transporte + prima + cesantias + intereses_cesantias + vacaciones

   
    return(liquidacion_total)
         # Cálculo total
            
    
        # 'Salario Proporcional': salario_proporcional,
        # 'Auxilio Transporte': auxilio_transporte,
        # 'Prima': prima,
        # 'Cesantías': cesantias,
        # 'Intereses Cesantías': intereses_cesantias,
        # 'Vacaciones': vacaciones,
        # 'Liquidación Total': liquidacion_total

# Ejemplo de uso:
# salario = 2000000  # Salario base mensual en COP
# dias_trabajados = 180  # Días laborados
# auxilio_transporte = 140606  # Auxilio de transporte mensual

# resultado = CalcularLiquidacion(salario, dias_trabajados, auxilio_transporte)
# for clave, valor in resultado.items():
#     print(f'{clave}: {valor:.2f} COP')
