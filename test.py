#!/usr/bin/python

import automata, nodo, expreg

prueba = '(a|b*c)|(ab|c+)'

expresionRegular = expreg.marcarConcatenacion(prueba)
print(prueba + ' ===> ' + expresionRegular + '\n')

expresionRegular = expreg.infijaAPosfija(expresionRegular)
inicioAutomata = automata.expregAThompson(expresionRegular)

automata.imprimirAutomata(inicioAutomata)
