"""
Programa: ej1.numeromayorqueotro.py
Autora: Virginia Ordoño Bernier
Fecha:17/10/2020

Propósito:
Crear un algoritmo que al pedir dos números indique si el primero es mayor que el segundo o no.

Análisis:
- Pedir dos números al usuario y compararlos.
- Si el número 1 es mayor, aparece mensaje indicando que es mayor.
- Si no se cumple, aparece mensaje indicando que no es mayor.
- Variables: number1, number2.
- Sentencias: if, else.
"""

print('Escribe dos número y a continuación el programa te dirá si el primero es mayor que el segundo o no.')

# Mediante input solicitamos los dos números.
number1 = (input('Escribe el primer número: '))
number2 = (input('Escribe otro número: '))

# Usamos tres estructuras alternativas if, para los tres posibles casos que se nos puedan dar.
if number1 > number2:
    print(number1, 'es mayor que', number2, '.')
else:
    print(number1, 'no es mayor que', number2, '.')
