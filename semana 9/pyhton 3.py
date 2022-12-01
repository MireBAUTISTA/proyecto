op='S'
cp = 0
ci = 0
while op.upper()!='N':
    x = int(input('N:'))
    if x%2==0:
        cp+= 1
    else:
        ci+=1
    op = input("Opción[S/N]: ")
print("Numeros pares: ",cp)
print("Numeros impares: ", ci)