'''
1. Suma de elementos
2. Promedio
3. Mayor
4. Menor
5. Buscar Elemento
'''
from ejemplo.operaciones import * 
lista=[]
n = int(input("Cantidad de elementos: "))
i = 0
while i<n:
    x = int(input())
    add(x)
    i+=1
print("Suma de elementos: ",suma())
print("Promedio de elementos: ",promedio())
print("Mayor de elementos: ",mayor())
print("Menor de elementos: ",menor())