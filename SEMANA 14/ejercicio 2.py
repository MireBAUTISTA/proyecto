def menuart(): 
    print() 
    print('1) PIZZA PEQUEÑA') 
    print('2) PIZZA MEDIANA') 
    print('3) PIZZA GRANDE') 
    print('4) Salir') 
     
def PEQUEÑA(pizzas): 
    p=5
    print("desea añadir ingredientes adicionales? ")
    print('1) SI') 
    print('2) NO') 
    op=int(input(" "))
    if op == 1:
        ci=int(input("Cantidad de ingredientes adicionales: "))
        pi=ci*1.5
        pt=p+pi
        print("PRECIO DE LA PIZZA: ",p)
        print("PRECIO POR LOS INGREDIENTES ADICIONALES: ",pi)
        print("TOTAL A PAGAR: ",pt)
    else:
        pi=0
        pt=p+pi
        print("PRECIO DE LA PIZZA: ",p)
        print("PRECIO POR LOS INGREDIENTES ADICIONALES: ",pi)
        print("TOTAL A PAGAR: ",pt)
    return pizzas
def MEDIANA(pizzas): 
    p=8
    print("desea añadir ingredientes adicionales? ")
    print('1) SI') 
    print('2) NO') 
    op=int(input()) 
    if op == 1:
        ci=int(input("Cantidad de ingredientes adicionales: "))
        pi=ci*1.5
        pt=p+pi
        print("PRECIO DE LA PIZZA: ",p)
        print("PRECIO POR LOS INGREDIENTES ADICIONALES: ",pi)
        print("TOTAL A PAGAR: ",pt)
    else:
        pi=0
        pt=p+pi
        print("PRECIO DE LA PIZZA: ",p)
        print("PRECIO POR LOS INGREDIENTES ADICIONALES: ",pi)
        print("TOTAL A PAGAR: ",pt)
    return pizzas
def GRANDE(pizzas): 
    p=12
    print("desea añadir ingredientes adicionales? ")
    print('1) SI') 
    print('2) NO') 
    op=int(input()) 
    if op == 1:
        ci=int(input("Cantidad de ingredientes adicionales: "))
        pi=ci*1.5
        pt=p+pi
        print("PRECIO DE LA PIZZA: ",p)
        print("PRECIO POR LOS INGREDIENTES ADICIONALES: ",pi)
        print("TOTAL A PAGAR: ",pt)
    else:
        pi=0
        pt=p+pi
        print("PRECIO DE LA PIZZA: ",p)
        print("PRECIO POR LOS INGREDIENTES ADICIONALES: ",pi)
        print("TOTAL A PAGAR: ",pt)
    return pizzas
pizzas=[] 
while True: 
    print()
    print("//////BIENVENIDOS A BELIPIZZA//////")
    menuart() 
    opc=input('Elija una opción: ') 
    if opc=='1': 
        pizzas=PEQUEÑA(pizzas) 
    elif opc=='2': 
        pizzas=MEDIANA(pizzas) 
    elif opc=='3': 
        pizzas=GRANDE(pizzas)      
    elif opc=='4': 
        print('Adiós, gracias por su visita...!!!') 
        break