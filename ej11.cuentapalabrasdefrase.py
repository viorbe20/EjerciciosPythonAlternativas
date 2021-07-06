"""ejercicio 11

suponiendo que hemos introducido una cadena por teclado que representa una frase (palabras separadas por espacios),
realiza un programa que cuente cuantas palabras tiene"""


print("Contador de palabras")
print("--------------------")

# Petición de datos
cadena = input("Introduce una frase: ")

# Proceso
estoy_en_palabra = False
contador_palabras = 0
for c in cadena:
    if c != " ":
        if not estoy_en_palabra:
            estoy_en_palabra = True
            contador_palabras += 1
    else:
        estoy_en_palabra = False

# Salida

print("Número de palabras:", contador_palabras)