from random import* 
def ld(n,p):
    for i in range(n): 
        x=randint(1,6) 
        print(x) 
        if x==p: 
            print('Lanzamiento en el cual salió el ',p, " es: ",i+1) 
            break
    return

a=int(input("Ingrese el número de lanzamientos máximos: "))
b=int(input("Ingrese el número que desea que salga: "))
print(ld(a,b))