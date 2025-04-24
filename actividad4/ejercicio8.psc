Algoritmo ejercicio8
	definir user_name Como Caracter
	definir password Como Caracter
	
	escribir "Ingrese el nombre de usuario"
	leer user_name
	escribir "Ingrese la contraseña"
	leer password
	
	si user_name=="admin" y password=="1234admin"
		escribir "Permitir acceso"
	SiNo
		escribir "Acceso denegado"
	FinSi
FinAlgoritmo
