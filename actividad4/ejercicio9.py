numero1 = int(input("Introduce el primer número: "))
numero2 = int(input("Introduce el segundo número: "))
numero3 = int(input("Introduce el tercer número: "))

if numero1 == numero2 and numero2 == numero3:
    print("Los tres números son iguales.")
elif numero1 >= numero2:
    if numero1 >= numero3:
        print("El número mayor es:", numero1)
    else:
        print("El número mayor es:", numero3)
else:
    if numero2 >= numero3:
        print("El número mayor es:", numero2)
    else:
        print("El número mayor es:", numero3)
    