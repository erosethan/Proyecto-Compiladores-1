#!/usr/bin/python

def esParentesis(char):
	return {
		'(': 1,
		')': -1
	}.get(char, 0)

def esOperador(char):
	return {
		'|': True,
		'-': True,
		'+': True,
		'*': True
	}.get(char, False)

def esCaracterEspecial(char):
	if esParentesis(char) or esOperador(char):
		return True
	return False

def infijaAPosfija(expresion):
	pila = []
	resultado = ''
	
	prioridad = {
		'(': 4,
		')': 4,
		'|': 3,
		'-': 2,
		'+': 1,
		'*': 0
	}
	
	n = len(expresion)
	for i in range(n):
		char = expresion[i]
		
		if not esCaracterEspecial(char):
			resultado += char
		
		if esOperador(char):
			while len(pila) > 0:
				if prioridad[pila[-1]] <= prioridad[char]:
					resultado += pila[-1]
					pila.pop()
				else:
					break
			pila.append(char);
		
		if esParentesis(char) == 1:
			pila.append(char)
		
		if esParentesis(char) == -1:
			while pila[-1] != '(':
				resultado += pila[-1]
				pila.pop()
			pila.pop()
		
	n = len(pila)
	for i in range(n):
		resultado += pila[-1]
		pila.pop()
	
	return resultado
