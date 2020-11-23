"""
Programa: ej17.carasdeundado.py
Fecha:25/10/2020
Autora: Virginia Ordoño

Propósito: Realiza un programa que pida por teclado el resultado (dato entero) obtenido al lanzar un dado de seis caras
y muestre por pantalla el número en letras (dato cadena) de la cara opuesta al resultado obtenido.

Análisis:
- Pedimos al usuario el número de la cara del dado.
- Si el valor introducido está entre 1 y 6, restamos ese número a 7 y el resultado es el otro lado de la cara.
- En caso contrario, aparece un mensaje de error.
- Variables: number.
- Secuencias: if, else.
"""

number = int(input('Introduce el número del dado correspondiente para que el programa te diga la cara opuesta: '))

if number in (1, 2, 3, 4, 5, 6):
    side = 7 - number
    print ('Es el número del lado opuesto es el', (side),'.' )
else:
    print ('El valor introducido no es correcto. Por favor, inténtalo de nuevo.')