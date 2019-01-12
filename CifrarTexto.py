# -*- encoding: utf-8 -*-
#Programa 2: Consiste en hacer un código que se encargue de cifrar y descifrar texto de acuerdo al método mostrado.
#

#Marco Antonio Delgado González
#Carlos Eduardo Ramírez Santiago
#Jose Angel Lopez Mondragon

def cifrar():
	#Ingreso de datos de usuario
	frase = input("Ingrese la frase que desea cifrar: ")
	clave = input("Ingrese su palabra clave: ")

	#Se quitan los espacios a las cadenas de entrada
	frase = frase.replace(" ", "")
	clave = clave.replace(" ", "")
	
	#Se mide la longitud de las cadenas
	len_frase = len(frase)
	len_clave = len(clave)
	
	#num_row es el numero de renglones
	num_row = len_frase/len_clave
	if(len_frase%len_clave > 0):
		num_row = int(num_row) + 1

	#tam_list es igual al tamaño de la frase + el redondeo
	tam_list = len_clave*num_row

	#Se convieten en listas ambas cadenas
	clave_list = list(clave)
	frase_list = list(frase)

	#Se llenan los espacios sobrantes con S
	espacios_sobrantes = int(tam_list)-len_frase
	for count_espacios in range(espacios_sobrantes):
		frase_list.append("S")

	#Se enlistan todos los elementos en una sola lista
	for i in range(len_clave):
		clave_list[i]=[list(clave)[i]]
	x=0
	for j in range(int(num_row)):
		for k in range(len_clave):
			clave_list[k].append(frase_list[x])
			x=x+1

	#Se ordena la lista
	clave_list.sort()

	#Se cambia de lista a cadena
	lista_temp = []
	for l in range(len_clave):
		del clave_list[l][0]
		temp =''.join(clave_list[l])
		lista_temp.append(temp)
	lista_cifrada=''.join(lista_temp)
	print("\nCadena cifrada: "+lista_cifrada)
		
def descifrar():
	#Ingreso de datos de usuario
	frase = input("\nIngrese la frase que desea descifrar: ")
	clave = input("Ingrese su palabra clave: ")

	#Se quitan los espacios a las cadenas de entrada
	frase = frase.replace(" ", "")
	clave = clave.replace(" ", "")
	
	#Se mide la longitud de las cadenas
	len_frase = len(frase)
	len_clave = len(clave)

	#Se calcula la longitud de las subdivisiones
	num_row = len_frase/len_clave
	if(len_frase%len_clave > 0):
		num_row = int(num_row)

	num = int(num_row)	

	frase_new_list = []

	#Se cambia de cadena a lista
	frase_list = list(frase)
	for e in range(len_clave):
		frase_new_list.append([])

	a=0
	#Se ordena la lista
	clave_list=list(clave)
	clave_list.sort()

	#Se agrupa en partes como letras tiene la palabra clave
	for i in range(len_clave):
		b=a+(num)
		frase_new_list[i].append(frase_list[a:b])
		a=b

	for i in range(len_clave):
		frase_new_list[i].insert(0,clave_list[i])

	for j in range(len_clave):
		temp = ''.join(frase_new_list[j][1])
		frase_new_list[j][1] = temp

	print("\nGrupos de frase decifrada: ",frase_new_list)

cifrar()
descifrar()
