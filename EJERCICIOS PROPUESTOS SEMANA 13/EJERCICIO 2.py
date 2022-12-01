def multiplo(n1,n2):
	if n2 % n1 == 0:
		return False
	else:
		return True

n1 = int(input("Número 1:"))
n2 = int(input("Número 2:"))
if multiplo(n1,n2):
	print(n1,"es múltiplo de",n2)
else:
	print(n1,"no es múltiplo de",n2)