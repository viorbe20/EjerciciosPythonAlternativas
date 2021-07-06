'''Programa: EJ6.mediade3numeros.py'''
'''Autora: Virginia Ordoño Bernier'''
'''Fecha:07/10/2020'''
'''Propósito: Calcular la media de tres números pedidos por teclado.'''

'''Análisis: Mediante la función input solicitamos 3 números al usuario. Creamos la fórmula de la media y 
mostramos el resultado.'''

#La función print muestra el enunciado del ejercicio.
print ('6. Calcular la media de tres números pedidos por teclado.')
print('')

#Mediante la función input pedimos los 3 números.
numero_1 = input ('A continuación escribe un número: ')
numero_2 = input ('A continuación escribe un segundo número: ')
numero_3 = input ('Por último escribe un tercer número: ')
print('')

#Creamos la variable de la media e incluimos los valores dados por el usuario.
suma = float(numero_1 + numero_2 + numero_3)
media_2 = suma / 3
print('')

#Usamos la función print para mostrar la media.
print ('La media de la suma de los números', 'es', str(media_2),'.')
