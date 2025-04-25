temperatura = float(input("Ingrese la temperatura en grados celsius: "))
uso_cpu = float(input("Ingrese porcentaje del uso del CPU: "))

if temperatura > 80 or uso_cpu > 95:
    print("Iniciando protocolo de emergencia...")
