"""Programa: ej14.vinicultores.py
Fecha:24/10/2020
Autora: Virginia Ordoño

Propósito:
La asociación de vinicultores tiene como política fijar un precio inicial al kilo de uva, la cual se
clasifica en tipos A y B, y además en tamaños 1 y 2. Cuando se realiza la venta del producto, ésta es de un solo
tipo y tamaño, se requiere determinar cuánto recibirá un productor por la uva que entrega en un embarque,
considerando lo siguiente:
- Si es de tipo A, se le cargan 20 céntimos al precio inicial cuando es de tamaño 1; y 30 céntimos si es de tamaño 2.
- Si es de tipo B, se rebajan 30 céntimos cuando es de tamaño 1, y 50 céntimos cuando es de tamaño 2.
Realice un algoritmo para determinar la ganancia obtenida.

Análisis:
- Mediante input pedimos al usuairo el tipo y el tamaño de la uva y el precio de salida.
- En función del tipo y el tamaño añadimos o restamos el importe correspondiente para obtener el precio final.
- Variables: type, size, price, A1, A2, B1, B2.
- Sentencias: if, elif.
"""

print('A continuación el programa te pidará unos datos para obtener la ganancia obtenida.')

# Mediante la función input pedimos al usuario que introduzca el tipo y el tamaño de la uva.
type = input('Introduce si la uva es de tipo A o B: ')
size = input('Introduce si la uva es de tamaño 1 o 2: ')
price = int(input('Introduce el precio por kilo en céntimos, que inicialmente tiene la uva: '))

# Si la uva es tipo 'A1' anadimos 20 céntimos al precio inicial e imprimimos un mensaje con la cantidad final.
if type == 'A' and size == '1':
    A1 = price + 20
    print(f"La ganancia de la uva A1 es", A1, ".")

# Si la uva es tipo 'A2' anadimos 30 céntimos al precio inicial e imprimimos un mensaje con la cantidad final.
elif type == 'A' and size == '2':
    A2 = price + 30
    print(f"La ganancia de la uva A2 es", A2, ".")

# Si la uva es tipo 'B1' restamos 30 céntimos al precio inicial e imprimimos un mensaje con la cantidad final.
elif type == 'B' and size == '1':
    B1 = price - 30
    print(f"La ganancia de la uva B1 es", B1, ".")

# Si la uva es tipo 'B2' restamos 50 céntimos al precio inicial e imprimimos un mensaje con la cantidad final.
elif type == 'B' and size == '2':
    B2 = price - 50
    print(f"La ganancia de la uva B2 es", B2, ".")
