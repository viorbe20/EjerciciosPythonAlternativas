"""
Programa: ej18.diasdelasemana.py
Fecha:25/10/2020
Autora: Virginia Ordoño

Propósito: Realiza un programa que pida el día de la semana (del 1 al 7) y escriba el día correspondiente.
Si introducimos otro número nos da un error.

Análisis:
- Pedimos el número de día al usuario.
- Si nos da un número del 1 al 7, aparece el día correspondiente.
- En caso contrario, da un mensaje de error.
- Variables:number.
- secuencias: if, elif, else.
"""


number = input('Introduce un número del 1 al 7 correspondientes a los días de la semana: ')

# Si el número es 1, aparece un mensaje de lunes y así sucesivamente.
if number == '1':
    print ('Es el lunes.')
elif number == '2':
    print ('Es el martes.')
elif number == '3':
    print ('Es el miércoles.')
elif number == '4':
    print ('Es el jueves.')
elif number == '5':
    print ('Es el viernes.')
elif number == '6':
    print ('Es el sábado.')
elif number == '7':
    print('Es el domingo.')

# En caso contrario aparece un mensaje de error.
else:
    print ('El valor introducido no es correcto. Por favor, inténtalo de nuevo.')