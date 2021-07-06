
'''Análisis: Pediremos la velocidad de cada vehículo y la distancia entre ambos para calcular el tiempo que el de atrás
tardará en alcanzarlo. Variables: v1 (velocidad 1), v2 (velocidad 2), d (distancia), t (tiempo).
 Funciones: suma y división para calcular el tiempo'''

#La función print muestra el enunciado del texto.
print ('16. Dos vehículos viajan a diferentes velocidades (v1 y v2) y están distanciados por una distancia d.')
print ('El que está detrás viaja a una velocidad mayor. Se pide hacer un algoritmo para ingresar la distancia')
print ('entre los dos vehículos (km) y sus respectivas velocidades (km/h) y con esto determinar y mostrar')
print ('en qué tiempo (minutos) alcanzará el vehículo más rápido al otro.')
print('')

#Solicitamos la velocidad y la distancia de los dos vehículos.
velocidad1 = input ('Escribe la velocidad en km/h a la que viaja el vehículo que está delante: ')
velocidad2 = input ('Escribe la velocidad en km/h a la que viaja el vehículo que está detrás. Recuerda que esta velocidad '
            'debe ser mayor a la del vehículo 1: ')
d = input ('Escribe la distancia, en kilómetros, que hay entre los dos vehículos: ')

#Calculamos el tiempo que tardará en alcanzar un coche a otro con la función tiempo:
tiempo = (int(distancia) / (int(velocidad1 - velocidad2))

#Con la función print mostramos el tiempo que tardará el coche.
print ('El de atrás tardará', (tiempo))