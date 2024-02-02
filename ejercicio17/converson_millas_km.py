def millas_a_kilometros(distancia_millas):

    distancia_kilometros = distancia_millas * 1.60934

    return distancia_kilometros

distancia_millas = float(input("Ingrese la distancia en millas: "))

distancia_kilometros = millas_a_kilometros(distancia_millas)

print(f"{distancia_millas} millas es igual a {distancia_kilometros} kilómetros.")
