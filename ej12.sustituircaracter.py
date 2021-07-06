"""Pide una cadena y dos caracteres por teclado (valida que sea un carácter),
sustituye la aparición del primer carácter en la cadena por el segundo carácter."""

# Pedimos datos.
cadena = input("Introduce una cadena de caracteres: ")
caracter1 = input("Introduce el carácter que tenemos que buscar: ")
caracter2 = input("Introduce el nuevo carácter: ")

# Recorremos la cadena.
while len(caracter1) != 1 or len(caracter2) != 1:
    print("Ese no es un carácter correcto. Por favor inténtalo de nuevo.\n")
    caracter1 = input("Introduce el carácter que tenemos que buscar: ")
    caracter2 = input("Introduce el nuevo carácter: ")

nueva = cadena.replace(caracter1, caracter2)

print(f"La nueva cadena es {nueva}")
