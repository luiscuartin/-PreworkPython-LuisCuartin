def contar_vocales(palabra):
    palabra = palabra.lower()
    vocales = "aeiou"

    contador_vocales = sum(1 for letra in palabra if letra in vocales)

    return contador_vocales


palabra_usuario = ("luismiguelcuartin")
cantidad_vocales = contar_vocales(palabra_usuario)
print(f"La palabra '{palabra_usuario}' tiene {cantidad_vocales} vocal(es).")
