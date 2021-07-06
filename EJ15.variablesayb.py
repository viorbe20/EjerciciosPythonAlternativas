'''Programa: EJ15.variablesayb.py'''
'''Autora: Virginia Ordoño Bernier'''
'''Fecha:12/10/2020'''
'''Propósito: Intercambiar el valor de dos variables.'''

'''Análisis: Solicitamos el valor de un número obtendremos el número invertido'''


#Con print mostramos el enunciado.
print ('15. Dadas dos variables numéricas A y B, que el usuario debe teclear, se pide realizar un algoritmo que')
print ('intercambie los valores de ambas variables y muestre cuanto valen al final las dos variables.')

#Solicitamos datos
A = input ('Escribe el valor de A: ')
B = input ('Escribe el valor de B: ')

#Operaciones
C = (float(A))
A = (float(B))
B = (float(C))
print('')

#Resultado
print ('Después del intercambio el valor de A es', int(A), 'y el valor de B es' ,(int(B)),'.')
