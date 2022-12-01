def menu():
    print()
    print("=====MENÚ=====")
    print("[1]. Suma de Términos")
    print("[2]. Cantidad de terminos")
    print("[3]. Primer termino")
    print("[4]. Ultimo termino")
    print("[5]. Salir")

print("Ingrese los datos sucesión")

def ingresar(sucesión): 
    cod=int(input('Ingrese código: ')) 
    cant=int(input('Ingrese cantidad: ')) 
    pre=float(input('Ingrese precio: ')) 
    nom=input('Ingrese nombre: ') 
    reg=[cod,cant,pre,nom] 
    sucesión=sucesión+[reg] 
    return sucesión 
sucesión=[]
n = int(input("Cantidad de elementos: "))
for i in range (0,n):
    x=int(input("Ingrese elementos de la suceción: "))
    sucesión.append(x)
    i=+1

def sumat(sucesión):
    for i in range (0,n):
        s = (n/2)*(i[0]+i[n-1])


sucesión=[]

while True: 
    menu() 
    opc=input('Elija una opción: ') 
    if opc=='1': 
        sucesión =sumat(sucesión) 
    elif opc=='2': 
        print(n)
    elif opc=='3': 
        sucesión=pt(sucesión)      
    elif opc=='4': 
        sucesión=ut(sucesión)             
    elif opc=='5': 
        print("Adiós ")
 
    