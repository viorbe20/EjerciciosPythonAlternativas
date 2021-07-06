'''Programa: EJ20.totaldinero.py'''
'''Autora: Virginia Ordoño Bernier'''
'''Fecha:12/10/2020'''
'''Propósito: Obtener la cantidad total de dinero.'''

'''Análisis: Solicitamos la cantidad exacta de monedas y su valor para calcular el valor final'''

#La función print muestra el enunciado del texto.
print ('20. Diseñar un algoritmo que nos diga el dinero que tenemos (en euros y céntimos)')
print ('después de pedirnos cuantas monedas tenemos de 2e, 1e, 50 céntimos, 20 céntimos o 10 céntimos.')

#Pedir datos.
monedas_2e = input ('Cuántas monedas tienes de 2 euros: ')
monedas_1e = input ('Cuántas monedas tienes de 1 euro: ')
monedas_50c = input ('Cuántas monedas tienes de 50 céntimos: ')
monedas_20c = input ('Cuántas monedas tienes de 20 céntimos: ')
monedas_10c = input ('Cuántas monedas tienes de 10 céntimos: ')

#Cálculos.
centimos_monedas_2e = (int(monedas_2e)*(200))
centimos_monedas_1e = (int(monedas_1e)*(100))
centimos_monedas_50c = (int(monedas_50c)*(50))
centimos_monedas_20c = (int(monedas_20c)*(20))
centimos_monedas_10c = (int(monedas_10c)*(10))

total_centimos = (int(centimos_monedas_2e) + int(centimos_monedas_1e) + int(centimos_monedas_50c) +
                  int (centimos_monedas_20c) + int(centimos_monedas_10c))

euros = int(total_centimos) // 100
centimos_resto = int(total_centimos) % 100

#Resultados.
print ('Tienes', (euros), 'euros y', (centimos_resto), 'céntimos.')
