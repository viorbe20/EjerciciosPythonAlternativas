"""
Programa: ej1.numeroaleatorio.py
Autora: Virginia Ordoño Bernier
Fecha:04/11/2020
____________________
Propósito
____________________
Crea una aplicación que permita adivinar un número. La aplicación genera un número aleatorio del 1 al 100.
A continuación va pidiendo números y va respondiendo si el número a adivinar es mayor o menor que el introducido,
además de los intentos que te quedan (tienes 10 intentos para acertarlo).

El programa termina cuando se acierta el número (además te dice en cuántos intentos lo has acertado),
si se llega al limite de intentos te muestra el número que había generado.
____________________
Análisis
____________________
- Importamos biblioteca random para generar un número aleatorio de 1 a 100.
- Pedimos al usuario que escriba un número entre 1 y 100 para ver si es el mismo que ha elegido la máquina.
Pueden ocurrir dos cosas:
    - No acierta. Aparece un mensaje indicando si el número es mayor o menor para que lo vuelva a intentar y le avisa
    del número de intentos que le quedan.
    - Acierta. Aparece un  mensaje mostrándolo.

- Si llega a 10 intentos, el programa se para.
____________________
Diseño
____________________
- Variables: num_user (número del usuario), num_py (número generado), guesses (límite de intentos),
             quesses now (intentos que quedan)
- Secuencias: if, elif, else.
- Bucles: while.
- Módulo: random función randint.
"""

print("Debes adivinar un número entre 1 y 100. Introduce un número y el programa te dirá si es mayor o menor "
      "que el número que tienes que adivinar.")
print("Tienes 10 intentos.\n")

# Importamos la función randint del módulo random. Esta nos creará un número aleatorio.
from random import randint

# Declaramos la variable para el número generado por Python
num_py = randint(1, 100)

# Declaramos un contador para determinar el máximo de veces que el usuario puede introducir un valor.
guesses = 10

# Pedimos datos.
num_user = int(input("Introduce un número entre el 1 y el 100: "))

# Creamos una variable que descuente 1 al límie de intentos.
guesses_now = guesses -1

# Ciclo que se repite mientras que el número introducido por el usuario sea diferente al generado y los intentos
# que quedan sean mayor a 0. Si algunas de estas condiciones no se cumple, se sale del ciclo.
while num_user != num_py and guesses_now > 0:

    # Si el número introducido es menor que el de generado, aparecer un mensaje indicándolo.
    if num_user < num_py:
        print(f"{num_user} es menor que el número que estoy pensando.")
    # Si el número introducido es mayor que el de generado, aparecer un mensaje indicándolo.
    else:
        print(f"{num_user} es mayor que el número que estoy pensando.")
    # Mensaje que aparece cuando se introduce un número incorrecto. Te avisa de los intentos que te quedan
    # y vuelve a pedir un nuevo número.
    num_user = int(input("Te quedan " +  str(guesses_now) + " intentos. Introduce un número entre 1 y 100: "))
    # Descuenta un intento cada vez que se completa el bucle.
    guesses_now -= 1


# En caso de acierto aparece un mensaje indicándolo.
if num_user == num_py:
    print(f"¡Enhorabuena!. Has adivinado el número en {guesses-guesses_now} intentos.")
# En caso de agotar el número de intentos, aparece un mensaje indicándolo.
else:
    print(f"Has agotado el número máximo de intentos. El número a adivinar era {num_py}.")
