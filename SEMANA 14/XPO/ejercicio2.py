def menuart(): 
    print() 
    print('1) Ingresar artículo') 
    print('2) Consultar artículo') 
    print('3) Comprar') 
    print('4) Vender') 
    print('5) Eliminar artículo')
    print('6) Total de productos')
    print('7) Lista de productos')
    print('8) Productos sin stock')
    print('9) Salir')
     
def ingresar(registros): 
    cod=int(input('Ingrese código: ')) 
    cant=int(input('Ingrese cantidad: ')) 
    pre=float(input('Ingrese precio: ')) 
    nom=input('Ingrese nombre: ') 
    reg=[cod,cant,pre,nom] 
    registros=registros+[reg] 
    return registros 
 
def consultar(registros): 
    c=int(input('Ingrese código: ')) 
    p=-1; 
    for i in range(len(registros)): 
        if c==registros[i][0]: 
            p=i 
            break 
    if p<0: 
        print('Artículo no existe') 
    else: 
        print('Cantidad: ',registros[p][1]) 
        print('Precio: ',registros[p][2]) 
        print('Nombre: ',registros[p][3]) 
         
def comprar(registros): 
    c=int(input('Ingrese código: ')) 
    p=-1; 
    for i in range(len(registros)): 
        if c==registros[i][0]: 
            p=i 
            break 
    if p<0: 
        print('Artículo no existe') 
    else: 
        k=int(input('Ingrese la cantidad comprada: ')) 
        registros[p][1]=registros[p][1]+k 
    return registros 

def vender(registros): 
    c=int(input('Ingrese código: ')) 
    p=-1; 
    for i in range(len(registros)): 
        if c==registros[i][0]: 
            p=i 
            break 
    if p<0: 
        print('Artículo no existe') 
    else:
        nomc=input("Ingrese el nombre del cliente: ")
        dni=int(input("Ingrese el DNI del cliente: "))
        regc=[nomc,dni] 
        k=int(input('Ingrese la cantidad vendida: ')) 
        registros[p][1]=registros[p][1]-k 
    return registros 
 
def eliminar(registros): 
    c=int(input('Ingrese código: ')) 
    p=-1; 
    for i in range(len(registros)): 
        if c==registros[i][0]: 
            p=i 
            break 
    if p<0: 
        print('Artículo no existe') 
    else: 
        del registros[p] 
    return registros 

def total(registros):
    print(len(registros))
    return registros

def lista(registros):
    print(registros)
    return registros

def p0s(registros):
    cont=0
    for i in range(len(registros)):
        if 0==registros[i][1]:
            cont=cont+1
            print(cont)
    return registros
    
registros=[] 
while True: 
    menuart() 
    opc=input('Elija una opción: ') 
    if opc=='1': 
        registros=ingresar(registros) 
    elif opc=='2': 
        consultar(registros) 
    elif opc=='3': 
        registros=comprar(registros)      
    elif opc=='4': 
        registros=vender(registros)             
    elif opc=='5': 
        registros=eliminar(registros)             
    elif opc=='6':
        registros=total(registros) 
    elif opc=='7':
        registros=lista(registros)
    elif opc=='8':
        registros=p0s(registros)  
    elif opc=='9':
        print("Adiós ")