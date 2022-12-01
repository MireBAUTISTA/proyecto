A = int(input("Número 1: "))
B = int(input("Número 2: "))
C = int(input("Número 3:"))
mayor = 0
if (A>B & A>C):
    mayor = A
    print("A es el mayor", A) 
if (B>A & B>C):
    mayor = B
    print("B es el mayor", B)
if (C>A & C>B):
    mayor = C
    print("C es el mayor", C)