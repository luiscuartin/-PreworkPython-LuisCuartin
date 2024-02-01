def suma_numeros_pares(numero):
    suma = 0
    for i in range(numero + 1):
        if i % 2 == 0:
            suma += i
    
    return suma


numero_usuario = 100
resultado = suma_numeros_pares(numero_usuario)
print(f"La suma de todos los números pares hasta {numero_usuario} es: {resultado}")

