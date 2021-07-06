"""
Programa: ej2.numeroscomparados0.py
Autora: Virginia Ordoño Bernier
Fecha:04/11/2020
_______________________________________________________________________________________________________________________
Propósito
_______________________________________________________________________________________________________________________
Realizar un algoritmo que pida números (se pedirá por teclado la cantidad de números a introducir). El programa
debe informar de cuantos números introducidos son mayores que 0, menores que 0 e iguales a 0.
_______________________________________________________________________________________________________________________
Análisis
_______________________________________________________________________________________________________________________
_______________________________________________________________________________________________________________________
Algoritmo
_______________________________________________________________________________________________________________________

"""

# Preguntamos al usuario la cantidad de números que va a introducir.
num = int(input("¿Cuántos números vas a introducir?: "))

# Creamos tres contadores, uno para cada tipo de número: igual, mayor o menor de cero.
cnt_zeros = 0
cnt_positives = 0
cnt_negatives = 0

# Creamos un bucle for para que la i tome el valor del rango contenido entre 1 y el número indicado por el usuario.
# Como en rango el número final siempre te devuelve un número menos, añadimos +1.
for i in range(1, num + 1):
    num = int(input(f"Número {i}: "))

# Comprobamos si cada número introducido por el usuario es mayor, menor o igual a cero e incrementamos
# el contador en uno con cada comprobación.
    if num > 0:
        cnt_positives += 1
    elif num < 0:
        cnt_negatives += 1
    else:
        cnt_zeros += 1

# Comprobados los números se muestra la cantidad aquellos que son mayor,menor o igual a 0 de manera separada.
print(f"Números positivos: {cnt_positives} ,end=""")
print(f"Números negativos: {cnt_negatives},end=""")
print(f"Números igual a 0: {cnt_zeros},end=""")
