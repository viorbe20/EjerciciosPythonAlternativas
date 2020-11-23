"""Programa: ej24.calificacionnumerica.py
Fecha:25/10/2020
Autora: Virginia Ordoño

Propósito: Diseña un programa que, dado un número real debe representar la calificación numérica de un examen,
proporcione la calificación cualitativa correspondiente al número dado.
La calificación cualitativa será una de las siguientes:
- «Suspenso» (nota menor que 5),
- «Aprobado» (nota mayor o igual que 5, pero menor que 7),
- «Notable» (nota mayor o igual que 7, pero menor que 9),
- «Sobresaliente» (nota mayor o igual que 9, pero menor que 10),
- «Matrícula de Honor» (nota 10).

Análisis:
- Pedimos al usuario la puntuación del examen.
- En función de la nota, aparece un mensaje con la correspondiente calificación.
"""

score = float(input('Dime la nota del examen: '))

# Si la nota es menor que 4, aparece un mensaje indicando la calificación correspondiente.
if score < 4:
    print('La nota es suspenso.')

# Si la nota es menor o igual que 5 y menor que 7, aparece un mensaje indicando la calificación correspondiente.
elif 5 >= score < 7:
    print('La nota es aprobado.')

# Si la nota es menor o igual que 7 y menor que 9, aparece un mensaje indicando la calificación correspondiente.
elif 7 >= score < 9:
    print('La nota es notable.')

# Si la nota es menor o igual que 9 y menor que 10, aparece un mensaje indicando la calificación correspondiente.
elif 9 >= score < 10:
    print('La nota es sobresaliente.')

# Si la nota es igual que 10, aparece un mensaje indicando la calificación correspondiente.
elif score == 10:
    print('La nota es matrícula de honor.')

# En caso contrario, aparece un mensaje diciendo que el valor no es correcto.
else:
    print('El valor introducido no es correcto.')
