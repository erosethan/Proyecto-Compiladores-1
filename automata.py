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
		os.system('%s.png' % nombreImagen)
	
	except IOError:
		print('Error al generar %s.png' % nombreImagen)
		formato.close()
	
	os.system('rm formato.dot')	
