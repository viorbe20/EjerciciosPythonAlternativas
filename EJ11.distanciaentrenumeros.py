'''Programa: EJ11.distanciaentrenumeros.py'''
'''Autora: Virginia Ordoño Bernier'''
'''Fecha:13/10/2020'''
'''Propósito: Mostrar la distancia entre dos números facilitados por el usuario.'''

'''Análisis: Solicitamos el valor de cada uno de los exámenes parciales y calculamos las medias en función 
del porcentaje indicado para cada trabajo. Variables: N1, N2, distancia, valor_absoluto'''

#Con print mostramos el enunciado.
print ('11. Pide al usuario dos números y muestra la "distancia" entre ellos (el valor absoluto de su diferencia')
print ('de modo que el resultado sea siempre positivo).')

#Solicitamos el valor de los números al usuario.
N1 = input ('Dime el valor del número 1: ')
N2 = input ('Dime el valor del número 2: ')

#Calculamos la distancia con los valores aportados anteriormente.
distancia = (int(N1) - int(N2))

#Calculamos el valor absoluto de la distancia.
valor_absoluto = abs(distancia)

#Mostramos la distancia final.
print ('La distancia entre' , str(N1) ,'y' , str(N2) ,'es' ,(valor_absoluto),'.')
