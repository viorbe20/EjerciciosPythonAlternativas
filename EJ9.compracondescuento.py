'''Programa: EJ9.compracondescuento.py'''
'''Autora: Virginia Ordoño Bernier'''
'''Fecha:12/10/2020'''
'''Propósito: Una tienda ofrece un descuento del 15% sobre el total de la compra y un cliente desea saber cuanto deberá pagar finalmente por su compra.'''

'''Análisis: Mediante input solicitamos al usuario el valor total de la compra. Calculamos el porcentaje del descuento 
lo aplicamos para mostrar el resultado final mediante print. Variables: total_inicial, descuento, total_final.'''

#La función print muestra el enunciado del ejercicio.
print ('9. Una tienda ofrece un descuento del 15% sobre el total de la compra y un cliente desea saber cuánto deberá pagar finalmente por su compra.')
print('')

#Con la función input solicitamos al usuario el valor de su compra  y creamos una variable.
total_inicial = input('Escribe cuál es el valor total de tu compra: ')

#Según el valor anterior calculamos el porcentaje del descuento.
descuento = (float(total_inicial) * (0.015))

#Aplicamos el descuento al total de la compra.
total_final = (float(total_inicial) - float(descuento))

#Usamos la función print para mostrar la comisión que ganaría al mes.
print('Si el valor total de tu compra son ', str(total_inicial), ' euros', ' el valor final con el descuento será ',
      str(total_final), ' euros.')





