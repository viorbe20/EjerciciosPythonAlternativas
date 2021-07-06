"""
Programa: ej5.limitedeunintervalo.py
Autora: Virginia Ordoño Bernier
Fecha:04/11/2020
_______________________________________________________________________________________________________________________
Propósito
_______________________________________________________________________________________________________________________
Una persona adquirió un producto para pagar en 20 meses. El primer mes pagó 10 €, el segundo 20 €, el tercero 40 €
y así sucesivamente. Realizar un programa para determinar cuánto debe pagar mensualmente y
el total de lo que pagará después de los 20 meses.
_______________________________________________________________________________________________________________________
Análisis
_______________________________________________________________________________________________________________________
- Pedimos al usuario que introduzca un carácter.
_______________________________________________________________________________________________________________________
Algoritmo
_______________________________________________________________________________________________________________________
- Variables: PAGO_
- Secuencias:
- Bucles:
"""

# Inicializamos las variables.
#month contiene el valor del pago del primer mes.
month_pay = 10

# Total es un acumulador de los importes mensuales.
total = 0

# Ciclo for donde vamos a obtener el número de mes con el pago correspondiente.
for month in range (1, 21):
    print(f"Pago mes {month:2d}: {month_pay:2d}€")

    # Total va acumulando la cantidad del mes anterior.
    total += month_pay

    # month_pay lo multiplicamos por dos para darle el valor del mes siguiente.
    month_pay *= 2

# Pago total
print(f"\n Total a pagar: {total: d}€")