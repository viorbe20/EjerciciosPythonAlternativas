"""
Programa: ej2.lineasdelultimoprograma.py
Autora: Virginia Ordoño Bernier
Fecha:22/10/2020

Propósito: Crear un algoritmo que indique qué líneas del último programa (y en qué orden) se ejecutarán para cada uno
de los siguientes casos:
1) a = 2 y b = 6
2) a = 0 y b = 3
3) a = 0 y b = -3
4) a = 0 y b = 0

Análisis:
- Pedimos al usuario el valor de 'a' y 'b'.
- Comparamos 'a' con 0, siendo x = -b / a.
- Si 'a' es diferente a 0, aparece un mensaje con el valor de 'x'.
- Si 'a' es igual a 0 y 'b' diferente a 0, aparece un mensaje de ecuación sin solución.
- Si 'b' es igual a 0, la ecuación tiene infinitas soluciones.
- Variables: 'a', 'b'.
- Secuencias: if.
"""

print('Programa para la resolución de la ecuación ax+b=0.')

# Solicitamos el valor de a y b:
a = float(input('Introduce el valor de a: '))
b = float(input('Introduce el valor de b: '))

# Con la sentencia if determinamos que si a diferente a 0, el resultado es x.
if a != 0:
    x = -b / a
    print('El valor de x es', x, '.')

# Con la sentencia if determinamos que el valor de 'a' que es cero, va a depender de si el valor de 'b' es
# diferente a cero. En ese caso imprime un mensaje de no tiene solución.
if a == 0:
    if b != 0:
        print('La ecuación no tiene solución.')

# Con la sentencia if determinamos que el valor de 'a' que es cero, va a depender de si el valor de 'b' es
# igual a cero. En ese caso imprime un mensaje de que la ecuación tiene infinitas soluciones.
    if b == 0:
        print('La ecuación tiene infinitas soluciones.')

'''
Análisis final
1) a = 2 y b = 6. 
if_1. Se para aquí ya que el valor de 'a' es diferente a 0 y por tanto hace un print porque 
al ser una expresión lógica verdadera la ejecuta, dando por tanto el valor de x.

2) a = 0 y b = 3. 
_if_1. El valor de 'a' es igual a 0 por lo que pasa a if_2.
_if_3. Se para aquí porque 'b' es diferente a 0 y hace un print. En este caso la ecuación no tiene solución porque es 
una ecuación dividida entre 0 es una excepción en Python.

3) a = 0 y b = -3
_if_1. El valor de a es igual a 0 por lo que pasa a if_2.
_if_3. Se para aquí porque b es diferente a 0 y hace un print. En este caso la ecuación no tiene solución porque es 
una ecuación dividida entre 0 es una excepción en Python.

4) a = 0 y b = 0
_if_1. El valor de 'a' es igual a 0 por lo que pasa a if_2.
_if_3. Pasa al siguiente if porque es 'b' es igual a 0.
_if_4. Se detiene aquí porque 'b' es igual a 0.En este caso se imprime un mensaje de que la ecuación
tiene infinitas soluciones ya que ambos elementos tienen valor 0.
'''