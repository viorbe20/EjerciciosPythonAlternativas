"""
Programa: ej3.vocalonovocal.py
Autora: Virginia Ordoño Bernier
Fecha:04/11/2020
_______________________________________________________________________________________________________________________
Propósito
_______________________________________________________________________________________________________________________
Pedir caracteres al ususario y que el programa responda si es vocal o no.
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
character = input('Introduce un caracter para que el programa te diga si es una vocal o no: ')

while len(character) == 1:

        if character in ("'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O, 'U'"):
                print('El carácter introducido SÍ es una vocal.')
                character = input("Introduce otro carácter:")

        else:
                print('El carácter introducido NO es una vocal.')
                character = input("Introduce otro carácter:")

else:
    print('Por favor, introduce solo un carácter: ')

