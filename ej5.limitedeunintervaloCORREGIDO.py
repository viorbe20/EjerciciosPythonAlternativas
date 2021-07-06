"""
Programa: ej5.limitedeunintervalo.py
Autora: Virginia Ordoño Bernier
Fecha:04/11/2020
_______________________________________________________________________________________________________________________
Propósito
_______________________________________________________________________________________________________________________
Escribe un programa que pida el limite inferior y superior de un intervalo. Si el límite inferior es mayor que
el superior lo tiene que volver a pedir. A continuación se van introduciendo números hasta que introduzcamos el 0.
Cuando termine el programa dará las siguientes informaciones:
- La suma de los números que están dentro del intervalo (intervalo abierto).
- Cuantos números están fuera del intervalo.
- Informa si hemos introducido algún número igual a los límites del intervalo.
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
# Inicializamos en 0 un contador fuera del intervalo.
cnt_out = 0
same_limits = False
cnt_in = 0

# Pedimos al usuario los límites inferior y superior.
lim_inf = int(input("Introduce el límite inferior del intervalo: "))
lim_sup = int(input("Introduce el límite superior del intervalo. Este número debe ser mayor al anterior: "))

# En caso de que el límite inferior sea mayor que el superior, aparece un mensaje de error indicándolo y solicitando
# que se introduzcan los límites en el orden indicado.
while lim_inf > lim_sup:
    print("El límite inferior no puede ser mayor al superior. Introduce los valores en el orden solicitado.\n")
    lim_inf = int(input("Introduce el límite inferior del intervalo: "))
    lim_sup = int(input("Introduce el límite superior del intervalo. Este número debe ser mayor al anterior: "))

# Pedimos al usuario un número o 0 en caso de que quiera salir.
num = int(input("\nIntroduce 0 para salir: "))

# Mientras el número sea diferente a 0 y si el número inferior es realmente inferior al superior, entonces obtenemos
# un número que está dentro del intervalo e incrementamos el contador dentro del intervalo a uno con cada comprobación.
while num!=0:
    if num>lim_inf and num<lim_sup: # Pertenece al intervalo
        cnt_in += num

# Mientras el número sea diferente a 0 pero el número inferior no es inferior al superior, entonces obtenemos
# un número que está fuera del intervalo e incrementamos el contador exterior al intervalo a uno con cada comprobación.
    else:   # No pertenece al intervalo
        cnt_out += 1

# Si el número introducido es igual a alguno de los límites, se crea una variable booleana con valor True.
        if num==lim_inf or num==lim_sup:
            same_limits = True
    num = int(input("Introduce un número (0, para salir): "))

# Mostramos el resultado de la suma de los números dentro del intervalo.
print("\nRESULTADOS:")
print(f"La suma de los números dentro del intervalo es {cnt_in}")

# Mostramos el resultado de la suma de los números fuera del intervalo.
print(f"La cantidad de números fuera del intervalo es {cnt_out}")

# Mostramos un mensaje si el número introducido es igual a alguno de los límites.
if same_limits:
    print("Se ha introducido algún número igual a los límites del intervalo.")

# Mostramos un mensaje si el número introducido es diferente a alguno de los límites.
else:
    print("No se ha introducido ningún número igual a los límites del intervalo.")
