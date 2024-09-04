# Calculadora de Nómina

## ¿Quién hizo esto?

**Autores**:
- Steven Oviedo
- Valentina Morales

## ¿Qué es y para qué es?

Este proyecto es una aplicación que calcula el total a pagar de una empresa a un empleado. Este pago corresponde a la diferencia entre los valores devengados y las deducciones de ley que aplican al salario del trabajador.

## ¿Cómo lo hago funcionar?
### Prerrequisito
Asegurese de eten4r Python instalado en su sistema. No hay dependencias externas para correr el proyecto.4

### Ejecución
Para correr el programa por fuera del entorno de desarrollo :
1. Navegar a la carpeta: una vez que hayas clonado el archivo, abre el símbolo del sistema (cmd) y navega a la carpeta donde guardaste el archivo, por ejemplo:
   ```bash
   cd C:\Users\Usuario\OneDrive\Documentos\U\Sexto Semestre\Código limpio\Clean-Code-1\src\Console
   ``` 
2. Ejecuta el script principal: <br>
   ```bash
   src\Console
   ```

## ¿Cómo está hecho?
### Arquitectura del proyecto
El proyecto está organizado en dos carpetas principales:

- **src**: Contiene el código fuente de la aplicación.
   - **console**: Contiene el script principal `Console.py` para la interacción del usuario.
   - **logic**: Contiene la lógica para el cálculo de la hipoteca inversa (`rLiquida_nomina1.py`).
- **tests**: Contiene pruebas unitarias para validar la funcionalidad del código.

### Organización del módulo
- `src\Console\Console.py`: archivo principal para la interacción del usuario. Recopila las entradas del usuario y muestra los resultados.
- `src\LiquidacionNomina\Liquida_nomina1.py`: contiene las funciones lógicas para el cálculo de la nomina, incluida la validación de las entradas y el cálculo del pago.

### Dependencias
- `unittest`: biblioteca estándar de Python para pruebas unitarias.

## Uso
Para ejecutar las pruebas unitarias desde la carpeta `test`, utilice el siguiente comando:

```bash
python Test/Liqui_test.py

Para ejecutar el archivo principal:
python src\Console\Console.py
```
   







