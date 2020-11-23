"""
Programa: ej4.divisioncero.py
Fecha:17/10/2020
Autora: Virginia Ordoño Bernier

Propósito:
Crear un algoritmo  que pida al usuario dos números y muestre su división si el segundo no es cero,
o un mensaje de aviso en caso contrario.

Análisis:
- Pedimos al usuario dos números.
- Si el segundo número es igual a 0 aparece un mensaje de aviso.
- Si no, aparece un mensaje calculando el valor de la división.
- Variables: number1, number2.
- Sentencias: if, else.
"""

print('Mostrar la división entre dos números sin que el segundo sea 0.')

# Con input pedimos al usuario que ingrese dos números.
number1 = int(input('Dime un número: '))
number2 = int(input('Dime un segundo número: '))

# Con la sentencia if determinamos que si el segundo número es 0, aparezca un mensaje de error.
if number2 == 0:
    print('¡Atención! El segundo número introducido debe ser diferente a 0. Intántalo de nuevo')

# Con la sentencia else determinamos que si el segundo número es diferente a 0, se muestre el resultado de la división.
else:
    division = int(number1 / number2)
    print(number1, 'dividido entre', number2, 'es igual a', division, '.')
