import re

def CalcularLiquidacion(salario, semanas_trabajadas,
                        tiempo_festivo_lab=0, Horas_Extras_Diu=0,
                        Horas_Extras_Noc=0, Horas_Extras_Fes=0,
                        dias_licencia=0 ,dias_incapacidad=0):
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
    dias_licencia: Dias de licencia remunerada que puede variar entre:
        - 5 días hábiles para licencias por luto y matrimonio.
        - 14 días calendario para la licencia de paternidad.
        - 126 días para la licencia de maternidad o adopción
    
    """

    # Asegúrate de que todas las entradas sean cadenas antes de la validación
    variables = [str(salario), str(semanas_trabajadas), str(tiempo_festivo_lab),
                 str(Horas_Extras_Diu), str(Horas_Extras_Noc), 
                 str(Horas_Extras_Fes), str(dias_incapacidad),str(dias_licencia)]

    patron = r'^\d+(\.\d+)?$'  # Patrón para números y decimales
    
    # Verificar si todas las cadenas contienen solo números y puntos
    if all(re.match(patron, var) for var in variables):
        # Convertir los valores a sus tipos numéricos correspondientes
        salario = float(salario)
        tiempo_festivo_lab = float(tiempo_festivo_lab)
        semanas_trabajadas = int(semanas_trabajadas)
        Horas_Extras_Diu = float(Horas_Extras_Diu)
        Horas_Extras_Noc = float(Horas_Extras_Noc)
        Horas_Extras_Fes = float(Horas_Extras_Fes)
        dias_incapacidad = int(dias_incapacidad)
        dias_licencia = int(dias_licencia)
    else:
        raise Exception("ERROR: Los valores ingresados solo pueden contener números y puntos.")

    #Validaciones básicas
    if any(x < 0 for x in [salario, semanas_trabajadas, tiempo_festivo_lab,
                           Horas_Extras_Diu, Horas_Extras_Noc, Horas_Extras_Fes, dias_incapacidad,dias_licencia]):
        raise Exception("VALOR INVÁLIDO: Los valores No pueden ser negativos.")

    # Validación del tipo de dato
    if not all(isinstance(x, (int, float)) for x in [salario, semanas_trabajadas,
                                                     tiempo_festivo_lab, Horas_Extras_Diu, 
                                                     Horas_Extras_Noc, Horas_Extras_Fes, dias_incapacidad,dias_licencia]):
        raise Exception("VALOR INVÁLIDO: Los valores deben ser numéricos.")
    
    if semanas_trabajadas < 1:
        raise Exception("VALOR INVÁLIDO:Las semanas trabajadas deben ser un numero mayor o igual a 1.")
    
    if tiempo_festivo_lab >8:
        raise Exception("VALOR INVÁLIDO: El timepo festivo laborado no piede ser mayor a 8 horas.")
   
    semanas_trabajadas = int(semanas_trabajadas)
    dias_trabajados = semanas_trabajadas * 6  # Convertir semanas a días trabajados

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
    valor_licencia = dias_licencia * valor_dia if dias_licencia > 4 else 0
    retencion_fuente = total_pagos *0.05 if salario > 4300000 else 0

    # Cálculo de deducción por incapacidad
    deduccion_incapacidad = dias_incapacidad * valor_dia * 0.333

    # Valor total a recibir
    liquidacion_total = total_pagos - (salud + pension + fondo_solidario + deduccion_incapacidad + 
                                       valor_licencia + retencion_fuente)
    
    
    print("------------------------------------------------")
    print(f"Salarios: Mensual:${salario}, Diario: ${valor_dia:.2f} , Hora: ${valor_hora:.2f}") 
    print(f"Tiempo laborado -> Semanas: {semanas_trabajadas}, Días: {dias_trabajados}")
    if dias_incapacidad != 0 :
        print(f"Dias de incapacidad: {dias_incapacidad}")
    print("<<< DATOS DEVENGADOS >>>") 
    if auxilio_transporte != 0:
        print(F"Auxilio de transporte: ${auxilio_transporte}")
    else:
        print(F"Auxilio de transporte: NO APLICA")
    print(f"Valor laborado en festivo: ${valor_festivo:.2f} | Valor de horas extras -> Diurnas: ${valor_extras_diurnas:.2f}, Nocturnas: ${valor_extras_nocturnas:.2f}, Festivo: ${valor_extras_festivas:.2f} ")
    print(f"Total devengados: ${total_pagos:.2f}")
    print("<<< DATOS DEDUCIDOS >>>") 
    print(f"Valor aporte pensión: ${pension:.2f}, Valor aporte salud: ${salud:.2f}, Valor aporte fondo solidario: ${fondo_solidario:.2f}")
    print(f"Valor incapacidades: ${deduccion_incapacidad:.2f} , Valor por licencia: ${valor_licencia:.2f}, Valor por retención de fuente: ${retencion_fuente:.2f}")
    print(f"La liquidación de nomina total es: ${liquidacion_total:.2f} COP")

    return (round(liquidacion_total, 2))
