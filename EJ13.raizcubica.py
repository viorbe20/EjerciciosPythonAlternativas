'''Programa: EJ13.raizcubica.py'''
'''Autora: Virginia Ordoño Bernier'''
'''Fecha:12/10/2020'''
'''Propósito: Obtener la raíz cúbica de un número.'''

'''Análisis: Solicitamos el valor de cada de 'x' e 'y'. Usamos el módulo math para solicitar la raiz cuadrada.
Calculamos las medias en función del porcentaje indicado para cada trabajo. Variables: N1, N2, distancia, valor_absoluto'''

print ('13. Realizar un algoritmos que lea un número y que muestre su raíz cuadrada y su raíz cúbica.')
print ('Python no tiene ninguna función predefinida que permita calcular la raíz cúbica, ¿cómo se puede calcular?')

#Pedimos datos
numero = input('Dime un número para calcular su raíz cúbica: ')

#Operaciones
raiz_cubica = (int(numero) ** (1/3))

#Resultado
print ('La raíz cúbica de' ,str(numero) ,'es' ,str(float(raiz_cubica)))