# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 22:43:37 2016

@author: Carlos
"""

def evalua(exp, e):
    #"""docstring"""
    data = exp.split()                  #Separar por espacio en blanco
    dicOBin = {'&':' and ', '|':' or ', '=>':''} #Asocia lo primero con lo que esté después de los :
    dicOUna = {'!':'not '}
    ops,val=[],[]                       #Pilas de operadores, valores
    for i in data:                      #Para cada elemento en data (asignación respectiva a,b-aa,ab)
        if i=='(':
            pass
        elif (i in dicOBin) or (i in dicOUna):
            ops.append(i)               #Arreglo con los operadores
        elif i==')':
            op,va = ops.pop(),val.pop() #Saca al operador
            if op in dicOUna:
                va = eval(dicOUna[op]+str(va))#aplica ! a va
            elif op == '=>':
                va = not val.pop() or va
            else:
                va = eval(str(val.pop())+dicOBin[op]+str(va)) #saco de val algo (cadena), saco un & o |, convierto va a cadena)
            val.append(va)
        else:
            val.append(e[i])
    #print(data)
    return val
    #return data                         #,dic0Una,dic0UnaBin

###################################################+

def tdd(f,fp,e,r):
    return f(fp,e)== r

fp='( ( p => q ) => ( ( p & r ) => ( q & r ) ) )'

print('********************************** TDD')
print( tdd(evalua, '( p => q )', {'p':True,'q':False}, [False]) )
print( tdd(evalua, '( p => q )', {'p':True,'q':True}, [True]) )