"""
Programa: ej21.elmayrodetresnumeros.py
Fecha:25/10/2020
Autora: Virginia Ordoño

Propósito: Realiza un programa que pida tres números enteros y diga cuál es el mayor.

Análisis:
- Pedimos al usuario 3 números.
- Comparamos los números y establecemos cuál es el mayor.
- Variables: number1, number2, number3.
- Sentencias: if.
"""

print('Introduce 3 números para que el programa te diga cuál es el mayor.')

number1 = input('Escribe un número: ')
number2 = input('Escribe un segundo número: ')
number3 = input('Escribe un tercer número: ')

# Si el primer número es mayor que los otros dos, aparece un mensaje indicándolo.
if number2 < number1 > number3:
    print('El número', number1, 'es el mayor de los tres.')

# Si el segundo número es mayor que los otros dos, aparece un mensaje indicándolo.
if number1 < number2 > number3:
    print('El número', number2, 'es el mayor de los tres.')

# Si el tercer número es mayor que los otros dos, aparece un mensaje indicándolo.
if number2 < number3 > number1:
    print('El número', number3, 'es el mayor de los tres.')
