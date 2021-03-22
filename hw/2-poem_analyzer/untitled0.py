#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 13:48:22 2020

@author: tommasodimario
"""

def colors(imm):
        lista = []
        for x in imm:
            lista += set(x)
        lista = set(lista)
        lista.remove((0,0,0))
        return list(lista)
imm = images.load('random-50-991-1437.png')
colors(imm)


def vertici(filename):
    imm = images.load(filename)
    # imm = [list(filter(lambda a: a != (0,0,0), row)) for row in imm]
    rettangoli = []
    for color in colors(imm):
        y = next(i for i in range(len(imm)) if color in imm[i])
        x = imm[y].index(color)
        p1 = (x,y)
        y1 = next(i for i in reversed(range(len(imm))) if color in imm[i])
        x1 = imm[y].index(color)
        p2 = (x1,y1)
        rettangoli.append(Rectangle(p1, p2, color, imm))
    return rettangoli

def ordine(rettangoli):
    diz = diz_int(rettangoli)
    ordine = []
    for rettangolo in rettangoli:
        for [diz[rettangolo]] in diz:
            if rettangolo in diz[rettangolo]:
                print(rettangolo)
        

def diz_int(rettangoli):
    colori = {rettangolo.color:rettangolo for rettangolo in rettangoli}
    
    return {rettangolo: [colori[colore] for colore in rettangolo.whosintersecating(rettangolo.imm)] for rettangolo in rettangoli}
            
# def ordine(rettangoli, imm):
#     dic = {rettangolo:rettangolo.whosintersecating(imm) for rettangolo in rettangoli}
#     for rettangolo in dic:
#         if dic.get(rettangolo)
        
# x = list(sorted(rettangoli, reverse = True))
# scorrere('circle.png')
def ex1(image_filename, encoded_filename):
    rettangoli = vertici(image_filename)
    lista = []
    for rettangolo in rettangoli:
        lista.append(rettangolo.whosintersecating)
    return lista

