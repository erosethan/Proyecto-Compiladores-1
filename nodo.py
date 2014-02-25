#!/usr/bin/python

class Nodo:
	identificador = 0
	
	def __init__(self, final = False):
		self.esFinal = final
		self.transiciones = []
		self.id = Nodo.identificador
		Nodo.identificador += 1
	
	def __str__(self):
		return 'S%d' % self.id
	
	def agregarTransicion(self, sig, char = '@'):
		self.transiciones.append((sig, char))
	
	def imprimir(self):
		formato = ''
		if self.esFinal:
			formato += str(self)
			formato += '[shape=doublecircle];\n'
		for trans in self.transiciones:
			formato += '%s->%s' % (str(self), str(trans[0]))
			formato += '[label="%s"];\n' % trans[1]
		return formato
