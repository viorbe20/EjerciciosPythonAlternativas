"""Programa: ej19.mescorrespondiente.py
Fecha:25/10/2020
Autora: Virginia Ordoño

Propósito: Escribe un programa que pida un número entero entre uno y doce e imprima el número de días
 que tiene el mes correspondiente.

Análisis:
- Pedimos al usuario que escriba el número correspondiente al mes.
- Si número está en la lista, indicará el número de días que tiene.
- Variables: number.
- Sentencias: if, elif.

"""

number = input('Escribe un número entre el 1 y el 12 del mes correspondiente para que el programa te diga '
               'los días que tiene ese mes.')

# Si el número es uno de la lista, aparecerá un mensaje indicando que tiene 31 días.
if number in (1, 3, 5, 7, 8, 10, 12):
    print('El mes tiene 31 días.')

# Si el número es uno de la lista, aparecerá un mensaje indicando que tiene 30 días.
elif number in (4, 6, 9, 11):
    print('El mes tiene 30 días.')

# Si el número es el dos, aparecerá un mensaje indicando que tiene 28 días.
elif number == 2:
    print('El mes tiene 28 días.')
