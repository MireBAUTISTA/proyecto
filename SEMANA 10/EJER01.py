op=1
texto=""
cont=0
cv=0
while op!=5:
    print("===MENU===")
    print("[1] ingresar cadena:")
    print("[2] # de espacio en blanco")
    print("[3] # de vocales")
    print("[4] Dimension de la cadena")
    print("[5] salir")
    op = int(input("opcion[1-5]:")) 
    if op == 1:
        texto = input("ingresar frase:")
    if op == 2:
        for cad in range(0,len(texto)):
            if texto[cad] == " ":
                cont+=1
        print("# de espacios e blanco :",cont)
    if op ==3:
        for cad in range(0,len(texto)):
           if texto[cad] == "a" or texto[cad] == "e" or texto[cad] == "i" or texto[cad]  == "o" or texto[cad]  == "u":
                cv+=1
        print("# de vocales:",cv)
    if op == 4:
        print("longitud de la entrada :", len(texto))