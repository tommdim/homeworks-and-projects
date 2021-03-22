#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 20:47:42 2020

@author: tommasodimario
"""

def conta_spastici(lista):
    lista_char = []
    for verso in lista:
        counter = 0
        for i, c in enumerate(verso[:-1]):
            if c in 'aeioujy' and verso[i+1] not in 'aeioujy':
                counter += 1
        lista_char.append(counter +1 )
    return lista_char

def contaverso(verso):
    counter = 0
    for i, c in enumerate(verso[:-1]):
        if c in 'aeioujy' and verso[i+1] not in 'aeioujy':
            counter += 1
        
    return counter +1

cv = 'dipestaggiotessessiallarmaipartenopea' #13
vv = 'igloorubiincassandogiuratispermatozoi' #14
cc = 'dipestaggiotessessiallarmaipartenopeap'#14