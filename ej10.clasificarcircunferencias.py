"""
Programa: ej10.clasificarcircunferencias.py
Fecha:24/10/2020
Autora: Virginia Ordoño

Propósito:
Algoritmo que pida los puntos centrales x1,y1,x2,y2 y los radios r1,r2 de dos circunferencias y
las clasifique en uno de estos estados:
- exteriores
- tangentes exteriores
- secantes
- tangentes interiores
- interiores
- concéntricas

Análisis:
- Pedimos al usuario el valor de x1, y1, r1, x2, y2, r2.
- Calculamos la distancia entre los radios de forma que según el resultado aparezca un mensaje indicando
el tipo de circunferencia.
- Variables: x1, x2, r1, x2, y2, r2, distance.
- Módulos: math.
- Sentencias: if, elif.
"""

print('Tendrás que escribir los valores que te pida el programa para que te clasifique las circunferencias.')

# Mediante la función input pedimos al usuario que introduzca un carácter y le damos valor a la variable 'caracter'.
x1 = float(input('Escribe el valor de x1: '))
y1 = float(input('Escribe el valor de y1: '))
r1 = float(input('Escribe el valor del radio 1: '))
x2 = float(input('Escribe el valor de x2: '))
y2 = float(input('Escribe el valor de y2: '))
r2 = float(input('Escribe el valor del radio 2: '))

# Importamos el módulo math para usar luego el parámetro de la raíz cuadrada y poder asignarle una función
# a la variable distance.
import math

distance = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Con if indicamos que si la distancia es mayor que la suma de los radios, se muestre un mensaje indicando que
# las circunferencias son exteriores.
if distance > r1 + r2:
    print('Las circunferencias son exteriores.')

# Con elif indicamos que si la distancia es igual a la suma de los radios, se muestre un mensaje indicando que
# las circunferencias son tangentes exteriores.
elif distance == r1 + r2:
    print('Las circunferencias son tangentes exteriores.')

# Con elif indicamos que si la distancia es menor que la suma de los radios y mayor que el valor absoluto de la
# resta de los radios, se muestre un mensaje indicando que las circunferencias son secantes.
elif (r1 + r2) > distance > abs(r1 - r2):
    print('Las circunferencias con secantes.')

# Con elif indicamos que si la distancia es igual que el valor absoluto de la resta de los radios, se muestre un mensaje
# diciendo que las circunferencias son tangentes interiores.
elif distance == abs(r1 - r2):
    print('Las circunferencias son tangentes interiores.')

# Con elif indicamos que si la distancia es mayor que cero y menor que el valor absoluto de la resta de los
# radios se muestre un mensaje diciendo que las circunferencias son interiores.
elif 0 < distance < abs(r1 - r2):
    print('Las circunferencias son interiores')

# Con elif indicamos que si la distancia es igual a cero,  se muestre un mensaje diciendo que
# las circunferencias son concéntricas.
elif distance == 0:
    print('Las circunferencias son concéntricas.')
