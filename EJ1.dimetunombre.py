'''Programa: EJ1.dimetunombre.py'''
'''Autora: Virginia Ordoño Bernier'''
'''Fecha:07/10/2020'''
'''Propósito: Preguntar al usuario su nombre y saludarlo'''

''' Análisis: Pedimos un nombre por teclado y luego con el nombre dado los saludamos con la función print. 
Variable: nombre.'''

#La función print muestra el enunciado del ejercicio
print ('Ejercicio 1. Escribir un programa que pregunte al usuario su nombre, y luego lo salude.')
print ('')

#Pedimos el nombre al usuario mediante la función input
nombre = input ('Dime tu nombre:')

#Mediante la función print se muestra el saludo y el valor dado al nombre por el usuario
print("Hola " + nombre)
