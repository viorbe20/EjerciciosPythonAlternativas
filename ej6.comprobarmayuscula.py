"""
Programa: ej6.comprobarmayuscula.py
Fecha:22/10/2020
Autora: Virginia Ordoño Bernier

Propósito:
Crear un algoritmo que al introducir una cadena, nos diga si es o no mayúscula.

Análisis:
- Pedimos al usuario una letra.
- Importamos módulo string y usamos la constante string.ascii_uppercase para que nos devuelva mayúsculas.
- Con lo que nos devuelve el parámetro, añadimos los caracteres que consideremos que falten mediante concatenación.
- Aplicamos el método 'find' en la cadena, de forma que nos muestra la posición donde se encuentra, en este caso la
mayúscula, dentro de cadena. En este caso muestra el mensaje: es mayúscula.
- Si no la encuentra retorna -1 y muestra mensaje: no es mayúscula.
- Variables: cad, capital, letter.
- Sentencias: if, else.
- Módulo: string.
- Constante: ascii_uppercase.
- Método: find.
"""

print('Escribe una letra para que el programa determine si es o no mayúscula: ')

# Con input pedimos al usuario que ingrese una letra.
cad = input('Introduce una letra para comprobar si es mayúscula: ')

# Importamos el módulo string para luego usar un parámetro.
import string

# Usamos el parámetro string.ascii_uppercase que retorna las letras en mayúsculas y concatenamos
# aquellas que consideramos que faltan.
capital = string.ascii_uppercase + "ÁÉÍÓÚÑÜ"

# Creamos la variable letter a la que le damos el valor obtenido del parámetro anterior. Si el resultado es -1,
# significa que la letra no es mayúscula. Si nos da un número, nos marca la posición que ocupa en la cadena y
# por tanto quiere decir que se encuentra en la cadena y que es mayúscula.
letter = capital.find(cad)

# Con if decimos que si el valor de la variable letter es -1
if letter == -1:
    print('La letra introducida no es mayúscula.')
else:
    print('La letra introducida es mayúscula.')
