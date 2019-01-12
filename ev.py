#( p | q )
def evalua(exp, e, ops, val):
	#lista de operadores binarios
	dicOBin = {'&':' and ', '|':' or ','=>':''}
	#lista de operadores unarios
	dicOUna = {'!':'not '}
	#si la entrada es cadena hacer split
	if type(exp) == type('str'):
		exp = exp.split()
		#invierte la cadena
		exp.reverse()
	#lee el ultimo digito(porque esta invertida)
	element = exp[-1]
	#si encuentra un parentesis entonces ignoralo
	if element == '(':
		pass
	#si encuentras un operador agregalo a lista de operadores
	elif(element in dicOBin) or (element in dicOUna):
		ops.append(element)
	#si encuentras un parentesis que cierra entonces 
	elif element == ')':
		#saca un operador de la pila y guarda en op y saca un valor de la pila y guarda en va
		op,va = ops.pop(),val.pop()
		#si op es unario entonces
		if op in dicOUna:
			#evalua el operadore + el valor
			va = eval(dicOUna[op]+str(va))
		# si el operador es implicacion entonces
		elif op == '=>':
			#va = la formula de implicacion
			va = not val.pop() or va 
		#sino va = evaluar el elemento va de la pila + operador binario + valor consiguiente
		else:
			va = eval(str(val.pop())+dicOBin[op]+str(va))
		#agregar va a la pila val
		val.append(va)
	#sino agrega premisas a val
	else:
		val.append(e[element])
	#hace pop a la lista para ir descartando elementos ya evaluados
	exp.pop()
	if len(exp) != 0:
		evalua(exp,e,ops,val);
	#regresa el valor del elemento de la pila
	return val