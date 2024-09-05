1) ¿Quién hizo esto?
Steven David Oviedo Herrera
Valentina Morales Restrepo 

2) ¿Qué es y para qué es? #Describir el propósito del proyecto 
Es una aplicación que calcula el total a pagar de una empresa a un empleado.
Este pago corresponde a la diferencia entre los valores devengados y las deducciones de ley que le aplican.

3) ¿Cómo lo hago funcionar?
Prerrequisitos: que se debe hacer o tener antes de poder correr este proyecto
Ejecución: como hacemos correr el programa, POR FUERA DEL ENTORNO DE DESARROLLO

4) ¿Cómo está hecho?
Describir la arquitectura del proyecto, bibliotecas usadas, dependencias de otros proyectos
Y la organización de los módulos (que hay en cada carpeta)
Este proyecto usa modulo como:
re: Este módulo proporciona operaciones de coincidencia de expresiones regulares 

Carpetas y archivos:
1) scr: En esta carpeta podemos encontrar otras dos.
    a. Console: Esta carpeta contiene el archivo con el ejecutable de la consola
    b. LiquidaciónNomina: Esa carpeta contiene la lógica base del proyecto

2) Test: En esta carpeta se encuetra el archivo que se encarga de correr las pruebas de error, extraordinarias y excepciones que tiene el código. 


-----------------------------------------------------------------------------------------------------

Estructura sugerida
Carpeta src: Codigo fuente de la logica de la aplicación. Tiene subcarpetas por cada capa de la aplicacion
Carpeta tests: Pruebas Unitarias
Recuerde que cada carpeta de código fuente debe contener un archivo __init.py que permite que python reconozca la carpeta como un Módulo y pueda hacer import

Uso
Para ejecutar las pruebas unitarias, desde la carpeta src, use el comando

cleancode-01\src> python -m unittest discover ..\tests -p '*test*.py' Para poder ejecutarlas desde la carpeta raiz, debe indicar la ruta de busqueda donde se encuentran los módulos, incluyendo las siguientes lineas al inicio del módulo de pruebas

import sys sys.path.append("src")
