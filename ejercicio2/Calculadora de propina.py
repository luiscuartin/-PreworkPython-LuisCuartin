
def cuenta(lista):
  total = 0
  for precio in lista:
    total += precio
  total *= 1.15
  return total

Factura = [2,6,4,8,7,5,21]

print(cuenta(Factura))