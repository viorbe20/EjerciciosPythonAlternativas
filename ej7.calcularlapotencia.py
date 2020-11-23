"""
Programa: ej7.calcularlapotencia.py
Autora: Virginia Ordoño Bernier
Fecha:22/10/2020

Propósito:
Crear un algoritmo que dada la base y el exponente, calcule le potencia. Pueden darse 3 situaciones:
1. Exponente positivo. Solo se imprimirá la potencia.
2. Exponente 0. El resultado será 1.
3. Exponente negativo. El resultado es 1/potencia con el exponente positivo

Análisis:
- Pedimos al usuario el valor de 'base' y 'exponente'.
- Si 'exponente' es mayor que 0 aparece mensaje mostrando la operación de cálcula de potencia.
- Si 'exponente' es igual que 0 aparece mensaje: potencia = 1.
- En caso contrario, aparece mensaje: la potencia es 1/potencia con el exponente positivo.
- Variables: base, exponente.
- Secuencias: if, elif, else.
"""

print('Escribe una cantidad para la base y otra para el exponente, de manera que el programa calcule la potencia: ')

# Con input pedimos al usuario que ingrese el valor de la base y el exponente.
base = input('Introduce el valor de la base: ')
exponent = input('Introduce el valor del exponente: ')

# Con if determinamos que en caso de que el exponente sea positivo se realice la operación y con print mostramos
# la potencia.
if exponent > '0':
    print('La potencia es base^exponente.')

# Con elif determinamos que en caso de que el exponente sea 0 se imprima que la potencia es = 1.
elif exponent == '0':
    print('La potencia es 1.')

# Con elif determinamos que en caso de que el exponente sea positivo, el resultado sea 1/potencia.
else:
    print('La potencia es 1/(base^abs(exponente)')
