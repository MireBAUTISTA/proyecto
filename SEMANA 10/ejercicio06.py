num=int(input("Número:"))
cad=str(num)
cad2=""
cont=1
for caracter in cad[::-1]:
	cad2=caracter+cad2
	if cont%3==0:
		cad2="."+cad2
	cont=cont+1
print(cad2)