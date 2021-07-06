'''Programa: EJ2.calcularperimetroyarea.py'''
'''Autora: Virginia Ordoño Bernier'''
'''Fecha:07/10/2020'''
'''Propósito: Calcular el perímetro y área de un rectángulo dada su base y su altura.'''

'''Análisis: mediante la función print pedimos la base y la altura al usuario. Después realizamos el cálculo
  del perímetro y el área según los datos facilitados anteriormente. Variables: base, altura'''

#La función print muestra el enunciado del ejercicio.
print ('2. Calcular el perímetro y área de un rectángulo dada su base y su altura.')
print ('')

#Pedimos datos al usuario.
base = float(input('Introduce el valor de la base del rectángulo: '))
altura = float(input('Introduce el valor de la altura del rectángulo: '))

#Realizamos la operación matemática correspondiente al perímetro y al área.
perimetro = 2*(base + altura)
area = base*altura
print ('')

#Con la función print mostramos el valor del perímetro y del área.
print ('El valor del perímetro es: ',str(int(perimetro)),'.')
print ('El valor del área es: ',str(int(area)),'.')


