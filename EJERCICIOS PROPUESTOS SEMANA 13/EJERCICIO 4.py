def espaciado(cad):
	cad_con_espacio = cad.replace(""," ")
	cad_con_espacio.strip()
	return cad_con_espacio

mensaje = input("Introduce una cadena:")
print("La cadena con espacio:",espaciado(mensaje))