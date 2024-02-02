def contar_pares_impares(lista):
    pares = 0
    impares = 0
    for numero in lista:
        if numero % 2 == 0:
            pares += 1
        else:
            impares += 1

    print("Cantidad de números pares:", pares)
    print("Cantidad de números impares:", impares)

lista_numeros = [1,5,6,8,7,4]

contar_pares_impares(lista_numeros)
