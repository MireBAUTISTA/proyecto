def mayor(j):
    mayor=0
    for e in range(0,len(j)):
        if j[e]>mayor:
            mayor =j[e]
    return mayor
def menor(j):
    menor=10000
    for z in range(0,len(j)):
        if j[z]<menor:
            menor=j[z]
    return menor

lista=[]
n=int(input("Cantidad de elementos: "))
i=0
while i<n:
    x=int(input())
    lista.append(x)
    i+=1
print("el numero mayor es: ",mayor(lista))
print("el numero menor es: ",menor(lista))