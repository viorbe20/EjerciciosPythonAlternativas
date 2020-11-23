"""Programa: ej23.numeromascercano.py
Fecha:04/11/2020
Autora: Virginia Ordoño

Propósito:
Diseña un programa que, dados cinco números enteros, determine cuál de los cuatro últimos números
es más cercano al primero. Por ejemplo, si el usuario introduce los números 2, 6, 4, 1 y 10,
el programa responderá que el número más cercano al 2 es el 1.

Análisis:
- Pedimos al usuario cinco números.
- Calculamos la diferencia entre el primer número y el resto.
- Comparamos las distancias y verificamos cuál es la menor para que aparezca un mensaje indicándolo.
"""

print('Introduce 5 números y el programa te dirá cuál está más cerca del primero.')

# Pedimos al usuario 5 números.
number1 = int(input('Escribe un primer número.'))
number2 = int(input('Escribe un segundo número.'))
number3 = int(input('Escribe un tercer número.'))
number4 = int(input('Escribe un cuarto número.'))
number5 = int(input('Escribe un quinto número.'))

# Calculamos la diferencia entre el primer número y el resto.
distance2 = abs(number1 - number2)
distance3 = abs(number1 - number3)
distance4 = abs(number1 - number4)
distance5 = abs(number1 - number5)

# Si la distancia del primer al segundo número es menor que la distancia entre el primer número y el resto,
# aparece un mensaje indicándolo.
if distance3 > distance2 < distance4 and distance2 < distance5:
    print('El número más cercano es', number2, '.')

# Si la distancia del primer al tercer número es menor que la distancia entre el primer número y el resto,
# aparece un mensaje indicándolo.
elif distance2 > distance3 < distance4 and distance3 < distance5:
    print('El número más cercano es', number3, '.')

# Si la distancia del tercer al segundo número es menor que la distancia entre el primer número y el resto,
# aparece un mensaje indicándolo.
elif distance2 > distance4 < distance3 and distance4 < distance5:
    print('El número más cercano es', number4, '.')

# En caso contrario, la menor distancia es con el último número. Aparece un mensaje indicáncolo..
else:
    print('El número más cercano es', number5, '.')