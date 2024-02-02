def convertir_a_horas_y_minutos():
        minutos_totales = int(input("Ingresa la cantidad de minutos a convertir: "))

        horas = minutos_totales // 60
        minutos_residuales = minutos_totales % 60
        if horas >= 1:

                print(f"{minutos_totales} minutos equivalen a {horas} horas y {minutos_residuales} minutos.")
        else:
            print(f"{minutos_totales} minutos equivalen a {minutos_residuales} minutos.")

convertir_a_horas_y_minutos()
