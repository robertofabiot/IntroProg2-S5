consumo_mes = float(input("Ingrese el total de litros consumidos en un mes en la vivienda: "))
personas = float(input("Ingrese la cantidad de personas que viven en la casa: "))
consumo_mes_persona = consumo_mes / personas
consumo_diario_persona = consumo_mes_persona / 30

print(f"El consumo total del mes es: {consumo_mes:.2f}")
print(f"Cantidad de personas: {personas:.2f}")
print(f"El consumo mensual por persona es: {consumo_mes_persona:.2f}")
print(f"El consumo diario por persona es: {consumo_diario_persona:.2f}")