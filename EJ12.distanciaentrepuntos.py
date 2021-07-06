'''Programa: EJ12.distanciaentrepuntos.py'''
'''Autora: Virginia Ordoño Bernier'''
'''Fecha:13/10/2020'''
'''Propósito: Mostrar la distancia entre dos puntos en un plano.'''

'''Análisis: Solicitamos el valor de cada de 'x' e 'y'. Usamos el módulo math para solicitar la raiz cuadrada.
Calculamos las medias en función del porcentaje indicado para cada trabajo. Variables: N1, N2, distancia, valor_absoluto'''

#Con print mostramos el enunciado.
print ('12. Pide al usuario dos pares de números x1,y2 y x2,y2, que representen dos puntos en el plano.')
print ('Calcula y muestra la distancia entre ellos.')

X1 = input ('Dime la coordenada X de un punto en un plano: ')
Y1_2 = input ('Dime la coordenada Y del mismo punto: ')
X2 = input ('Dime la coordenada X del segundo punto: ')

'Importamos el módulo math para calcular la raíz cuadrada.'
import math

distancia = int (math.sqrt((int(X2) - int(X1))**2 + (int(Y1_2) - int(Y1_2))**2))

print ('Distancia' , str(distancia))
