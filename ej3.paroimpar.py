"""
Programa: ej3.numeroparoimpar.py
Autora: Virginia Ordoño Bernier
Fecha:17/10/2020

Propósito: Crear un algoritmo que al pedir un número indique si es par o impar.

Análisis:
- Pedimos al usuario un número.
- Dividimos la variable por dos para saber si el resto es 0. En ese caso aparece un mensaje de el número es par.
- Si no, aparace el mensaje: el número es impar.
- Variable: number.
- Secuencias: if, else.
"""

print('Escribe un número y el programa te dirá si es par o impar.')

# Mediante input solicitamos un número.
number = int(input('Dime un número: '))

# If para establecer si la diferencia de la división es 0.
if number % 2 == 0:
    print('El número', number, 'es un número par.')
else:
    print('El número', number, 'es un número impar.')
