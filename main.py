#!/usr/bin/python

import automata, nodo, expreg

entrada = input()

expresionRegular = expreg.marcarConcatenacion(entrada)
print(entrada + ' ===> ' + expresionRegular + '\n')

expresionRegular = expreg.infijaAPosfija(expresionRegular)
inicioAutomata = automata.expregAThompson(expresionRegular)

automata.generarImagen(inicioAutomata, 'AFN')

alfabeto = expreg.obtenerAlfabeto(expresionRegular)
inicioAutomata = automata.thompsonADeterminista(inicioAutomata, alfabeto)

automata.generarImagen(inicioAutomata, 'AFD')
