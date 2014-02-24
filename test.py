#!/usr/bin/python

import automata, nodo, expreg

prueba = 'a|((a|b)-c)*-d+'

expresionRegular = expreg.marcarConcatenacion(prueba)
print(prueba + ' ===> ' + expresionRegular + '\n')

expresionRegular = expreg.infijaAPosfija(expresionRegular)
inicioAutomata = automata.expregAThompson(expresionRegular)

automata.generarImagen(inicioAutomata, 'prueba')
