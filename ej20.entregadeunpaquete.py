"""
Programa: ej20.entregadeunpaquete.py
Fecha:25/10/2020
Autora: Virginia Ordoño

Propósito:
Una compañía de transporte internacional tiene servicio en algunos países de
América del Norte, América Central, América del Sur, Europa y Asia.
El costo por el servicio de transporte se basa en el peso del paquete y la zona a la que va dirigido.
lo anterior se muestra en la tabla:

ZONA	UBICACIÓN	COSTO/GRAMO
1	América del Norte	24.00 euros
2	América Central	20.00 euros
3	América del Sur	21.00 euros
4	Europa	10.00 euros
5	Asia	18.00 euros
Parte de su política implica que los paquetes con un peso superior a 5 kg no son transportados,
esto por cuestiones de logística y de seguridad.
Realice un algoritmo para determinar el cobro por la entrega de un paquete o, en su caso, el rechazo de la entrega.

Análisis:
- Pedimos al usuario el peso del paquete y la zona de destino.
- Si el paquete pesa más de 5kg, aparece un mensaje de que no puede ser transportado.
- En caso contrario, en función del destino se calculará el precio correspondiente.
- Variables: destination, kg, gr, rate.
- Sentencias: if, elif.
"""
print('A continuación tendrás que proporcionar unos datos para saber el coste final del envío.')

kg = ('Introduce el peso del paquete.')
destination = ('Introduce el lugar de destino.')

# Si el paquete pesa más de 5 kg, aparece el mensaje: no se puede enviar.
if kg > 5:
    print('El paquete no puede ser enviado ya que supera el peso máximo permitido.')

# En caso contrario y si el destino es América del Norte, aplicamos la tarifa correspondiente:
elif destination == 'América del Norte':
    gr = kg * 100
    rate = gr * 24
    print('El valor de envío es', rate, 'euros.')

# En caso contrario y si el destino es América Central, aplicamos la tarifa correspondiente:
elif destination == 'América Central':
    gr = kg * 100
    rate = gr * 20
    print('El valor de envío es', rate, 'euros.')

# En caso contrario y si el destino es América del Sur, aplicamos la tarifa correspondiente:
elif destination == 'América del Sur':
    gr = kg * 100
    rate = gr * 21
    print('El valor de envío es', rate, 'euros.')

# En caso contrario y si el destino es Europa, aplicamos la tarifa correspondiente:
elif destination == 'Europa':
    gr = kg * 100
    rate = gr * 10
    print('El valor de envío es', rate, 'euros.')

# En caso contrario y si el destino es Asia, aplicamos la tarifa correspondiente:
elif destination == 'Asia':
    gr = kg * 100
    rate = gr * 18
    print('El valor de envío es', rate, 'euros.')