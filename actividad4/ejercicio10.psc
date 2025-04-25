Algoritmo ejercicio10
	Definir dia, mes, ANO Como Entero
	Escribir 'Ingrese el día: '
	Leer dia
	Escribir 'Ingrese el mes: '
	Leer mes
	Escribir 'Ingrese el año'
	Leer ANO
	Si mes==2 Y dia>29 Entonces
		Escribir 'ERROR'
		Sino si (mes==4 O mes==6 O mes==9 O mes==11) Y dia>30 Entonces
			Escribir 'ERROR'
		Sino si (mes==1 O mes==3 O mes==5 O mes==7 O mes==8 O mes==10 O mes==12) Y dia>31 Entonces
			Escribir 'ERROR'
		FinSi
		FinSi
	FinSi

FinAlgoritmo
