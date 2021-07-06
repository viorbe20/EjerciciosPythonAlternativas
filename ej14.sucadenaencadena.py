Ejercicio 14

Realizar un programa que compruebe si una cadena contiene una subcadena. Las dos cadenas se introducen por teclado.

# Inicializamos variables
esta_subcadena = False
i = 0

# Pedimos datos
cadena = input("Dame una cadena: ")
subcadena = input(f"Dame una subcadena de '{cadena}': ")

# Proceso de búsqueda de la subcadena
comprobar_hasta = len(cadena)-len(subcadena)
while not esta_subcadena and i<=comprobar_hasta:
    if subcadena == cadena[i:i+len(subcadena)]:
        esta_subcadena = True
    i += 1

# Mostramos resultado
if esta_subcadena:
    print("Muy bien")
else:
    print(f"Me estás engañando '{subcadena}' no forma parte de '{cadena}'")