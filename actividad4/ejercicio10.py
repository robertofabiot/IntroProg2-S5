dia = int(input("Ingrese el día: "))
mes = int(input("Ingrese el mes: "))
anio = int(input("Ingrese el año: "))

if mes == 2 and dia > 29:
    print("ERROR")
elif (mes == 4 or mes == 6 or mes == 9 or mes == 11) and dia > 30:
    print("ERROR")
elif (mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12) and dia > 31:
    print("ERROR")