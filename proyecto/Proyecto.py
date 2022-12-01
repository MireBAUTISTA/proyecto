registros=[]
def menuart(): 
    print() 
    print('1) Matricular alumno') 
    print('2) Buscar alumno') 
    print('3) Eliminar matricula de alumno')
    print('4) Salir')
     
def matricula(registros): 
    nombre=input('Ingrese el nombre del alumno : ')
    apellido=input('Ingrese el apellido del alumno : ')
    dni=int(input('Ingrese el DNI del alumno: ')) 
    grado=input('Ingrese el grado en el que se desea matricular al alumno:') 
    nivel=input('Ingrese el nivel: ')
    nombrep=input('Ingrese el nombre del apoderado : ')
    apellidop=(input('Ingrese el apellido del apoderado : '))
    dnip=int(input('Ingrese el DNI del apoderado: ')) 
    print('//////////////////Matricula por alumno $150//////////////////////////') 
    print('mencione si efectuo el pago de la matricula correctamente')
    print('si tu respuesta es (SI) escriba [00]')
    print('si tu respuesta es (no) escriba [11]')
    pago=int(input(''))
    precio=150
    if pago==00:
        print('//////////////////matricula exitosa//////////////////////////') 
        print('//////////////////BOLETA//////////////////////////')
        print('Nombre del alumno             :',nombre) 
        print('Apellido del alumno           :',apellido)
        print('DNI del alumno                :',dni)
        print('Grado y Nivel del matriculado :',grado,nivel)
        print('Nombre del apoderado          :',nombrep) 
        print('Apellido del apoderado        :',apellidop)
        print('DNI del apoderado             :',dnip)
        print('Pago de la matricula          :',precio)
    else :
        print('//////////////////matricula no es valida//////////////////////////') 
        print('efectue el pago al siguiente nuemero de cuenta de la institución educativa')
        print('1111-66666-7777')
        print('luego de haber realizado el pago vuelva a la pagina principal')
        reg1=[nombre,apellido,dni,grado,nivel,pago,precio]
        print(reg1)
        registros=registros+[reg1] 
    return registros
def buscar(registros): 
    c=int(input('Ingrese DNI: ')) 
    print(len(registros))
    '''for i in range(0,len(registros)):
        print('',registros[i][2])
        
        if c==registros[i][2]: 
            
            print('Nombre: ',registros[i][0])
            print('Apellido: ',registros[i][1])
            print('Grado: ',registros[i][3])
            print('Nivel: ',registros[i][4])        
        else: 
            print('El alumno no está matriculado') '''
         
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


while True: 
    menuart() 
    opc=input('Elija una opción: ') 
    if opc=='1': 
        registros=matricula(registros) 
    if opc=='2': 
        registros=buscar(registros)
    elif opc=='3': 
        print(eliminar(registros)) 
    elif opc=='4':
        print("Adiós ")