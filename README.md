1) ¿Quién hizo esto?
Lista de autores (no ponga email, telefonos, nada de informacion privada)

2) ¿Qué es y para qué es?
Describir el propósito del proyecto

3) ¿Cómo lo hago funcionar?
Prerrequisitos: que se debe hacer o tener antes de poder correr este proyecto
Ejecución: como hacemos correr el programa, POR FUERA DEL ENTORNO DE DESARROLLO

4) ¿Cómo está hecho?
Describir la arquitectura del proyecto, bibliotecas usadas, dependencias de otros proyectos
Y la organización de los módulos (que hay en cada carpeta)
-----------------------------------------------------------------------------------------------------

Estructura sugerida
Carpeta src: Codigo fuente de la logica de la aplicación. Tiene subcarpetas por cada capa de la aplicacion
Carpeta tests: Pruebas Unitarias
Recuerde que cada carpeta de código fuente debe contener un archivo __init.py que permite que python reconozca la carpeta como un Módulo y pueda hacer import

Uso
Para ejecutar las pruebas unitarias, desde la carpeta src, use el comando

cleancode-01\src> python -m unittest discover ..\tests -p '*test*.py' Para poder ejecutarlas desde la carpeta raiz, debe indicar la ruta de busqueda donde se encuentran los módulos, incluyendo las siguientes lineas al inicio del módulo de pruebas

import sys sys.path.append("src")
