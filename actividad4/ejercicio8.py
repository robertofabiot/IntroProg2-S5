user_name = input("Ingrese el nombre de usuario: ")
password = input("Ingrese la contraseña: ")

if user_name == "admin" and password == "1234admin":
    print("Acceso permitido")
else:
    print("Acceso denegado")