cadena = input("Ingrese cadena: ")
cva=0
cve=0
cvi=0
cvo=0
cvu=0
print(cadena.upper())
for cad in range(0,len(cadena)):
    print(cadena[cad])
print(cadena[::-1])
print("El número de letras es: ",len(cadena))
print(cadena.replace("","&")[1:-1])
print(cadena[0].upper(),cadena[1:])
print(cadena.center(20,"*"))
for cad in range(0,len(cadena)):
    if cadena[cad] == "a" or cadena[cad] == "A":
        cva+=1
    if cadena[cad] == "e" or cadena[cad] == "E":
        cve+=1
    if cadena[cad] == "i" or cadena[cad] =="I":
        cvi+=1
    if cadena[cad] == "o" or cadena[cad] =="O":
        cvo+=1
    if cadena[cad] == "u" or cadena[cad] =="U":
        cvu+=1
print("a se repite: ",cva," veces")
print("e se repite: ",cve," veces")
print("i se repite: ",cvi," veces")
print("o se repite: ",cvo," veces")
print("u se repite: ",cvu," veces")