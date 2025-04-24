Algoritmo ejercicio7
	Definir monto_total Como Real
	Definir satisfaccion Como Entero
	Definir propina Como Real
	Escribir 'Ingrese el monto total'
	Leer monto_total
	Escribir 'Ingrese el número según su satisfacción'
	Escribir '[1] Buena'
	Escribir '[2] Mala'
	Leer satisfaccion
	Si satisfaccion==1 Entonces
		propina <- monto_total*0.15
	FinSi
	Si satisfaccion==2 Entonces
		propina <- monto_total*0.05
	SiNo
		Escribir 'Ingrese una opción válida'
		// Aquí quería poner un exit, pero no supe cómo.
	FinSi
	monto_total <- monto_total+propina
	Escribir 'El total a pagar es ', monto_total
FinAlgoritmo
