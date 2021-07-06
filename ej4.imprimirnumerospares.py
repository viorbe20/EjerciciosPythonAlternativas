"""
Programa: ej4.imprimirnumerospares.py
Autora: Virginia Ordoño Bernier
Fecha:04/11/2020
_______________________________________________________________________________________________________________________
Propósito
_______________________________________________________________________________________________________________________
Escribir un programa que imprima todos los números pares entre dos números que se le pidan al usuario.
_______________________________________________________________________________________________________________________
Análisis
_______________________________________________________________________________________________________________________
- Pedimos al usuario que introduzca un carácter.
_______________________________________________________________________________________________________________________
Algoritmo
_______________________________________________________________________________________________________________________
- Variables:
- Secuencias:
- Bucles:
"""

print('Introduce dos números para que el programa imprima todos los pares entre esos números: ')

# Pedimos al usuario que introduzca dos números.
n1 = int(input("Introduce el número 1: "))
n2 = int(input("Introduce el número 2: "))

# En caso de que el primer número sea mayor, tendremos que intercambiarlos de posición.
if n1 > n2:
    n1, n2 = n2, n1

# Hacemos una división entera del n1 entre 2 para ver si el resto es 1 para comprobar si es un número impar.
# En ese caso añadimos 1 para convertirlo en par.
if n1 % 2 == 1:
    n1 += 1

# Si el valor de n está en el rango entre los dos números dados por el usuario aparece
for n in range(n1, n2 + 1, 2):
    print(f"{n} ", end="")
