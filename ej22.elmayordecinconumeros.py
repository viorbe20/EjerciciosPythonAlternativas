"""Programa: ej21.elmayrodetresnumeros.py
Fecha:25/10/2020
Autora: Virginia Ordoño

Propósito: Realiza un programa que pida tres números enteros y diga cuál es el mayor.

Análisis:
- Pedimos al usuario 5 números.
- Comparamos los números y establecemos cuál es el mayor.
- Variables: number1, number2, number3, number4, number5.
- Sentencias: if.
"""

print('Introduce 5 números para que el programa te diga cuál es el mayor.')

number1 = input('Escribe un número: ')
number2 = input('Escribe un segundo número: ')
number3 = input('Escribe un tercer número: ')
number4 = input('Escribe un cuarto número: ')
number5 = input('Escribe un quinto número: ')

# Si el primer número es mayor que los otros, aparece un mensaje indicándolo.
if number2 < number1 > number3 and number4 < number1 > number5:
    print('El número', number1, 'es el mayor de los cinco.')

# Si el segundo número es mayor que los otros, aparece un mensaje indicándolo.
if number1 < number2 > number3 and number4 < number2 > number5:
    print('El número', number2, 'es el mayor de los cinco.')

# Si el tercer número es mayor que los otros, aparece un mensaje indicándolo.
if number2 < number3 > number1 and number4 < number3 > number5:
    print('El número', number3, 'es el mayor de los cinco.')

# Si el cuarto número es mayor que los otros, aparece un mensaje indicándolo.
if number1 < number4 > number2 and number3 < number4 > number5:
    print('El número', number4, 'es el mayor de los cinco.')

# Si el quinto número es mayor que los otros, aparece un mensaje indicándolo.
if number1 < number5 > number2 and number3 < number5 > number4:
    print('El número', number5, 'es el mayor de los cinco.')
