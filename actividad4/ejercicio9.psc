Algoritmo ejercicio9
	Definir numero1, numero2, numero3 Como Real
	Escribir 'Ingrese el primer n�mero'
	Leer numero1
	Escribir 'Ingrese el segundo n�mero'
	Leer numero2
	Escribir 'Ingrese el tercer n�mero'
	Leer numero3
	Si numero1==numero2 Y numero2==numero3 Entonces
		Escribir 'Los n�meros son iguales'
	SiNo
		Si numero1>=numero2 Entonces
			Si numero1>numero3 Entonces
				Escribir 'El mayor es ', numero1
			SiNo
				Escribir 'El mayor es ', numero3
			FinSi
		SiNo
			Si numero2>numero3 Entonces
				Escribir 'El mayor es ', numero2
			SiNo
				Escribir 'El mayor es ', numero3
			FinSi
		FinSi
	FinSi
FinAlgoritmo
