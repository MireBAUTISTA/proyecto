c = 0
s = 0
op = 'S'
while op.upper()!= 'N':
    c =+1
    x = int(input("N: "))
    s += x
    op = input("Opción[S/N]: ")
print("El promedio es", str(s/c))