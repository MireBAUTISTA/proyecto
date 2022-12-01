def Login(nombre,password,intentos):
	intentos += 1
	if nombre == "usuario1" and password == "asdasd":
		return(True,intentos)
	else:
		return(False,intentos)
		

cuantasveces = 0
while True:
	usuario = input("Usuario:")
	clave = input("Password:")
	entrar,cuantasveces = Login(usuario,clave,cuantasveces)
	if not entrar:
		print("Error. Nombre de usuario o contraseña incorrecta.")
	if entrar or cuantasveces == 3: 
		break
	
if entrar:
	print("Bienvenidos al sistema")
else: 
	print("No has entrado en el sistema")