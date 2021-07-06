'''Programa: EJ7.minutosyhoras.py'''
'''Autora: Virginia Ordoño Bernier'''
'''Fecha:07/10/2020'''
'''Propósito: Realizar un programa que reciba una cantidad de minutos y muestre por pantalla 
a cuántas horas y minutos corresponde.'''

'''Análisis: Mediante la función input solicitamos 3 números al usuario. Creamos la fórmula de la media y 
mostramos el resultado. Variables: minutos, horas.'''

#La función print muestra el enunciado del ejercicio.
print ('7. Realiza un programa que reciba una cantidad de minutos y muestre por pantalla a cuantas horas y minutos corresponde.')
print('')

#Con la función input solicitamos un número de minutos y creamos la variable minutos.
minutos = input('Dime cuántos minutos quieres convertir en horas: ')

#Creamos la variable horas con el input dado de los minutos.
horas = int(minutos) // 60
minutos_resto = int(minutos) % 60

print (str(minutos) + ' minutos equivalen a ' + str(horas) + ' horas y ' + str(minutos_resto) +' minutos')


