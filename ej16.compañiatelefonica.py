"""
Programa: ej16.compañiatelefonica.py
Fecha:25/10/2020
Autora: Virginia Ordoño

Propósito: La política de cobro de una compañía telefónica es: cuando se realiza una llamada, el cobro es
por el tiempo que ésta dura, de tal forma que:
- 1 a 5 minutos: 1 euro.
- 6 a 8 minutos: 80 céntimos.
- 9 y 10 minutos: 70 céntimos.
- 11 o más minutos, 50 céntimos.
Además, se carga un impuesto de 3 % cuando es domingo, y si es otro día, en turno de mañana, 15 %,
y en turno de tarde, 10 %. Realice un algoritmo para determinar cuánto debe pagar por cada concepto
una persona que realiza una llamada..

Análisis:
- Pedimos al usuario la duración de la llamada en minutos, el día en que se realizó y el horario.
- Calculamos el valor de la llamada en función de los minutos, el día y la parte del día y aplicamos los
valores correspondientes.
- Variables: minutes, day, shift, total.
- Sentencias: if, elif.
"""
print('A continuación el programa te pedirá unos datos y te dirá cuánto tienes que pagar por una llamada telefónica.')

# Pedimos al usuario los minutos de duración de la llama.
minutes = int(input('Por favor, introduce los minutos de duración de la llamada: '))
day = input('Por favor, introduce el día de la semana en el que se realizó la llamada: ')
shift = input('Por favor, indica en qué horario se realizó la llamada escribibiendo mañana, tarde o noche: ')

# Si la duración de la llamada está entre 1 y 5 minutos y es en domingo, calculamos el valor correspondiente por minuto.
if 1 <= minutes <= 5 and day == 'domingo':
    total = int(100 + (100*0.03))
    print('El importe a pagar es', total, 'céntimos.')

# Si la duración de la llamada está entre 1 y 5 minutos y es un día diferente a domingo en el período de la noche,
# calculamos el valor correspondiente por minuto.
elif day in ('lunes', 'martes', 'miércoles', 'jueves', 'viernes', 'sábado') and shift == 'noche':
    total = 100
    print('El importe a pagar es', total, 'céntimos.')

# Si la duración de la llamada está entre 1 y 5 minutos y es un día diferente a domingo en el período de la tarde,
# calculamos el valor correspondiente por minuto.
elif day in ('lunes', 'martes', 'miércoles', 'jueves', 'viernes', 'sábado') and shift == 'tarde':
    total = int(100 + (100*0.10))
    print('El importe a pagar es', total, 'céntimos.')

# Si la duración de la llamada está entre 1 y 5 minutos y es un día diferente a domingo en el período de la noche,
# calculamos el valor correspondiente por minuto.
elif day in ('lunes', 'martes', 'miércoles', 'jueves', 'viernes', 'sábado') and shift == 'mañana':
    total = int(100 + (100*0.15))
    print('El importe a pagar es', total, 'céntimos.')

# Si la duración de la llamada está entre 6 y 8 minutos y es en domingo, calculamos el valor correspondiente por minuto.
if 6 <= minutes <= 8 and day == 'domingo':
    total = int(80 + (80*0.03))
    print('El importe a pagar es', total, 'céntimos.')

# Si la duración de la llamada está entre 6 y 8 minutos y es un día diferente a domingo en el período de la noche,
# calculamos el valor correspondiente por minuto.
elif day in ('lunes', 'martes', 'miércoles', 'jueves', 'viernes', 'sábado') and shift == 'noche':
    total = 80
    print('El importe a pagar es', total, 'céntimos.')

# Si la duración de la llamada está entre 6 y 8 minutos y es un día diferente a domingo en el período de la tarde,
# calculamos el valor correspondiente por minuto.
elif day in ('lunes', 'martes', 'miércoles', 'jueves', 'viernes', 'sábado') and shift == 'tarde':
    total = int(80 + (80*0.10))
    print('El importe a pagar es', total, 'céntimos.')

# Si la duración de la llamada está entre 6 y 8 minutos y es un día diferente a domingo en el período de la noche,
# calculamos el valor correspondiente por minuto.
elif day in ('lunes', 'martes', 'miércoles', 'jueves', 'viernes', 'sábado') and shift == 'mañana':
    total = int(80 + (80*0.15))
    print('El importe a pagar es', total, 'céntimos.')

# Si la duración de la llamada está entre 9 y 10 minutos y es en domingo, calculamos el valor correspondiente por
# minuto.
if 9 <= minutes <= 10 and day == 'domingo':
    total = int(70 + (70*0.03))
    print('El importe a pagar es', total, 'céntimos.')

# Si la duración de la llamada está entre 9 y 10 minutos y es un día diferente a domingo en el período de la noche,
# calculamos el valor correspondiente por minuto.
elif day in ('lunes', 'martes', 'miércoles', 'jueves', 'viernes', 'sábado') and shift == 'noche':
    total = 70
    print('El importe a pagar es', total, 'céntimos.')

# Si la duración de la llamada está entre 9 y 10 minutos y es un día diferente a domingo en el período de la tarde,
# calculamos el valor correspondiente por minuto.
elif day in ('lunes', 'martes', 'miércoles', 'jueves', 'viernes', 'sábado') and shift == 'tarde':
    total = int(70 + (70*0.10))
    print('El importe a pagar es', total, 'céntimos.')

# Si la duración de la llamada está entre 9 y 10 minutos y es un día diferente a domingo en el período de la noche,
# calculamos el valor correspondiente por minuto.
elif day in ('lunes', 'martes', 'miércoles', 'jueves', 'viernes', 'sábado') and shift == 'mañana':
    total = int(70 + (70*0.15))
    print('El importe a pagar es', total, 'céntimos.')

# Si la duración de la llamada es mayor que 10 minutos y es en domingo, calculamos el valor correspondiente por minuto.
if minutes < 10 and day == 'domingo':
    total = int(50 + (50*0.03))
    print('El importe a pagar es', total, 'céntimos.')

# Si la duración de la llamada es mayor que 10 minutos y es un día diferente a domingo en el período de la noche,
# calculamos el valor correspondiente por minuto.
elif day in ('lunes', 'martes', 'miércoles', 'jueves', 'viernes', 'sábado') and shift == 'noche':
    total = 50
    print('El importe a pagar es', total, 'céntimos.')

# Si la duración de la llamada es mayor que 10 minutos y es un día diferente a domingo en el período de la tarde,
# calculamos el valor correspondiente por minuto.
elif day in ('lunes', 'martes', 'miércoles', 'jueves', 'viernes', 'sábado') and shift == 'tarde':
    total = int(50 + (50*0.10))
    print('El importe a pagar es', total, 'céntimos.')

# Si la duración de la llamada es mayor que 10 minutos y es un día diferente a domingo en el período de la noche,
# calculamos el valor correspondiente por minuto.
elif day in ('lunes', 'martes', 'miércoles', 'jueves', 'viernes', 'sábado') and shift == 'mañana':
    total = int(50 + (50*0.15))
    print('El importe a pagar es', total, 'céntimos.')
