"""
Programa: ej8.aceptadanoaceptada.
Autora: Virginia Ordoño Bernier
Fecha:22/10/2020

Propósito:
Crear un algoritmo que con los datos ‘nota’ y ‘edad’ y ‘sexo’ y muestre:
- Mensaje ‘ACEPTADA’ si la nota es mayor o igual a cinco, la edad es mayor o igual a
dieciocho y el sexo es ‘F’.
- En caso de que se cumpla lo mismo, pero el sexo sea ‘M’, debe imprimir ‘POSIBLE’.
- Si no se cumplen dichas condiciones se debe mostrar ‘NO ACEPTADA’.

Análisis:
- Pedimos al usuario la información de la nota, la edad y el sexo.
- Si la nota es mayor o igual a cinco, la edad es mayor o igual a dieciocho y el sexo es ‘F’ aparece mensaje aceptada.
- Si el sexo no es femenino, aparece mensaje: posible.
- En caso contrario a los anterior, aparece mensaje: no aceptada.
- Variables: score, age, gender.
- Secuencias: if, else.
"""

print('Facilita los datos que se pedirán a continuación para saber si se cumplen las condiciones para ser aceptada')

# Pido los datos.
score = int(input('Escribe tu nota final: '))
age = int(input('Escribe tu edad: '))
gender = input('Indica tu sexo. Usa F para mujer y M para hombre: ')

# Con la sentencia if establecemos que si la puntuación es igual o mayor que 5 y la edad igual o mayor que 18,
# aparecerá un mensaje de 'aceptada'.
if score >= 5 and age >= 18:
    if gender == 'F':
        print('Es aceptada')
    else:
        print('Es posible.')
else:
    print('No aceptada.')
