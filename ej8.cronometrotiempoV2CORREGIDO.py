import time

# Proceso
for horas in range(0, 24):  # desde las 0 horas a las 23
    for minutos in range(0, 60):  # desde el minuto 0 al 59
        for segundos in range(0, 60):  # desde el segundo 0 al 59
            print(f"{horas:02}:{minutos:02}:{segundos:02}", end="")
            time.sleep(1)  # esperamos un segundo
            print(8 * "\b", end="")  # ponemos el cursor al principio de la línea