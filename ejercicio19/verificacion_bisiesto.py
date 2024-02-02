def es_bisiesto(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

year_usuario = int(input("Ingrese un año: "))

if es_bisiesto(year_usuario):
    print(f"{year_usuario} es un año bisiesto.")
else:
    print(f"{year_usuario} no es un año bisiesto.")
