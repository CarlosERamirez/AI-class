# -*- encoding: utf-8 -*-
#Programa1 
#Operaciones con numeros complejos

#	*Módulo y ángulo
#	*Suma y resta
#	*Multiplicación y división
#	*Potenciación


#Marco Antonio Delgado González
#Carlos Eduardo Ramírez Santiago
#Jose Angel Lopez Mondragon

import math

def modulo_y_angulo(a,b):  #funcion para calcular modulo y angulo

	print ("Modulo y angulo \n")
	if (a!=0):
		mod=math.sqrt(a*a+b*b)

		if a>0 and b>=0:
			ang=math.atan(b/a)*(180/math.pi)
		if a<0 and b>=0:
			ang=math.atan(b/a)*(180/math.pi)+180
		if a<0 and b<=0:
			ang=math.atan(b/a)*(180/math.pi)+270
		if a>0 and b<=0:
			ang=(math.atan(b/a)*(180/math.pi))*-1+270			
	
		print ("Modulo: ",mod)
		print ("Angulo: ",ang)
		potenciacion(mod,ang)
	else:
		print ("Valor de la componente real no valido.")


def suma_y_resta(R1,I1): #funcion para calcular suma y resta

	print ("\nSuma y resta \n")

	r2 = float(input("Digite componente real del segundo numero: "))	
	i2 = float(input("Digite componente imaginaria del segundo numero: "))

	r3=R1+r2
	r4=R1-r2

	i3=I1+i2
	i4=I1-i2

	print ("suma:",r3,"+",i3,"i")
	print ("resta:",r4,"-",i4,"i")

def producto_y_division(R1,I1): #funcion para calcular multiplicacion y division

	print ("\nProducto y división \n")

	r2 = float(input("Digite componente real del segundo numero: "))
	i2 = float(input("Digite componente imaginaria del segundo numero: "))	

	proR=R1*r2-I1*i2
	proI=(R1*i2+I1*r2)

	cocR=(R1*r2+I1*i2)/(r2*r2+i2*i2)
	cocI=(-R1*i2+I1*r2)/(r2*r2+i2*i2)


	print ("Producto: ",proR,"+",proI,"i")

	if ((R1==r2)and(I1==i2)and(I1==r2)and(R1==i2)):
		print ("Cociente:",1)
	else:	
		print ("Cociente:",cocR,"-",cocI,"i")

def potenciacion(mag,an):

	print ("\nPotenciación \n") #funcion para calcular potencia
	
	pot = float(input("Digite la potencia deseada mayor a cero: "))

	if pot!=0:
		potm=math.pow(mag,pot)
		pota=an*pot
		print ("Numero original en forma polar:",mag,"cis",an)
		print ("Resultado en forma polar:",potm,"cis",pota)

	else:
		print ("Resultado:",1)

#programa principal---------------------------------------------------------------

while True:
	try:
		r1 = float(input("Digite componente real del primer numero: "))
		break
	except ValueError:
		print ("Error de Valores.")
		
while True:
	try:
		i1 = float(input("Digite componente imaginaria del primer numero: "))	
		print ("\n")
		break
	except ValueError:
		print ("Error de Valores")

modulo_y_angulo(r1,i1)
suma_y_resta(r1,i1) 
producto_y_division(r1,i1)

#fin programa principal