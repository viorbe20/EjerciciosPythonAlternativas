'''Programa: EJ10.notafinal.py'''
'''Autora: Virginia Ordoño Bernier'''
'''Fecha:12/10/2020'''
'''Propósito: Calcular la calificación final de un alumno en la materia de Algoritmos.'''

'''Análisis: Solicitamos el valor de cada uno de los exámenes parciales y calculamos las medias en función 
del porcentaje indicado para cada trabajo.'''

print ('10. Un alumno desea saber cual será su calificación final en la materia de Algoritmos. Dicha calificación')
print ('se compone de los siguientes porcentajes: 55% del promedio de sus tres calificaciones parciales')
print ('30% de la calificación del examen final y 15% de la calificación de un trabajo final.')
print('')

#Con la función input solicitamos al usuario el valor de los parciales  y creamos una variable para cada uno de ellos.
parcial1 = input('Escribe cuál es la nota de tu primer parcial: ')
parcial2 = input('Escribe cuál es la nota de tu segundo parcial: ')
parcial3 = input('Escribe cuál es la nota de tu tercer parcial: ')
examen_final = input('Escribe cuál es la nota de tu examen final: ')
trabajo_final = input('Escribe cuál es la nota de tu trabajo final: ')

nota_parciales = ((float(parcial1) + float(parcial2) + float(parcial3)) / (3)) * (0.55)
nota_examen = (float(examen_final) * (0.30))
nota_trabajo = (float(trabajo_final) * (0.15))

nota_final = (float(nota_parciales) + float(nota_examen) + float(nota_trabajo))

print ('')
print ('Tu nota final es ', str(nota_final))
