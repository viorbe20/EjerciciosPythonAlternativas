'''Programa: EJ5.fahrenheitacelsius.py'''
'''Autora: Virginia Ordoño Bernier'''
'''Fecha:07/10/2020'''
'''Propósito: Escribir un programa que convierta un valor dado en grados Fahrenheit a grados Celsius.'''

'''Análisis: Mediante la función print pedimos los grados en Fahrenheit. Los pasamos a Celsius y mostramos el resultado
mediante print. Variables: fahrenheit, celsius.'''

#La función print muestra el enunciado del ejercicio.
print ('5. Escribir un programa que convierta un valor dado en grados Fahrenheit a grados Celsius.')
print ('')

#Mediante la función input pedimos el valor de los grados Fahrenheit.
fahrenheit = input('Escribe los grados Fahrenheit: ')
print ('')

#Realizamos la fórmula para calcular el valor de los grados Celsius.
celsius = (float(fahrenheit)-32*(5/9))

#Usamos la función print para mostrar la conversión a Celsius.
print (str(fahrenheit) +' grados Fahrenheti equivalen a ' +str(celsius) +' grados Celsius.')


