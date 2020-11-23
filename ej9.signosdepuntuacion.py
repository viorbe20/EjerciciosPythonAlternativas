"""
Programa: ej9.signosdepuntuacion.py
Fecha:24/10/2020
Autora: Virginia Ordoño

Propósito:
Diseñar un programa que lea un carácter de teclado y muestre por pantalla los mensajes:
- «Es signo de puntuación» solo si el carácter leído es un signo de puntuación,
- «Es una letra» si es una letra (da igual que sea mayúscula, minúscula o acentuada),
- «Es un dígito» si es un dígito,
- «Es otro carácter» r el si no es ninguno de los anteriores,
- «No es un carácter» si el usuario ha introducido más de un carácter.

Análisis:
- Pedimos un carácter al usuario.
- Leemos la cadena y establecemos que, si nos devuelve un carácter, se imprimen diferentes mensajes en función
del tipo de carácter que sea.
- En caso contrario, imprime: no es un carácter.
- Operador: in.
- Sentencias: if, elif, else.
- Función: len.
- Métodos: isalpha, isdigit.
"""

print('Escribir un carácter de teclado para que el programa especifique de qué tipo es.')

# Pedimos al usuario que introduzca un carácter.
chain = input('Introduce por favor un carácter para que el programa especifique de qué tipo es: .')

# La función 'len' lee la cadena. Con la función 'if', si el valor es igual a 1 sigue leyendo. Si en la cadena hay
# un signo de puntuación, aparece un mensaje indicándolo.
if len(ch) == 1:
    if ch in ".,:;()[]¿¡!¿?'\'/":
        print("Es un signo de puntuación.")

# Usamos método 'isalpha' para determinar si en la cadena hay una letra, aparece un mensaje indicándolo.
    elif ch.isalpha():
        print("Es una letra")

# Usamos método 'isdigit' para determinar si en la cadena hay un dígito, aparece un mensaje indicándolo.
    elif ch.isdigit():
        print("Es un dígito.")

# En caso contrario, aparece un mensaje indicando que es otro carácter.
    else:
        print("Es otro carácter.")

# En caso contrario, aparece un mensaje indicando que no es un carácter.
else:
    print("No es un carácter.")
