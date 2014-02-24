#!/usr/bin/python

class Nodo:
	identificador = 0
	
	def __init__(self, esFinal = False):
		self.transiciones = []
		self.esFinal = esFinal
		self.id = Nodo.identificador
		Nodo.identificador += 1
	
	def __str__(self):
		return 'S%d' % self.id
	
	def agregarTransicion(self, sig, char = '@'):
		self.transiciones.append((sig, char))
	
	def imprimir(self, archivo):
		try:
			if self.esFinal:
				archivo.write('%s [shape=doublecircle];\n' % str(self))
			for trans in self.transiciones:
				archivo.write('%s->%s [label="%s"];\n' % (str(self), str(trans[0]), trans[1]))
		except IOError:
			pass
