"""
Programa: ej5.quienesmasjoven.py
Fecha:24/10/2020
Autora: Virginia Ordoño Bernier

Propósito:
Crear un programa que lea la edad de dos personas y diga quién es más joven, teniendo en cuenta que ambas
pueden tener la misma edad. En tal caso, hacerlo saber con un mensaje adecuado.

Análisis:
- Pedimos al usuario dos edades y las comparamos.
- Si la primera es mayor, aparece un mensaje indicándolo.
- Si la primera es menor, aparece un mensaje indicándolo.
- En caso contrario, aparece un mensaje indicando que la edad es la misma.
- Variables: age1, age2.
- Sentencias: if, elif, else.
"""

print('Escribe la edad de dos personas para que el programa determine cuál de ellas es mayor.')

# Mediante la función input pedimos al usuario la edad de las dos personas.
age1 = input('Escribe la edad de la primera persona: ')
age2 = input('Escribe la edad de la segunda persona: ')

if age1 > age2:
    print('La primera persona es mayor que la segunda.')
elif age1 < age2:
    print('La segunda personas es mayor que la primera.')
else:
    print('Las dos personas tienen la misma edad.')
