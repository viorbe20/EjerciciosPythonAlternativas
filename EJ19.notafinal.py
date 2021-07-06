'''Programa: EJ19.notafinal.py'''
'''Autora: Virginia Ordoño Bernier'''
'''Fecha:12/10/2020'''
'''Propósito: Obtener la nota final.'''

'''Análisis: Solicitamos la puntuación de las respuestas del estudiante para obtener la nota final '''

#La función print muestra el enunciado del texto.
print ('19. Escribir un algoritmo para calcular la nota final de un estudiante, considerando que por cada')
print ('respuesta correcta 5 puntos, por una incorrecta -1 y por respuestas en blanco 0. Imprime el resultado')
print ('obtenido por el estudiante.')

#Pedir datos.
respuestas_correctas = input ('Escribe cuántas respuestas correctas has obtenido: ')
respuestas_incorrectas = input ('Escribe cuántas respuestas incorrectas has obtenido: ')
respuestas_blanco = input ('Escribe cuántas respuestas has dejado en blanco: ')

#Operaciones.
puntos_correctas = (int(respuestas_correctas) * (5))
puntos_incorrectas = (int(respuestas_incorrectas) * (-1))
puntos_blanco = ((respuestas_blanco) * (0))

nota_final= (int(puntos_correctas) + int(puntos_incorrectas))

#Resultados.
print ('Tu nota final es', (nota_final),'.')


