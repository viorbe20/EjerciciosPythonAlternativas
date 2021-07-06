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
- Variables: num_user (número del usuario), num_py (número generado), guesses (intentos).
- Secuencias: if, elif, else.
- Bucles: while True, break.
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

# Ciclo que se repite mientras que el usuario introduzca números diferentes al que hay que adivinar.
# Aparece un mensaje pidiendo un nuevo número e indicando el número de intentos que quedan.
while True:
    num_user = int(input(f"Te quedan {guesses} intentos. Introduce un número: "))

    # Si el número introducido es menor que el de generado, aparecer un mensaje indicándolo.
    if num_user < num_py:
        print(f"{num_user} es menor que el número que estoy pensando.")
    # Si el número introducido es mayor que el de generado, aparecer un mensaje indicándolo.
    elif num_user > num_py:
        print(f"{num_user} es mayor que el número que estoy pensando.")

    # Descontamos 1 a cada interación.
    guesses -= 1

    # Salimos del ciclo si acierta el número o si llega a intentarlo 10 veces.
    if num_user == num_py or guesses == 0:
        break

# En caso de acierto aparece un mensaje indicándolo.
if num_user == num_py:
    print(f"¡Enhorabuena!. Has adivinado el número en {10-guesses} intentos.")
# En caso de agotar el número de intentos, aparece un mensaje indicándolo.
else:
    print(f"Has agotado el número máximo de intentos. El número a adivinar era {num_py}.")
