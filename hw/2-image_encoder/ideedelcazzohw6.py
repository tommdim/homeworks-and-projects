#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 16:20:42 2020

@author: tommasodimario
"""
# -*- coding: utf-8 -*-
'''
Abbiamo una immagine formata da N rettangoli colorati (vuoti, è disegnato solo il bordo) su sfondo nero che vogliamo comprimere.
Per comprimerla bisogna trovare nell'immagine tutti gli N rettangoli presenti, anche se intersecati.
Dobbiamo ordinare i rettangoli in modo che la sequenza di operazioni di disegno riproduca fedelmente l'immagine originale.
Potete assumere che:
    - tutti i rettangoli hanno colori diversi
    - ciascun rettangolo ne interseca almeno un altro
    - i lati di rettangoli diversi non si sovrappongono per lungo ma si incrociano solamente
    - gli angoli di rettangoli diversi non si sovrappongono
    - la sequenza è unica (esiste una sola sovrapposizione tra rettangoli che li ordina)

Per ciascuno degli N rettangoli individuati abbiamo 5 informazioni da codificare sotto forma di una immagine:
    - x, y: coordinate dell'angolo superiore sinistro (x=colonna, y=riga)
    - w, h: larghezza ed altezza in pixel
    - C:    colore del rettangolo

Lo schema di compressione costruisce una seconda immagine di dimensioni 5xN.
La nuova immagine contiene, nello stesso ordine della sequenza di disegno, 
su righe successive dall'alto in basso i dati di ciascun rettangolo 
codificati come 5 pixel consecutivi in orizzontale come segue:
    x, y, w, h: sono codificati ciascuno con un pixel: i tre canali RGB del pixel rappresentano il valore in base 256.
        Esempio: (1,2,3) = 1*(256^2) + 2*(256^1) + 3 = 66051
    C: è il colore del 5° pixel

Infine vogliamo conoscere il bounding-box del gruppo di rettangoli, ovvero il rettangolo minimo,
con angolo superiore sinistro in (xmin, ymin) ed angolo inferiore destro (xmax, ymax)
che racchiude tutti i rettangoli.

Progettate ed implementate la funzione ex1(image_filename, encoded_filename) che:
    - legge il file indicato dal parametro 'image_filename' usando la libreria 'images' allegata
    - individua gli N rettangoli e li ordina
    - costruisce l'immagine 5xN che codifica le informazioni dei rettangoli
    - salva l'immagine codificata nel file indicato dal parametro 'encoded_filename'
    - ritorna la tupla con le 4 coordinate (xmin, ymin, xmax, ymax) del bounding box

ATTENZIONE: non importate altre librerie e non aprite file diversi da quelli passati per argomento.
'''

import images 

def colors(imm):
        lista = []
        for x in imm:
            lista += x
        lista = set(lista)
        lista.remove((0,0,0))
        return list(lista)
        
                # lista_ordine(vertici('circle.png'))
# x = list(sorted(rettangoli, reverse = True))
# scorrere('circle.png')

def ordine(rettangoli):
    return sorted(rettangoli, key = Rectangle.lp, reverse = True)


# def ordine(rettangoli):
    # diz = diz_int(rettangoli)
    # ordine = []
    # for rettangolo in rettangoli:
    #     for [diz[rettangolo]] in diz:
    #         if rettangolo in diz[rettangolo]:
    #             print(rettangolo)
    # return sorted(rettangoli, key = Rectangle.lp, reverse = True)

# def ordine(rettangoli, imm):
#     dic = {rettangolo:rettangolo.whosintersecating(imm) for rettangolo in rettangoli}
#     for rettangolo in dic:
#         if dic.get(rettangolo)
        
    # def key(self, r):
    #     if isinstance(r , Rectangle):
    #         lista = self.whosintersecating(self.imm)
    #         if lista == []:
    #             return self
    #         if r.color in lista:
    #             return r

    # def lp(self):
    #     counter = 0
    #     for cord in self.perimetro():
    #         x = cord[0]
    #         y = cord[1]
    #         if self.imm[y][x] == self.color:
    #             counter +=1
    #     return len(self.perimetro()) - counter

    # def __lt__(self, other):
        
    #     lista = self.whosintersecating(self.imm)
    #     if other.color in lista:
    #         return True
    #     else:
    #         return False
        
    # def __gt__(self,other):
    #     lista = self.whosintersecating(self.imm)
    #     if other.color not in lista:
    #         return True
    #     else:
    #         return False
        
        

# def first_last(row, j):
#     for i, pixel in enumerate(row):
#         if row.count(pixel) > 2:
#             if pixel != (0,0,0) and row[i+1] == (0,0,0):
#                 p1 = (row.index(pixel), j)
#                 p2 = (i,j)
#                 return [p1,p2]
                
    # def lato(self):
    #     return [(self.p1[0],i) for i in range(self.p3[1],self.p1[1]+1)]
    
# def vertici(filename):
#     imm = images.load(filename)
#     # imm = [list(filter(lambda a: a != (0,0,0), row)) for row in imm]
#     rettangoli = []
#     for color in colors(imm):
#         switch = True
#         for j, row in enumerate(imm):
#             if row.count(color) > 2:
#                 if switch:
#                     i = row.index(color)
#                     p1 = (i,j)
#                     switch = False
#                     continue
#                 x = next(i for i in reversed(range(len(row))) if row[i] == color)
#                 y = j
#                 p2 = x,y
#                 rettangoli.append(Rectangle(p1, p2, color,imm))
#     return rettangoli

# def check_int(rettangoli, imm):
#     chi =[]
#     for rettangolo in rettangoli:
#         for coordinata in rettangolo.perimetro():
#             x = coordinata[0]
#             y = coordinata[1]
#             if imm[y][x] != rettangolo.color:
#                 chi.append(imm[y][x])
#         return chi

def vertici(filename):
    imm = images.load(filename)
    # imm = [list(filter(lambda a: a != (0,0,0), row)) for row in imm]
    rettangoli = []
    for color in colors(imm):
        y = next(i for i in range(len(imm)) if color in imm[i])
        x = imm[y].index(color)
        y1 = next(i for i in reversed(range(len(imm))) if color in imm[i])
        x1 = imm[y].index(color)
        rettangoli.append(Rectangle(x,y),(x1,y1))
        
        # for j, row in enumerate(imm):
        #     if row.count(color) > 2:
        #         if switch:
        #             i = row.index(color)
        #             p1 = (i,j)
        #             switch = False
        #             continue
        #         x = next(i for i in reversed(range(len(row))) if row[i] == color)
        #         y = j
        #         p2 = x,y
        #         rettangoli.append(Rectangle(p1, p2, color,imm))
    return rettangoli