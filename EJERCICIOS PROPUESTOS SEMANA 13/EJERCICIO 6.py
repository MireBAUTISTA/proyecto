import math
def areayperimetro(radio):
	area = math.pi * radio ** 2;
	perimetro = 2 * math.pi * radio;
	return area,perimetro
radio = float(input("Introduce el radio:"))
area,perimetro = areayperimetro(radio)
print("Área:",area)
print("Perímetro:",perimetro)