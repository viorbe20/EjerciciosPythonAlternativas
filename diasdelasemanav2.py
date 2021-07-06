'''Programa:diasdelasemana.py'''
'''Autora: Virginia Ordoño Bernier'''
'''Fecha:20/10/2020'''
'''Propósito: Pedir al usuario un número entre 1 y 7 que nos devuelva el día de la semana correspondiente .'''

'''Análisis: Implementación de la formac compacta de if. Pedimos al usuario que ingrese un número del 1 al 7. Primero damos la opción a introducir un valor 
incorrecto. La sentencia if nos avisa del error si el número es menos de 1 o mayor de 7. Con la sentencia else 
determinamos el resto de valores entre 1 y 7 y les asignamos el día correspondiente'''

#La función print muestra el enunciado del ejercicio.
print ('Dando un número del 1 al 7 obtener el día de la semana correspondiente')
print ('')

#Pedir al usuario que ingrese un número del 1 al 7.
number = int(input('Escribe un número del 1 al 7: '))

#Sentencia if para número 1 y forma compacta de if para permitir números diferentes de 1. Asignar el día en función
# del número ingresado.
if number == 1:
    print ('Lunes')
elif number == 2:
    print ('Martes')
elif number == 3:
    print ('Miércoles')
elif number == 4:
    print ('Jueves')
elif number == 5:
    print ('Viernes')
elif number == 6:
    print ('Sábado')
elif number == 7:
    print ('Domingo')

#Sentencia else para ejecutar el resto de los números que estén enter 1 o 7.
else:
    print ('No corresponde a ningún día')

