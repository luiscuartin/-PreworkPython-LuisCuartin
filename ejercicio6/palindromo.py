
def es_palindromo(palabra):
  palabra = palabra.lower()
  return palabra == palabra[::-1]


palabra = "luis"
print(es_palindromo(palabra))