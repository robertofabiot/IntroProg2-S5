import datetime as dt
fecha_ingreso = input("Digite la fecha de ingreso en formato YYYY-MM-DD: ")
fecha_ingreso = dt.datetime.strptime(fecha_ingreso,"%Y-%m-%d")
fecha_actual = dt.datetime.now()

dias = (fecha_actual - fecha_ingreso).days
print(fecha_actual)
print(fecha_ingreso)
print(f"La cuenta lleva {dias} días inactiva")

if dias > 30:
    print("Cuenta inactiva")