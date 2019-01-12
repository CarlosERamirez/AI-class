#Programa4:

#Desarrollar el programa para un agente seguidor de línea de tipo reflejo simple con tres
#sensores de luz y dos motores.
#Desarrollar el programa para un agente basado en metas seguidor de línea cuya directiva es
#limpiar (tipo Mo).

#Marco Antonio Delgado González
#Carlos Eduardo Ramírez Santiago
#Jose Angel Lopez Mondragon

#instrucciones variable para guardar metas = secuencia de acciones para llegar a la meta 
instrucciones = []
#bandera para mantener el estado del avance hacia la meta
flag = 0

#Funcion para cargar metas, el parametro meta debe estar formado de 6 instrucciones definidas por el usuario
def metas(meta):
	for i in range(len(meta)):
		#instrucciones guarda las metas
		instrucciones.append(meta[i])
	return instrucciones

#Funcion que evalua sucesos con respecto a las metas, y regresa True si el suceso es deseable y False en caso contrario
def evaluacionSucesos(estado):
	global flag
	if flag == 0 and estado == instrucciones[0]:
		flag = 1
		return True
	elif flag == 1 and estado == instrucciones[1]:
		flag = 2
		return True
	elif flag == 2 and estado == instrucciones[2]:
		flag = 3
		return True
	elif flag == 3 and estado == instrucciones[3]:
		flag = 4
		return True
	elif flag == 4 and estado == instrucciones[4]:
		flag = 5
		return True
	elif flag == 5 and estado == instrucciones[5]:
		flag = 0
		print("Se cumplio el objetivo")
		return True
	else:
		return False

#Funcion que decide si la accion se debe efectuar o no
def decisionDeseable(estado, evaluacion):
	if evaluacion == True:
		return estado
	else:
		return False

#Funcion que interpreta la entrada escrita en linea de comandos cada llave de estado significa una accion
def interpretarEntrada(percepcion):
	estado = {'000':'3','001':'1','010':'3','011':'1','100':'0','101':'0','110':'0','111':'0'}	
	return estado[percepcion]

#Funcion que decide que accion se debe realizar con respecto al estado
def condicionAccion(estado):
	if estado == False:
		pass
	else:
		accion = {'0':'gira-derecha','1':'gira-izquierda','2':'alto','3':'avanza'}
		return accion[estado]

#Funcion de agente de reflejo simple
def agenteReflejoSimple(percepcion):
 	estado = interpretarEntrada(percepcion)
 	accion = condicionAccion(estado)
 	return accion

#Funcion de agente basado en logro de metas
def agenteLogroMetas(percepcion):
	estado = interpretarEntrada(percepcion)
	evaluacion = evaluacionSucesos(estado)
	estado = decisionDeseable(estado,evaluacion)
	accion = condicionAccion(estado)
	if estado == False:
		print("No es deseable realizar esta accion")
	else:
		return accion

		