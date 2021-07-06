'''Programa: EJ3.calcularhipotenusa.py'''
'''Autora: Virginia Ordoño Bernier'''
'''Fecha: 07/10/2020'''
'''Propósito: Dados los catetos de un triángulo rectángulo, calcular su hipotenusa.'''

'''Análisis: Mediante la función print pedimos el valor de los catetos al usuario. Importamos el módulo math 
para tener acceso a la operación de raíz cuadrada. Después realizamos el cálculo de la hipotenusa según 
los datos facilitados anteriormente. Variables: side_1, side_2, hypotenuse'''

#La función print muestra el enunciado del ejercicio.
print ('3. Dados los catetos de un triángulo rectángulo, calcular su hipotenusa.')
print ('')

#Mediante la función input pedimos el valor del cateto 1 en float.
side_1 = float (input('Dime el valor del cateto 1: '))

#Mediante la función input pedimos el valor del cateto 2 en float.
side_2 = float (input('Dime el valor del cateto 2: '))

#Importamos el módulo math para calcular la raíz cuadrada.
import math

#Con el valor de los catetos creamos la variable para calcular el valor de la hipotenusa.
hypotenuse = (float (math.sqrt((side_1**2) + (side_2**2))))
print ('')

#Usamos la función print para mostrar el valor de la hipotenusa.
print ("EL valor de la hipotenusa es: " + str(hypotenuse))
