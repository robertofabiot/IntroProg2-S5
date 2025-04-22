capital_inicial = float(input("Ingrese el capital inicial: "))
interes_anual = float(input("Ingrese el interés anual en porcentaje: "))
tiempo = float(input("Ingrese la cantidad de años: "))

interes_anual_dec = interes_anual / 100
monto_final = ((1 + interes_anual_dec)**tiempo)*capital_inicial

interes_ganado = monto_final - capital_inicial

print(f"Capital inicial: {capital_inicial:.2f}")
print(f"Tasa: {interes_anual:.2f}")
print(f"Años: {tiempo:.2f}")
print(f"Monto final: {monto_final:.2f}")
print(f"Interés ganado: {interes_ganado:.2f}")