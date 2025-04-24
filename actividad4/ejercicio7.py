monto_total = float(input("Ingrese el monto total: "))
satisfaccion = input("Ingrese el número según su satisfacción" + "\n" + "[1] Buena" + "\n" + "[2] Mala" + "\n")

if satisfaccion == "1":
    propina = monto_total * 0.15
    monto_total += propina
elif satisfaccion == "2":
    propina = monto_total * 0.05
    monto_total += propina
else:
    print("Opción no válida")
    exit()

print("El monto total es: ", monto_total)
