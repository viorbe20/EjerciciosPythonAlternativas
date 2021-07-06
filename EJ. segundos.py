'''Programa: EJ.segundos.py'''

segundos = input ('Escribe el número de segundos: ')

minutos = int(segundos) // 60
segundos_resto = int(segundos) % 60
horas = int(minutos//60)
minutos_resto = int (minutos) % 60


print ((horas), (minutos_resto), (segundos_resto))

