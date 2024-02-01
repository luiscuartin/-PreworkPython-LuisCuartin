def determinar_dia_semana(numero):
    dias_semana = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
    
    if 1 <= numero <= 7:
        dia_semana = dias_semana[numero - 1]
        return dia_semana
    else:
        return "Número no válido. Por favor, ingrese un número del 1 al 7."

numero_usuario = int(input("Ingrese un número del 1 al 7 para representar un día de la semana: "))

resultado = determinar_dia_semana(numero_usuario)
print(f"El número {numero_usuario} corresponde a {resultado}.")
