"""Pide una cadena y un carácter por teclado y
muestra cuantas veces aparece el carácter en la cadena.


dime tu cadena : virginia(3 veces la i)
Dime el caracter deseado: i
Aparece: en {cadena} el caractacter {caracter} aparace 3 veces.

variables: cadena,caracter

 i -> para i=0 hasta longitud(cadena) con paso 1 hacer:
    ....

i -> variable de control -> 0,1,2,3,4,5,6 -> iteraciones
0, 1, 2,

 """

cadena = input("Introduce una cadena de caracteres: ")
caracter = input("Introduce un carácter: ")
acumulador = 0

for i in range(len(cadena)): #iteracion 1: i -> 0    hasta len(cadena) -> virginia hasta 8-1 0 al 7 (i -> 0, len(cadena) -> 8-1), i -> 1, i -> 2,
    if cadena[i] == caracter: # si cadena[0] -> v == i, cadena[1] i == i  , cadena [2] r != i
        acumulador+=1 # 0 -> 1

print(f" En {cadena} el caractacter {caracter} aparace {acumulador} veces.")


