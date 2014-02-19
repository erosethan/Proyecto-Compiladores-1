#!/usr/bin/python

import sys

def imprimirAutomata(inicio):
	queue = [inicio]
	while 0 < len(queue):
		nodo = queue.pop(0)
		nodo.imprimir()
		for trans in nodo.transiciones:
			queue.append(trans[0])

def expregAThompson(expreg):
	inicios = []
	finales = []
	n = len(expreg)
	
	for i in range(n):
		if expreg[i] == '|':
			nodo_union_inicio = Nodo()		
			nodo_union_final = Nodo(True)
			nodo_inicio_grafo1 = inicio.pop()
			nodo_final_grafo1 = final.pop()			
			nodo_final_grafo1.esFinal = False			
			nodo_inicio_grafo2 = inicio.pop()
			nodo_final_grafo2 = final.pop()	
			nodo_final_grafo2.esFinal(False)
			nodo_union_inicio.agregar_transicion(nodo_inicio_grafo1, '@')						
			nodo_union_inicio.agregar_transicion(nodo_inicio_grafo2, '@')
			nodo_final_grafo1.agregar_transicion(nodo_union_final, '@')
			nodo_final_grafo2.agregar_transicio(nodo_union_final, '@')	
			inicio.append(nodo_union_inicio)
			final.append(nodo_union_final)
			
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

		elif expreg[i] == '+':
			nodo_positiva_inicio = Nodo()
			nodo_positiva_final = Nodo(True)
			nodo_inicio_grafo = inicio.pop()
			nodo_final_grafo = final.pop()
			nodo_final_grafo.esFinal(False)
			nodo_final_grafo.agregar_transicion(nodo_positiva_final, '@')				
			nodo_final_grafo.agregar_transicion(nodo_inicio_grafo, '@')
			nodo_inicio_positiva.agregar_transicion(nodo_inicio_grafo, '@')
			inicio.append(nodo_inicio_positiva)
			final.append(nodo_final_positiva)
			
		elif expreg[i] == '*':
			nodo_kleene_inicio = Nodo()
			nodo_kleene_final = Nodo(True)
			nodo_inicio_grafo = inicio.pop()
			nodo_final_grafo = final.pop()
			nodo_final_grafo.esFinal(False)
			nodo_final_grafo.agregar_transicion(nodo_inicio_grafo, '@')
			nodo_kleene_inicio.agregar_transicion(nodo_inicio_grafo, '@')
			nodo_final_grafo.agregar_transicion(nodo_kleene_final, '@')
			nodo_kleene_inicio.agregar_transicion(nodo_kleene_final, '@')
			inicio.append(nodo_kleene_inicio)
			final.append(nodo_kleene_final)
			
		else:
			nuevoInicio = Nodo()
			nuevoFinal = Nodo(True)
			nuevoInicio.agregarTransicion(nuevoFinal, expreg[i])
			
			inicios.append(nuevoInicio)
			finales.append(nuevoFinal)
	
	return (inicios[0], finales[0])
	
def main():
	(a, b) = expregAThompson('ab-')
	imprimirAutomata(a)

if __name__ == "__main__":
	main()