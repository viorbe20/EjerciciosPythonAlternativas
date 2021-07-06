'''Programa: EJ14.numeroinvertido.py'''
'''Autora: Virginia Ordoño Bernier'''
'''Fecha:12/10/2020'''
'''Propósito: Obtener un número invertido.'''

'''Análisis: Solicitamos el valor de un número obtendremos el número invertido'''


#Con print mostramos el enunciado.
print ('14. Dado un número de dos cifras, diseñe un algoritmo que permita obtener el número invertido.')

#Pedimos datos
numero = input ('Dime un número para calcular el inverso: ')

#Cálculos
numero_invertido = join(reversed(numero))

#Solución
print ('El número invertido' , str(numero_invertido))
