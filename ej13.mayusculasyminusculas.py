"""Ejercicio 13

Realizar un programa que lea una cadena por teclado y convierta las mayúsculas a minúsculas y vicevers"""

# Pedimos los datos
cadena = input("Dime una cadena: ")
aux = ""

# Sacamos letra por letra y comprobamos si es minúsculas o mayúsculas
for x in range(0,len(cadena)):
    letra = cadena[x]

    # Lo transformamos al contrario y lo metemos en una variable
    if letra.isupper():
        aux += letra.lower()
    else:
        aux += letra.upper()
print(f"La cadena es {aux}")