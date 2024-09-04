import re
# Exepcion personalizada que se usa en un caso de error particular
class ValorNegativo( Exception ): 
    pass
class ValorInvalido( Exception ): 
    pass
class SemanaCero( Exception ): 
    pass
class MasDe8HorasFestivoLaboradas( Exception ): 
    pass
class ValorNoEntero ( Exception):
    pass
class ComaSeparador (Exception):
    pass

def CalcularLiquidacion(salario_mensual, semanas_trabajadas,
                        tiempo_festivo_laborado=0, horas_extras_diurnas=0,
                        horas_extras_nocturnas=0, horas_extras_festivos=0,
                        dias_licencia=0 ,dias_incapacidad=0):
    """    
    Calcula la liquidación de nómina para empleados en Colombia.
    ----------------------------------------------------
    salario_mensual: Salario base mensual del empleado.
    semanas_trabajadas: Semanas laboradas durante el período.
    auxilio_transporte: Auxilio de transporte mensual (si aplica).Solo si salario_mensual <= 2 SMLMV (2.600.000)
    tiempo_festivo_lab: Tiempo trabajado en festivos (que no son extras).
    Horas_Extras_Diu: Horas extras diurnas.
    Horas_Extras_Noc: Horas extras nocturnas.
    Horas_Extras_Fes: Horas extras en festivos.
    deduccion_salud: Aporte del empleado a salud (4%)
    deduccion_pension: Aporte del empleado a pensión (4%)
    deduccion_fondo_solidario: Aporte al fondo de solidaridad (solo si salario_mensual > 4 SMLMV)
    dias_incapacidad: Días de incapacidad.
    dias_licencia: Dias de licencia remunerada
    
    """
    # Lista de variables y nombres descriptivos
    variables = [
        (salario_mensual, 'Salario mensual', True),
        (semanas_trabajadas, 'Semanas trabajadas', False),
        (tiempo_festivo_laborado, 'Tiempo festivo trabajado', False),
        (horas_extras_diurnas, 'Horas extras diurnas', False),
        (horas_extras_nocturnas, 'Horas extras nocturnas', False),
        (horas_extras_festivos, 'Horas extras en festivos', False),
        (dias_incapacidad, 'Días de incapacidad', True),
        (dias_licencia, 'Días de licencia', True)
    ]

    variables_convertidas  = []

    # Validar cada variable
    for entrada, nombre_variable, entero in variables:
        try:
            # Verificar si la entrada contiene una coma como separador decimal
            if ',' in entrada:
                raise ComaSeparador(f"ERROR: Dato inválido en {nombre_variable}: Use un punto (.) como separador decimal, no una coma (,).")

            # Convertir a número flotante para asegurar que es numérico
            valor = float(entrada)

            # Si debe ser entero, verificar que no tenga decimales
            if entero and float(entrada) != int(float(entrada)):
                raise ValorNoEntero(f"ERROR: Dato inválido en {nombre_variable}: Se esperaba un número entero.")


            # Verificar si es negativo
            if valor < 0:
                raise ValorNegativo(f"ERROR: Dato inválido en {nombre_variable}: Los números no pueden ser negativos.")
            
            # Convertir a entero si debe serlo
            valor = int(valor) if entero else valor
            
            # Agregar la variable convertida a la lista
            variables_convertidas.append((valor, nombre_variable, entero))

        except ValueError:
            # Si la conversión a float también falla, es porque hay caracteres no numéricos
            raise ValorInvalido(f"ERROR: Dato inválido en {nombre_variable}: Asegúrese de que sea un número numérico, no negativo y sin letras o caracteres especiales.")

    # Desempaquetar las variables convertidas
    salario_mensual = variables_convertidas[0][0]
    semanas_trabajadas = variables_convertidas[1][0]
    tiempo_festivo_laborado = variables_convertidas[2][0]
    horas_extras_diurnas = variables_convertidas[3][0]
    horas_extras_nocturnas = variables_convertidas[4][0]
    horas_extras_festivos = variables_convertidas[5][0]
    dias_incapacidad = variables_convertidas[6][0]
    dias_licencia = variables_convertidas[7][0]
                          
    # Declaracion de constantes
    TOTAL_DIAS_DEL_MES = 30
    HORAS_DIARIAS_TRABAJADAS = 8
    MAXIMO_SALARIO_CON_AUXILIO_TRANSPORTE = 2600000
    TOTAL_DIAS_A_LA_SEMANA = 6
    VALOR_POR_HORA_TRABAJADA_FESTIVO = 1.75
    VALOR_POR_HORA_EXTRA_TRABAJADA_DIURNA = 1.25
    VALOR_POR_HORA_EXTRA_TRABAJADA_NOCTURNA = 1.75
    VALOR_POR_HORA_EXTRA_TRABAJADA_FESTIVO = 2
    PORCENTAJE_A_RESTAR_POR_SALUD = 0.04
    PORCENTAJE_A_RESTAR_POR_PENSION = 0.04
    PORCENTAJE_A_RESTAR_POR_FONDO = 0.01
    SALARIO_A_RESTAR_FONDO = 4000000
    PORCENTAJE_A_RESTAR_POR_RETENCION = 0.05
    SALARIO_A_RESTAR_RETENCION = 4300000
    PORCENTAJE_A_RESTAR_POR_INCAPACIDAD = 0.333

    if semanas_trabajadas == 0:
        raise SemanaCero("VALOR INVÁLIDO:Las semanas trabajadas deben ser un numero mayor o igual a 1.")
    
    if tiempo_festivo_laborado > HORAS_DIARIAS_TRABAJADAS:
        raise MasDe8HorasFestivoLaboradas("VALOR INVÁLIDO: El timepo festivo laborado no piede ser mayor a 8 horas.")
    
    dias_trabajados = semanas_trabajadas *  TOTAL_DIAS_A_LA_SEMANA# Convertir semanas a días trabajados

    # Cálculos iniciales
    auxilio_transporte = 162000 if salario_mensual <= MAXIMO_SALARIO_CON_AUXILIO_TRANSPORTE else 0
    salario_diario = salario_mensual / TOTAL_DIAS_DEL_MES

    salario_hora = salario_diario / HORAS_DIARIAS_TRABAJADAS
    # Cálculo de pagos adicionales
    ganacias_por_festivo = tiempo_festivo_laborado * salario_hora * VALOR_POR_HORA_TRABAJADA_FESTIVO 
    ganancias_por_extras_diurnas = horas_extras_diurnas * salario_hora * VALOR_POR_HORA_EXTRA_TRABAJADA_DIURNA
    ganancias_por_extras_nocturnas = horas_extras_nocturnas * salario_hora * VALOR_POR_HORA_EXTRA_TRABAJADA_NOCTURNA
    ganacias_por_extras_festivas = horas_extras_festivos * salario_hora * VALOR_POR_HORA_EXTRA_TRABAJADA_FESTIVO

    # Ingresos Totales
    total_ingresos = (salario_diario * dias_trabajados) + auxilio_transporte + ganacias_por_festivo + \
                  ganancias_por_extras_diurnas + ganancias_por_extras_nocturnas + ganacias_por_extras_festivas
          
    # Deducciones
    salud = total_ingresos * PORCENTAJE_A_RESTAR_POR_SALUD
    pension = total_ingresos * PORCENTAJE_A_RESTAR_POR_PENSION
    fondo_solidario = total_ingresos * PORCENTAJE_A_RESTAR_POR_FONDO if salario_mensual > SALARIO_A_RESTAR_FONDO else 0
    pago_por_licencia = dias_licencia * salario_diario
    retencion_fuente = total_ingresos *PORCENTAJE_A_RESTAR_POR_RETENCION if salario_mensual > SALARIO_A_RESTAR_RETENCION else 0
    deduccion_incapacidad = dias_incapacidad * salario_diario * PORCENTAJE_A_RESTAR_POR_INCAPACIDAD

    # Valor total a recibir
    liquidacion_total = total_ingresos - (salud + pension + fondo_solidario + deduccion_incapacidad + 
                                       pago_por_licencia + retencion_fuente)
    
    return (round(liquidacion_total, 2))
