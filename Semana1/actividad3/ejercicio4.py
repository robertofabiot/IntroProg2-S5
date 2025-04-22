#Cálculo del consumo de combustible
distancia_km = float(input("Ingrese la distancia recorrida en km: "))
litros_consumidos = float(input("Ingrese la cantidad de litros consumidos: "))  
rendimiento = distancia_km / litros_consumidos

precio_por_litro = float(input("Ingrese el precio por litro: "))
gasto_total = litros_consumidos * precio_por_litro

print(f"Distancia: {distancia_km:.2f}")
print(f"Litros: {litros_consumidos:.2f}")
print(f"Precio por litro: {precio_por_litro:.2f}")
print(f"Rendimiento del vehículo: {rendimiento:.2f}")
print(f"Gasto total en combustible: {gasto_total:.2f}")
