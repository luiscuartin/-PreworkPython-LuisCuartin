import datetime

def calcular_edad():
    año_nacimiento = int(input("Por favor, ingresa tu año de nacimiento: "))

    año_actual = datetime.datetime.now().year

    edad = año_actual - año_nacimiento

    print(f"Tienes {edad} años.")

calcular_edad()
