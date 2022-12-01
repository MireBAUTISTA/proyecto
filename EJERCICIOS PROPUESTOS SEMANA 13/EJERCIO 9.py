def Intercambiar(mayor,menor):
	if mayor<menor:
		return menor,mayor
	else:
		return mayor,menor


def CalcularMCD(num1,num2):
	num1, num2 = Intercambiar(num1,num2)
	resto = num1 % num2
	if resto == 0: 
		return num2
	else:
		
		return CalcularMCD(num2,resto)
	

numero1 = int(input("Número 1:"))
numero2 = int(input("Número 2:"))
print("MCD: ", CalcularMCD(numero1,numero2))