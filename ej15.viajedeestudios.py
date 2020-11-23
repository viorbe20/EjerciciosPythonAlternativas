"""Programa: ej15.viajedeestudios.py
Fecha:24/10/2020
Autora: Virginia Ordoño

Propósito: El director de una escuela está organizando un viaje de estudios, y requiere determinar cuánto debe cobrar
a cada alumno y cuánto debe pagar a la compañía de viajes por el servicio. La forma de cobrar es la siguiente:
- Si son 100 alumnos o más, el costo por cada alumno es de 65 euros;
- De 50 a 99 alumnos, el costo es de 70 euros,
- De 30 a 49, de 95 euros,
- Si son menos de 30, el costo de la renta del autobús es de 4000 euros,  sin importar el número de alumnos.
Realiza un programa que determine el pago a la compañía de autobuses  y lo que debe pagar cada alumno por el viaje.

Análisis:
- Pedimos al usuario el número de alumnos que irán al viaje.
- Calcularemos el número de estudiantes para saber con esa cantidad, lo que tiene que pagar cada estudiante y lo que
hay que pagar a la agencia de viajes.
- Sentencias: if, elif, else.
- Variables: students, agency, ps1, ps2, ps3, ps4.
"""

# La función print muestra el enunciado del ejercicio.
print('A continuación el programa te pidará el número de alumnos que van al viaje para determinar cuánto debes cobrar '
      'a cada alumno y cuánto debes pagar a la compañía de viajes.')

# Mediante la función input pedimos al usuario que introduzca el número de alumnos que van al viaje.
students = int(input('Introduce el número de alumnos que van al viaje: '))

# Con la sentencia if establecemos lo que pagará cada alumno si van 100 o más al viaje. Según esa cantidad, calculamos
# el valor que debemos pagar a la agencia.
if students >= 100:
    ps1 = students * 65
    print('Cada alumno debe pagar', ps1, 'euros.')
    agency = students * ps1
    print('Debes pagar a la agencia', agency, 'euros.')

# Con la sentencia elif establecemos lo que pagará cada alumno si van entre 99 y 50 al viaje. Según esa cantidad,
# calculamos el valor que debemos pagar a la agencia.
elif 99 >= students <= 50:
    ps2 = students * 70
    print('Cada alumno debe pagar', ps2, 'euros.')
    agency = students * ps2
    print('Debes pagar a la agencia', agency, 'euros.')

# Con la sentencia elif establecemos lo que pagará cada alumno si van entre 49 y 30 al viaje. Según esa cantidad,
# calculamos el valor que debemos pagar a la agencia.
elif 49 >= students <= 30:
    ps3 = students * 95
    print('Cada alumno debe pagar', ps3, 'euros.')
    agency = students * ps3
    print('Debes pagar a la agencia', agency, 'euros.')

# Con la sentencia elif establecemos lo que pagará cada alumno si van entre 29 y 1 al viaje. Según esa cantidad,
# calculamos el valor que debemos pagar a la agencia.
elif 29 >= students <= 1:
    ps4 = 4000 / students
    print('Cada alumno debe pagar', ps4, 'euros.')
    agency = 4000
    print('Debes pagar a la agencia', agency, 'euros.')

# Con la sentencia else aparece un mensaje de error, en caso de que el usuario introduzca una cantidad errónea.
else:
    print('El carácter introducido no es correcto.')
