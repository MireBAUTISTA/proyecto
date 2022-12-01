cad=input("Cadena:")
caracter=input("Caracter:")
for i in range(0,9):
    cad=cad.replace(str(i),caracter)
print(cad)