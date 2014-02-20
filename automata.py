#!/usr/bin/python

from nodo import Nodo

def imprimirAutomata(inicio):
    indice = 0
    cola = [inicio]
    while indice < len(cola):
        cola[indice].imprimir()
        for trans in cola[indice].transiciones:
            if not cola.count(trans[0]):
                cola.append(trans[0])
        indice += 1

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