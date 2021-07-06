'''Programa: EJ18.pediriniciales.py'''
'''Autora: Virginia Ordoño Bernier'''
'''Fecha:12/10/2020'''
'''Propósito: Obtener iniciales del nombre y apellidos.'''

'''Análisis: Solicitamos el valor de un número obtendremos el número invertido'''

#La función print muestra el enunciado del texto.
print ('18. Pedir el nombre y los dos apellidos de una persona y mostrar las iniciales.')

#Solicitar datos
nombre = input ('Escribe tu nombre: ')
apellido_1 = input ('Escribe tu primer apellido: ')
apellido_2 = input ('Escribe tu segundo apellido: ')

#Operaciones
inicial_1 = (nombre [0])
inicial_2 = (apellido_1 [0])
inicial_3 = (apellido_2 [0])

#Resultados
iniciales = ((inicial_1)+(inicial_2)+(inicial_3))
print (iniciales)




