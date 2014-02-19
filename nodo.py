class Nodo:
	identificador = 0

	def __init__(self, esFinal = False):
		self.transiciones = []
		self.esFinal = esFinal
		self.id = Nodo.identificador
		Nodo.identificador += 1
		
	def __str__(self):
		return 'Nodo(%d)' % self.id

	def agregarTransicion(self, sig, char = '@'):
		self.transiciones.append((sig, char))

	def imprimir(self):
		print('Inicia ' + str(self))
		for trans in self.transiciones:
			print('%s --(%s)--> %s' % (str(self), trans[1], str(trans[0])))
		print('Termina ' + str(self) + '\n')