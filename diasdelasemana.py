'''Programa:diasdelasemana.py'''
'''Autora: Virginia Ordoño Bernier'''
'''Fecha:20/10/2020'''
'''Propósito: Pedir al usuario un número entre 1 y 7 que nos devuelva el día de la semana correspondiente .'''

'''Análisis: Pedimos al usuario que ingrese un número del 1 al 7. Primero damos la opción a introducir un valor 
incorrecto. La sentencia if nos avisa del error si el número es menos de 1 o mayor de 7. Con la sentencia else 
determinamos el resto de valores entre 1 y 7 y les asignamos el día correspondiente'''

#La función print muestra el enunciado del ejercicio.
print ('Dando un número del 1 al 7 obtener el día de la semana correspondiente')
print ('')

#Pedir al usuario que ingrese un número del 1 al 7.
number = int(input('Escribe un número del 1 al 7: '))

#Sentencia condicional if, por si el usuario introduce un número que no esté entre 1 y 7. Print nos devuelve el mensaje
# de error
if number < 1:
    print ('El número', number,  'no es válido.')
if number > 7:
    print ('El número', number, 'no es válido.')

#Sentencia else para ejecutar el bloque correspondiente a los números entre 1 y 7 y asignarle el día correspondiente.
# Print nos devuelve el día que corresponde al número ingresado.
else:
    if number == 1:
        print ('El número 1 corresponde al lunes.')
    if number != 1:
        if number == 2:
            print ('El número 2 corresponde al martes.')
        if number != 2:
            if number == 3:
                print ('El número 3 corresponde al miércoles.')
        if number != 3:
            if number == 4:
                print('El número 4 corresponde al jueves.')
            if number != 4:
                if number == 5:
                    print('El número 5 corresponde al viernes.')
                if number != 5:
                    if number == 6:
                        print('El número 6 corresponde al sábado.')
                    if number != 6:
                        if number == 7:
                            print('El número 7 corresponde al domingo.')
