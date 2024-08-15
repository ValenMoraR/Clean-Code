import re

def CalcularLiquidacion(salario: float, semanas_trabajadas: int,
                        tiempo_festivo_lab: float = 0, Horas_Extras_Diu: float = 0,
                        Horas_Extras_Noc: float = 0, Horas_Extras_Fes: float = 0, 
                        dias_incapacidad: int = 0, porcentaje_incapacidad: float = 0.66):
    """
    Calcula la liquidación de nómina básica en Colombia.
    ----------------------------------------------------
    salario: Salario base mensual del empleado.
    semanas_trabajadas: Semanas laboradas durante el período.
    auxilio_transporte: Auxilio de transporte mensual (si aplica).Solo si SALARIO <= 2 SMLMV (2.600.000)
    tiempo_festivo_lab: Tiempo trabajado en festivos (que no son extras).
    Horas_Extras_Diu: Horas extras diurnas.
    Horas_Extras_Noc: Horas extras nocturnas.
    Horas_Extras_Fes: Horas extras en festivos.
    deduccion_salud: Aporte del empleado a salud (4% del salario)
    deduccion_pension: Aporte del empleado a pensión (4% del salario)
    deduccion_fondo_solidario: Aporte al fondo de solidaridad (solo si salario > 4 SMLMV)
    deduccion_incapacidades: Valor por incapacidades descontadas del salario
    dias_incapacidad: Días de incapacidad.
    porcentaje_incapacidad: Porcentaje del salario que se paga durante la incapacidad.
    
    """

    # Validaciones básicas
    if any(x < 0 for x in [salario, semanas_trabajadas, tiempo_festivo_lab,
                           Horas_Extras_Diu, Horas_Extras_Noc, Horas_Extras_Fes, dias_incapacidad, porcentaje_incapacidad]):
        raise ValueError("Los valores no pueden ser negativos.")
    
    semanas_trabajadas = int(semanas_trabajadas)
    dias_trabajados = semanas_trabajadas * 7  # Convertir semanas a días trabajados

    # Validación del tipo de dato
    if not all(isinstance(x, (int, float)) for x in [salario, semanas_trabajadas,
                                                     tiempo_festivo_lab, Horas_Extras_Diu, 
                                                     Horas_Extras_Noc, Horas_Extras_Fes, dias_incapacidad, porcentaje_incapacidad]):
        raise ValueError("Todos los valores deben ser numéricos.")

    # Cálculos iniciales
    auxilio_transporte = 162000 if salario <= 2600000 else 0
    valor_dia = salario / 30
    valor_hora = valor_dia / 8

    # Cálculo de pagos adicionales
    valor_festivo = tiempo_festivo_lab * valor_hora * 1.75  # Tiempo normal en festivos
    valor_extras_diurnas = Horas_Extras_Diu * valor_hora * 1.25
    valor_extras_nocturnas = Horas_Extras_Noc * valor_hora * 1.75
    valor_extras_festivas = Horas_Extras_Fes * valor_hora * 2

    # Ingresos Totales
    total_pagos = (valor_dia * dias_trabajados) + auxilio_transporte + valor_festivo + \
                  valor_extras_diurnas + valor_extras_nocturnas + valor_extras_festivas

    # Deducciones

    salud = total_pagos * 0.04
    pension = total_pagos * 0.04
    fondo_solidario = total_pagos * 0.01 if salario > 4000000 else 0
    licencias = 0
    retencion_fuente = total_pagos *0.05 if salario > 4300000 else 0

    # Cálculo de deducción por incapacidad
    deduccion_incapacidad = dias_incapacidad * valor_dia * 0.333

    # Valor total a recibir
    liquidacion_total = total_pagos - (salud + pension + fondo_solidario + deduccion_incapacidad + 
                                       licencias + retencion_fuente)

    return round(liquidacion_total, 2)

# # Ejemplo de uso
# salario = 3000000
# semanas_trabajadas = 4
# auxilio_transporte = 140606
# tiempo_festivo_lab = 10
# Horas_Extras_Diu = 5
# Horas_Extras_Noc = 3
# Horas_Extras_Fes = 2
# dias_incapacidad = 5
# porcentaje_incapacidad = 0.66  # 66% del salario diario

# resultado = CalcularLiquidacion(salario, semanas_trabajadas, auxilio_transporte, tiempo_festivo_lab, 
#                                 Horas_Extras_Diu, Horas_Extras_Noc, Horas_Extras_Fes, 
#                                 dias_incapacidad, porcentaje_incapacidad)
# print(f"La liquidación total es: {resultado} COP")
