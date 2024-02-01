def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

peso = 81 #En kilogramos
altura =1.92 #en metros

imc = calcular_imc(peso, altura)

print(f"Su índice de masa corporal es: {imc}")

if imc < 18.5:
    print("Bajo peso")
elif 18.5 <= imc < 25:
    print("Peso normal")
elif 25 <= imc < 30:
    print("Sobrepeso")
else:
    print("Obesidad")
