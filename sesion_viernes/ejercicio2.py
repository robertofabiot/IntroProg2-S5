sueldo = float(input("Ingrese el sueldo del empleado: "))
bono = None

if sueldo > 3000:
    bono = sueldo * 0.1
elif sueldo > 1500 and sueldo <= 3000:
    bono = sueldo * 0.05
elif sueldo <= 1500:
    bono = 0

sueldo_bono = sueldo + bono

print(f"El sueldo es de {sueldo}")
print(f"El bono es de {bono}")
print(f"El sueldo con el bono es de {sueldo_bono}")
