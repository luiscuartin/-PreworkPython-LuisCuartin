def dolares_a_euros(cantidad_dolares):
    cantidad_euros = cantidad_dolares * 0.85
    return cantidad_euros


cantidad_dolares = 10

cantidad_euros = dolares_a_euros(cantidad_dolares)

print(f"{cantidad_dolares} dólares equivalen a {cantidad_euros} euros.")
