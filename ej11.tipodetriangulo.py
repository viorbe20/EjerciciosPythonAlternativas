"""
Programa: ej11.tipodetriangulo.py
Fecha:24/10/2020
Autora: Virginia Ordoño

Propósito:
Programa que lea 3 datos de entrada A, B y C, correspondientes a las dimensiones de los lados de
un triángulo. El programa debe determinar qué tipo de triangulo es, teniendo en cuenta los siguiente:
- Si se cumple Pitágoras entonces es triángulo rectángulo.
- Si sólo dos lados del triángulo son iguales entonces es isósceles.
- Si los 3 lados son iguales entonces es equilátero.
- Si no se cumple ninguna de las condiciones anteriores, es escaleno.

Análisis:
- Pedimos al usuario la longitud de los tres lados para que en función de la longitud de dichos lados y comparándolos
entre ellos, establezcamos el tipo de triángulo que es.
- Variables: side1, side2, side3.
- Sentencias: if, elif, else.
"""

print('Tendrás que escribir los datos que te pida el programa para que te diga el tipo de triángulo.')

# Mediante la función input pedimos al usuario que introduzca tres datos correspondientes a los lados de un triángulo.
side1 = int(input('Introduce la longitud de un lado: '))
side2 = int(input('Introduce la longitud del segundo lado: '))
side3 = int(input('Introduce la longitud del último lado: '))

# La secuencia if indica que si el triángulo cumple con el teorema de Pitágoras el triángulo es rectángulo:
if side1**2 == (side2**2)+(side3**2) or side2**2 == (side1**2)+(side3**2) or side3**2 == (side1**2)+(side2**2):
    print('Es un triángulo rectángulo.')

# La secuencia elif indica que si los dos lados tienen la misma longitud y el tercero no, es un triángulo isósceles.
elif side1 == side2 != side3 or side2 == side3 != side1 or side1 == side3 != side2:
    print('Es un triángulo isósceles.')

# La secuencia elif indica que si los tres lados tienen la misma longitud, se trata de un triángulo equilátero.
elif side1 == side2 == side3:
    print('Es un triángulo equilátero.')

# La secuencia else indica que en el resto de los casos, se trata de un triángulo escaleno.
else:
    print('Es un triángulo escaleno.')
