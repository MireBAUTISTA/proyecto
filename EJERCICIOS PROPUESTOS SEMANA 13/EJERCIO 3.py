c = int(input("¿Cuantos dias desea calcular las temperaturas? "))
def TM(t1,t2):
	return (t1 + t2)/2

for indice in range(c):
	tmin = float(input("Introduce temperatura mínima:"))
	tmax = float(input("Introduce temperatura máxima:"))
	print("Temperatura media:",TM(tmin,tmax))