inventario_inicial = float(input("Ingrese la cantidad inicial en el inventario: "))
productos_recibidos = float(input("Ingrese la cantidad de productos recibidos: "))
productos_vendidos = float(input("Ingrese la cantidad de productos vendidos: "))

inventario_actual = productos_recibidos + inventario_inicial
inventario_actual -= productos_vendidos

print(f"""
Inventario inicial:       {inventario_inicial:>10.2f}
Productos recibidos:      {productos_recibidos:>10.2f}
Productos vendidos:       {productos_vendidos:>10.2f}
Inventario final:         {inventario_actual:>10.2f}
""")