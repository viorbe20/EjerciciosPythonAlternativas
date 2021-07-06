"""
Programa: ej6.resultadodelapotencia.py
Autora: Virginia Ordoño Bernier
Fecha:04/11/2020
_______________________________________________________________________________________________________________________
Propósito
_______________________________________________________________________________________________________________________
Escribe un programa que dados dos números, uno real (base) y un entero positivo (exponente),
saque por pantalla el resultado de la potencia. No se puede utilizar el operador de potencia.
_______________________________________________________________________________________________________________________
Análisis
_______________________________________________________________________________________________________________________
- Pedimos al usuario que introduzca un carácter.
_______________________________________________________________________________________________________________________
Algoritmo
_______________________________________________________________________________________________________________________
- Variables:
- Secuencias:
- Bucles:
"""
# Inicializamos variables
# Esta variable, será uno elevado al exponente y luego lo multiplicamos por la base introducida.
potencia = 1

# Pedimos datos.
base = float(input('Introduce la base: '))
exponent = int(input('Introduce el exponente: '))

# Usamos guión porque la variable no será necesaria, solo necesitamos que el ciclo se ejecute.
# La variable _ coge el valor absoluto del exponente.
# La potencia se multiplica por la base, el número de veces que indique el exponente.
for _ in range(abs(exponent)):
    potencia *= base

# Exponente negativo es 1 partido por la potencia.
if exponent < 0:
    potencia = 1/potencia

# Salida.
print(f"\n{base} elevado a {exponent} es {potencia}")
