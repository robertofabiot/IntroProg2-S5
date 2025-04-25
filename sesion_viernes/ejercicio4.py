def es_triangulo(lado1, lado2, lado3):
    if lado1<=0 or lado2<=0 or lado3<=0:
        return("El número no puede ser 0")
    elif ((lado1 + lado2)>lado3) and ((lado2 + lado3)>lado1) and ((lado1 + lado3)>lado2):
        return("Los números pueden formar un triángulo")
    else:
        return("Los números no pueden formar un triángulo")

def main():
    lado1 = float(input("Ingrese el primer número: "))
    lado2 = float(input("Ingrese el segundo número: "))
    lado3 = float(input("Ingrese el tercer número: "))
    print(es_triangulo(lado1,lado2,lado3))

main()




