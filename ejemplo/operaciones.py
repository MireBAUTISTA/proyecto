lista=[]

def add(n):
    lista.append(n)

#Suma de elementos de la lista
def suma():
    sum =0
    for i in range(0,len(lista)):
        sum+=lista[i]
    return sum
#Prromedio de elementos de la lista
def promedio():
    return suma()/len(lista)

#Número mayor de la lista
def mayor():
    mayor = 0
    for e in range(0,len(lista)):
        if lista[e]>mayor:
            mayor = lista[e]
    return mayor

def menor():
    menor = 10000
    for z in range(0,len(lista)):
        if lista[z]<menor:
            menor = lista[z]
    return menor