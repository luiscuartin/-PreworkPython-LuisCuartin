def contar_palabras(oracion):
    palabras = oracion.split()

    cantidad_palabras = len(palabras)

    return cantidad_palabras

oracion_usuario = input("Ingrese una oración: ")

cantidad_palabras = contar_palabras(oracion_usuario)

print(f"La oración ingresada tiene {cantidad_palabras} palabras")
