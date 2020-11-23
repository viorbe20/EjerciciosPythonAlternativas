"""Programa: ej23v2.numeromascercano.py
Fecha:04/11/2020
Autora: Virginia Ordoño

Propósito:
Diseña un programa que, dados cinco números enteros, determine cuál de los cuatro últimos números
es más cercano al primero. Por ejemplo, si el usuario introduce los números 2, 6, 4, 1 y 10,
el programa responderá que el número más cercano al 2 es el 1.

Análisis:
- Pedimos al usuario cinco números.
- Calculamos la distancia entre el primer número y el segundo poniendo a este último jcomo candidato a ser
el más cercano.
- Haremos la comprobación con el resto de números. Si fuera menos que la del candidato lo sustituimos.

 _______________________________________________________________________________________________________________________
 Algoritmo
 _______________________________________________________________________________________________________________________
 Variables:
 - number1, number2, number3, number4, number5 (números introducidos)
 - distance guardará la 'distancia' del primer número con el candidato.
 - candidate: número candidato a la menor distancia.

 Pedir
 - number1, number2, number3, number4, number5.
 - distance. abs(number1 - number2)
 """

print("Introduce 5 números y el programa te dirá cuál está más cerca del primero.")
print("__________________________________________________________________________")

# Pedimos al usuario 5 números.
print ("Dame cinco números")
n1 = int(input())
n2 = int(input())
n3 = int(input())
n4 = int(input())
n5 = int(input())

# Establecemos candidato inicial.
candidate = n2
distance = abs(n1 - n2)

# Comprobamos tercer número.
if abs(n1-n3) < distance:
    candidate = n3
    distance = abs(n1-n3)

# Comprobamos cuarto número.
if abs(n1-n4) < distance:
    candidate = n4
    distance = abs(n1-n4)

# Comprobamos quinto número.
if abs(n1-n5) < distance:
    candidate = n5
    distance = abs(n1-n5)

print(f"EL número {candidate} es el número con menor distancia a {n1}")