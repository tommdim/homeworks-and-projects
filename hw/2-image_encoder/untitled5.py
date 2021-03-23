#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 11:18:19 2020

@author: tommasodimario
"""
# def order(d_intersec,d_diff_per,lista_ordine,element):
    
def order(d_intersec,d_diff_per,lista_ordine,element):
    dizionario_prova = {}
    lista_ordine.append(element)
    switch = False
    if len((lista_ordine)) == len (d_intersec):
        return list(reversed(lista_ordine))
        
        # print(list(reversed(lista_ordine)))
        
      
    for key in d_intersec:
        if element in d_intersec[key]:
            d_intersec[key].remove(element)
    for inter in d_intersec[element]:
        dizionario_prova[inter]=d_diff_per[inter]
    for inter in dizionario_prova:
        inter = (min(dizionario_prova, key=dizionario_prova.get))
    
        return order(d_intersec,d_diff_per,lista_ordine,inter)
    
        
    # return 1
d_intersec = {(255, 0, 255): [(128, 128, 128), (0, 255, 0)], (128, 128, 128): [(255, 0, 255), (0, 0, 128)], (0, 255, 0): [(255, 0, 255), (0, 0, 128)], (0, 0, 128): [(128, 128, 128), (0, 255, 0)]}
d_diff_per = {(255, 0, 255): 4, (128, 128, 128): 2, (0, 255, 0): 0, (0, 0, 128): 2}
lista_ordine = []
num_rect = [(255, 0, 255), (128, 128, 128), (0, 255, 0), (0, 0, 128)]
for element in num_rect:
    if d_diff_per[element] == 0:
        lista_ordine = order(d_intersec,d_diff_per,lista_ordine,element)
         
        print(lista_ordine)
