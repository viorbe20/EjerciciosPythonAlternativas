'''Programa: EJ4.operaciones2numeros.py'''
'''Autora: Virginia Ordoño Bernier'''
'''Fecha:07/10/2020'''
'''Propósito: Dados dos números, mostrar la suma, resta, división y multiplicación de ambos.'''

'''Análisis: Mediante la función print pedimos el valor de dos números al usuario. Después realizamos 
las operaciones indicadas con los datos facilitados anteriormente. Variables: number_1, number_2.'''

#La función print muestra el enunciado del ejercicio.
print ('4. Dados dos números, mostrar la suma, resta, división y multiplicación de ambos.')
print ('')

#Mediante la función input pedimos el valor del número 1 en float al usuario.
number_1 = float (input ('Dame el valor del número 1: '))

#Mediante la función input pedimos el valor del número 2 en float al usuario.
number_2 = float (input ('Dame el valor del número 2: '))
print ('')

#Mediante la función print obtenemoslas siguientes operaciones: suma, resta, multiplicación y división en números float.
print ('Operaciones con', str(int(number_1)) ,'y' ,str(int(number_2)),'.','Resultado en números decimales:')
print (number_1 ,'+', number_2 ,'=' , (float(number_1+number_2)))
print (number_1 ,'-', number_2 ,'=' , (float(number_1-number_2)))
print (number_1 ,'/', number_2 ,'=' , (float(number_1/number_2)))
print (number_1 ,'x', number_2 ,'=' , (float(number_1*number_2)))
print ('')

#Mediante la función print obtenemoslas siguientes operaciones: suma, resta, multiplicación y división en números enteros.
print ('Operaciones con', str(int(number_1)) ,'y' ,str(int(number_2)),'.','Resultado en números enteros:')
print (number_1 ,'+', number_2 ,'=' , (int(number_1+number_2)))
print (number_1 ,'-', number_2 ,'=' , (int(number_1-number_2)))
print (number_1 ,'/', number_2 ,'=' , (int(number_1/number_2)))
print (number_1 ,'x', number_2 ,'=' , (int(number_1*number_2)))