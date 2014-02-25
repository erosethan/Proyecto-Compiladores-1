#!/usr/bin/python

import os
from nodo import Nodo

def expregAThompson(expreg):
	n = len(expreg)
	if n == 0:
		return Nodo(True)
	
	inicios = []
	finales = []

	for i in range(n):
		if expreg[i] == '|':
			nuevoInicio = Nodo()      
			nuevoFinal = Nodo(True)
			
			nodoInicioB = inicios.pop()
			nodoInicioA = inicios.pop()
			nodoFinalB = finales.pop()
			nodoFinalA = finales.pop()
			
			nodoFinalA.esFinal = False
			nodoFinalB.esFinal = False
			nuevoInicio.agregarTransicion(nodoInicioA)
			nuevoInicio.agregarTransicion(nodoInicioB)
			nodoFinalA.agregarTransicion(nuevoFinal)
			nodoFinalB.agregarTransicion(nuevoFinal)
			
			inicios.append(nuevoInicio)
			finales.append(nuevoFinal)

		elif expreg[i] == '-':
			nodoInicioB = inicios.pop()
			nodoInicioA = inicios.pop()
			nodoFinalB = finales.pop()
			nodoFinalA = finales.pop()

			nodoFinalA.esFinal = False;
			for transicion in nodoInicioB.transiciones:
				nodoFinalA.agregarTransicion(transicion[0], transicion[1])
			del nodoInicioB

			inicios.append(nodoInicioA)
			finales.append(nodoFinalB)

		elif expreg[i] == '+' or expreg[i] == '*':
			nuevoInicio = Nodo()
			nuevoFinal = Nodo(True)
			
			nodoInicio = inicios.pop()
			nodoFinal = finales.pop()
			
			nodoFinal.esFinal = False
			nodoFinal.agregarTransicion(nuevoFinal)               
			nodoFinal.agregarTransicion(nodoInicio)
			nuevoInicio.agregarTransicion(nodoInicio)
			
			if expreg[i] == '*':
				nuevoInicio.agregarTransicion(nuevoFinal)
			
			inicios.append(nuevoInicio)
			finales.append(nuevoFinal)

		else:
			nuevoInicio = Nodo()
			nuevoFinal = Nodo(True)
			nuevoInicio.agregarTransicion(nuevoFinal, expreg[i])

			inicios.append(nuevoInicio)
			finales.append(nuevoFinal)

	return inicios[0]

def cerraduraEpsilon(iniciales):
	cola = []
	indice = 0
	for inicial in iniciales:
		cola.append(inicial)
	
	while(indice < len(cola)):
		for trans in cola[indice].transiciones:
			if trans[1] == '@' and not cola.count(trans[0]):
				cola.append(trans[0])
		indice += 1
	
	return set(cola)

def moverConCaracter(iniciales, char):
	alcanzables = []
	
	for inicial in iniciales:
		for trans in inicial.transiciones:
			if char == trans[1]:
				alcanzables.append(trans[0])
	
	return set(alcanzables)

def irConCaracter(iniciales, char):
	mover = moverConCaracter(iniciales, char)
	return cerraduraEpsilon(mover)

def thompsonADeterminista(inicio, alfabeto):
	inicial = cerraduraEpsilon({inicio})
	
	nodosGenerados = [Nodo()]
	estadosGenerados = [inicial]
	nEstados = len(estadosGenerados)
	
	indice = 0
	while indice < nEstados:
		for char in alfabeto:
			nodo = nodosGenerados[indice]
			estado = estadosGenerados[indice]
			
			nuevo = irConCaracter(estado, char)
			
			if not len(nuevo):
				continue
			
			if estadosGenerados.count(nuevo):
				generado = estadosGenerados.index(nuevo)
				transicion = nodosGenerados[generado]
				
			else:
				transicion = Nodo()
				estadosGenerados.append(nuevo)
				nodosGenerados.append(transicion)
			
			nodo.agregarTransicion(transicion, char)
		
		nEstados = len(estadosGenerados)
		indice += 1
	
	for i in range(nEstados):
		for estado in estadosGenerados[i]:
			if estado.esFinal:
				nodosGenerados[i].esFinal = True
			if nodosGenerados[i].esFinal: break
	
	return nodosGenerados[0]

def generarImagen(inicio, nombreImagen):
	try:
		formato = open('formato.dot', 'w')
		
		formato.write('digraph automata{\n')
		formato.write('rankdir=LR;\n')
		formato.write('node[shape=circle];\n')
		formato.write('%s[style=filled];\n' % str(inicio))
		
		indice = 0
		cola = [inicio]
		while indice < len(cola):
			formato.write(cola[indice].imprimir())
			for trans in cola[indice].transiciones:
				if not cola.count(trans[0]):
					cola.append(trans[0])
			indice += 1
		
		formato.write('}\n')
		formato.close()
		
		os.system('dot -Tpng formato.dot -o %s.png' % nombreImagen)
	
	except IOError:
		print('Error al generar %s.png' % nombreImagen)
		formato.close()
	
	os.system('rm formato.dot')
