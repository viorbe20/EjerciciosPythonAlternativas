"""
Programa: ej13.desglosedebilletes.py
Fecha:24/10/2020
Autora: Virginia Ordoño

Propósito:
Programa que calcule el desglose mínimo en billetes y monedas de una cantidad exacta de euros.
Hay billetes de 500, 200, 100, 50, 20, 10 y 5€ y monedas de 2 y 1€. Por ejemplo, si deseamos conocer el desglose
de 434€, el programa mostrará por pantalla el siguiente resultado:
- 2 billetes de 200 euros.
- 1 billete de 20 euros.
- 1 billete de 10 euros.
- 2 monedas de 2 euros.

Análisis:
- Pedimos al usuario la cantidad total de euros.
- Dividimos la cantidad entre la cantidad del billete y calculamos el número de billetes.
- Así sucesivamente.
- Secuencias: if.
- Variables: money, note 500, note200, note100, note50, note20, note10, note5, coin2, coin1.
"""

# La función print muestra el enunciado del ejercicio.
print('A continuación el programa te pidará que introduzcas un cantidad en euros para decirte a cuántos billetes '
      'y monedas corresponde.')

# Mediante la función input pedimos al usuario que introduzca la cantidad exacta de euros.
money = int(input('Introduce una cantidad exacta de euros: '))

# Si la división entera de la cantidad es diferente a 0, el número de billetes es la división entera. Le restamos a
# la cantidad inicial la multiplicación entre el número de billetes de 500 por 500.
if money // 500 != 0:
    note500 = money // 500
    print(f"{note500} billetes de 500 euros")
    money -= note500 * 500

# Si la división entera de la cantidad es diferente a 0, el número de billetes es la división entera. Le restamos a
# la cantidad inicial la multiplicación entre el número de billetes de 200 por 200.
if money // 200 != 0:
    note200 = money // 200
    print(f"{note200} billetes de 200 euros")
    money -= note200 * 200

# Si la división entera de la cantidad es diferente a 0, el número de billetes es la división entera. Le restamos a
# la cantidad inicial la multiplicación entre el número de billetes de 100 por 100.
if money // 100 != 0:
    note100 = money // 100
    print(f"{note100} billetes de 100 euros")
    money -= note100 * 100

# Si la división entera de la cantidad es diferente a 0, el número de billetes es la división entera. Le restamos a
# la cantidad inicial la multiplicación entre el número de billetes de 50 por 50.
if money // 50 != 0:
    note50 = money // 50
    print(f"{note50} billetes de 50 euros")
    money -= note50 * 50

# Si la división entera de la cantidad es diferente a 0, el número de billetes es la división entera. Le restamos a
# la cantidad inicial la multiplicación entre el número de billetes de 20 por 20.
if money // 20 != 0:
    note20 = money // 20
    print(f"{note20} billetes de 20 euros")
    money -= note20 * 20

# Si la división entera de la cantidad es diferente a 0, el número de billetes es la división entera. Le restamos a
# la cantidad inicial la multiplicación entre el número de billetes de 10 por 10.
if money // 10 != 0:
    note10 = money // 10
    print(f"{note10} billetes de 10 euros")
    money -= note10 * 10

# Si la división entera de la cantidad es diferente a 0, el número de billetes es la división entera. Le restamos a
# la cantidad inicial la multiplicación entre el número de billetes de 5 por 5.
if money // 5 != 0:
    note5 = money // 5
    print(f"{note5} billetes de 5 euros")
    money -= note5 * 5

# Si la división entera de la cantidad es diferente a 0, el número de monedas es la división entera. Le restamos a
# la cantidad inicial la multiplicación entre el número de monedas de 2 por 2.
if money // 2 != 0:
    coin2 = money // 2
    print(f"{coin2} monedas de 2 euros")
    money -= coin2 * 2

# Si la división entera de la cantidad es diferente a 0, el número de monedas es la división entera. Le restamos a
# la cantidad inicial la multiplicación entre el número de monedas de 1 por 1.
if money // 1 != 0:
    coin1 = money // 1
    print(f"{coin1} monedas de 1 euros")
    money -= coin1 * 1
