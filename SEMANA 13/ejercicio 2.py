def suma(x,y):
    return x+y
def resta(x,y):
    return x-y
def multiplicación(x,y):
    return x*y
def división(x,y):
    if y!=0:
        return x/y
    return "Invalido"

n1 = float(input("N1: "))
n2 = float(input("N2: "))

print("La suma es: ",suma(n1,n2))
print("La resta es: ",resta(n1,n2))
print("La multiplicación es: ",multiplicación(n1,n2))
print("La dicisión es: ",división(n1,n2))