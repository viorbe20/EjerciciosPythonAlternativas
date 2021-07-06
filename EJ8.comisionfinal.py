'''Programa: EJ8.comisionfinal.py'''
'''Autora: Virginia Ordoño Bernier'''
'''Fecha:12/10/2020'''
'''Propósito: Un vendedor recibe un sueldo base más un 10% extra por comisión de sus ventas, el vendedor desea saber 
cuánto dinero obtendrá por concepto de comisiones por las tres ventas que realiza en el mes y el total que recibirá 
en el mes tomando en cuenta su sueldo base y comisiones.'''

'''Análisis: Mediante la función input solicitamos al usuario el valor de su sueldo base y mediante una variable 
calculamos la comisión. Variables_ sueldo_base, comision'''

#La función print muestra el enunciado del ejercicio.
print ('8. Un vendedor recibe un sueldo base más un 10% extra por comisión de sus ventas, '
       'el vendedor desea saber cuanto dinero obtendrá por concepto de comisiones por las tres ventas que realiza '
       'en el mes y el total que recibirá en el mes tomando en cuenta su sueldo base y comisiones.')
print('')

#Con la función input solicitamos al usuario el valor de su sueldo base y creamos una variable.
sueldo_base = input('Escribe el valor de tu sueldo base: ')
ventas = input('Escribe el valor total de tus ventas: ')

#En función del valor anterior calculamos la comisión que obtendría al mes.
total_ventas = round((float(ventas) /100) * 3)

#Usamos la función print para mostrar la comisión que ganaría al mes.
print('Con un sueldo base de ' + str(sueldo_base) + ' euros' + ' la comisión mensual que corresponde son ' + str(comision) + ' euros.')
print ('Tu sueldo bruto será ' + str(sueldo_base) + str(comision) + ' euros.')


'''rEVISAR Y HACER DE NUEVO'''





