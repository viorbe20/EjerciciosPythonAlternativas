"""
Programa: ej8.cronometrotiempo.py
Autora: Virginia Ordoño Bernier
Fecha:04/11/2020
_______________________________________________________________________________________________________________________
Propósito
_______________________________________________________________________________________________________________________
Hacer un programa que muestre un cronometro, indicando las horas, minutos y segundos.
Para hacer una espera en Python podemos usar el método sleep del módulo time.
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
import time

# Inicializamos contador para las horas, minutos y segundos.
hours = 0
minutes = 0
seconds = 0


# Hacemos un ciclo infinito y esperamos 1 segundo cada iteración
# 02 es para indicar que va a ocupar dos lugares.
while True:
    print(f"{hours:02}:{minutes:02}:{seconds:02}", end="")
    time.sleep(1)

    # Mientras los segundos sean menor a 59 se incrementa en 1. Así se van contando los segundos.
    if seconds < 59:
        seconds += 1

    # En caso contrario (segundos mayor que 59) hacemos que vuelvan a 0.
    else:
        seconds=0
        # Si en ese caso los minutos son menos que 59, incrementamos los minutos en 1.
        if minutes < 59:
           minutes += 1
        # En caso contrario (minutos mayor 59) dejamos los minutos a 0 e incrementamos la hora en 1..
        else:
            minutes = 0
            hours += 1

# onemos el cursor al principio de la línea
    print(8 * "\b", end="") # \b desplaza el cursor a la izquierda