"""
Programa: ej12.añobisiesto.py
Fecha:24/10/2020
Autora: Virginia Ordoño

Propósito:
Programa que lea un año e indique si es  bisiesto. Nota: un año es bisiesto sí es un número
divisible por 4, pero no si es divisible por 100, excepto que también sea divisible por 400.

Análisis:
- Pedimos al usuario el año.
- Si es divisible por 4, pero no si es divisible por 100, excepto que también sea divisible por 400 aparece un mensaje
indicando que es bisiesto.
- En caso contrario, aparece un mensaje indicando que no es bisiesto.
- Variables: year.
- Sentencias: if, else.
"""

print('A continuación el programa te pidará que escribas un año y determinará si se trata o no de un año bisiesto.')

# Mediante la función input pedimos al usuario que introduzca el año.
year = int(input('Escribe un año para que el programa determine si se trata o no de un año bisiesto.'))

# Mediante la sentencia if pedimos establecemos aquellos años que son divisibles por 4, que no lo son por 100 pero que
# son por 400 para deteminar que son bisiestos.
if year % 4 == 0 or not year % 100 == 0 or year % 400 == 0:
    print('Es un año bisiesto.')

# Con else establecemos que con el resto de resultados obtenemos años no bisiestos.
else:
    print('No es un año bisiesto.')
