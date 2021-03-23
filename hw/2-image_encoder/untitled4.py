'''#!/usr/bin/env python3
# -*- coding: utf-8 -*-

Created on Wed Nov 25 14:10:51 2020

@author: tommasodimario
'''
         
'''import images


class Rectangle:
    def __init__(self, p1, p2, color,imm): #dove p1 e p2 sono vertici opposti
        self.p1 = p1 #1,2 AS
        self.p2 = p2 #5,0 BD
        self.p3 = (p1[0], p2[1]) #1,0 BS
        self.p4 = (p2[0], p1[1]) #5,2 AD
        self.w = abs(p2[0] - p1[0]) +1
        self.h = abs(p1[1] - p2[1]) +1
        self.color = color
        self.imm = imm
        self.xmax = max([p1[0],p2[0],self.p3[0],self.p4[0]])
        self.ymax = max([p1[1],p2[1],self.p3[1],self.p4[1]])
        self.xmin = min([p1[0],p2[0],self.p3[0],self.p4[0]])
        self.ymin = min([p1[1],p2[1],self.p3[1],self.p4[1]])
        
    
    def __repr__(self):
        return f'Rec{self.color}rectangle with vertices {self.p1}, {self.p2}'
  
    
    def perimetro(self):
        p = [(self.p1[0],i) for i in range(self.p1[1],self.p3[1]+1)]\
                + [(self.p2[0],i) for i in range(self.p4[1],self.p2[1]+1)]\
                + [(i,self.p1[1]) for i in range(self.p1[0],self.p4[0]+1)]\
                + [(i,self.p3[1]) for i in range(self.p3[0],self.p2[0]+1)]
        return list(dict.fromkeys(p))
        

    def whosintersecating(self):
        chi = set()
        for coordinata in self.perimetro():
            x = coordinata[0]
            y = coordinata[1]
            if self.imm[y][x] != self.color:
                chi.add(self.imm[y][x])
        return list(chi)


def colors(imm):
        lista = []
        imm2 = [list(set(r)) for r in imm]
        for x in imm2:
            lista += set(x)
        lista = set(lista)
        lista.remove((0,0,0))
        return list(lista), imm2


def p1(imm, imm2, color):
    y = next(i for i in range(len(imm2)) if color in imm2[i])
    x = imm[y].index(color)
    return (x,y)
    
def p2(imm, imm2, color):
    y1 = next(i for i in reversed(range(len(imm2))) if color in imm2[i])
    x1 = max(i for i, col in enumerate(imm[y1]) if col == color)
    return (x1,y1)


def vertici(filename):
    imm = images.load(filename)
    rettangoli = []
    colori, imm2 = colors(imm)
    for color in colori:
        
        p11 = p1(imm, imm2,color)
        p22 = p2(imm, imm2,color)
        rettangoli.append(Rectangle(p11, p22, color, imm))
    return rettangoli

def diz_colori(rettangoli):
    return {rett : rett.whosintersecating() for rett in rettangoli}

def ordine(rettangoli):
    d = diz_colori(rettangoli)
    lista_ordine = {}
    while len(lista_ordine) < len(rettangoli):
        for rett in d:
            if d[rett] == []:
                lista_ordine[rett] = '§'
                for lista in d.values():
                    if rett.color in lista:
                        lista.remove(rett.color)
    return list(reversed(lista_ordine))

def converter(number):
    r = 0
    g = 0
    b = 0
    while number > 255:
        if number >= 256**2:
            r = 0
            while number > 256**2:
                number -= 256**2
                r += 1
        number -= 256
        g += 1
    b = number
    return (r,g,b)
        
# @profile
def encodedimage(rettangoli):
    imm = []
    lista_ordine = ordine(rettangoli)
    # colori = {rettangolo.color:rettangolo for rettangolo in rettangoli}
    # ordi = [colori[colore] for colore in lista_ordine]
    for rett in lista_ordine:
        x = rett.p1[0]
        y = rett.p1[1]
        lista = [converter(x),converter(y),converter(rett.w),converter(rett.h),rett.color]
        imm.append(lista)
    return imm


def boundingbox(rettangoli):
    xmin = min([rettangolo.xmin for rettangolo in rettangoli])
    xmax = max([rettangolo.xmax for rettangolo in rettangoli])
    ymin = min([rettangolo.ymin for rettangolo in rettangoli])
    ymax = max([rettangolo.ymax for rettangolo in rettangoli])
    return (xmin,ymin,xmax,ymax)

# @profile
def ex1(image_filename, encoded_filename):
    rettangoli = vertici(image_filename)
    enc = encodedimage(rettangoli)
    print(enc)
    images.save(enc, encoded_filename)
    return boundingbox(rettangoli)
# ex1('random-30-1574-1334.png', 'test_random-30-1574-1334.png')
    '''               
# def lista_ordine(rettangoli):
#     dic_int = diz_int(rettangoli)
#     ordine = []
#     while len(set(ordine)) < len(rettangoli):
#         for rettangolo in dic_int:
#             if dic_int[rettangolo] == []:
#                 ordine.append(rettangolo)
#                 for lista in dic_int.values():
#                     if rettangolo in lista:
#                         lista.remove(rettangolo)
    
#     return list(reversed(dict.fromkeys(ordine)))


# def diz_int(rettangoli):
#     colori = {rettangolo.color:rettangolo for rettangolo in rettangoli}
    
#     return {rettangolo: [colori[colore] for colore in rettangolo.whosintersecating()] for rettangolo in rettangoli}


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
import images


class Rectangle:
    def __init__(self, p1, p2, color,imm): #dove p1 e p2 sono vertici opposti
        self.p1 = p1 #1,2 AS
        self.p2 = p2 #5,0 BD
        self.p3 = (p1[0], p2[1]) #1,0 BS
        self.p4 = (p2[0], p1[1]) #5,2 AD
        self.w = abs(p2[0] - p1[0]) +1
        self.h = abs(p1[1] - p2[1]) +1
        self.color = color
        self.imm = imm
        self.xmax = max([p1[0],p2[0],self.p3[0],self.p4[0]])
        self.ymax = max([p1[1],p2[1],self.p3[1],self.p4[1]])
        self.xmin = min([p1[0],p2[0],self.p3[0],self.p4[0]])
        self.ymin = min([p1[1],p2[1],self.p3[1],self.p4[1]])
        
        
    def __repr__(self):
        return f'Rec{self.color}rectangle with vertices {self.p1}, {self.p2}'
  
    
    def perimetro(self):
        p = [(self.p1[0],i) for i in range(self.p1[1],self.p3[1]+1)]\
                + [(self.p2[0],i) for i in range(self.p4[1],self.p2[1]+1)]\
                + [(i,self.p1[1]) for i in range(self.p1[0],self.p4[0]+1)]\
                + [(i,self.p3[1]) for i in range(self.p3[0],self.p2[0]+1)]
        return list(dict.fromkeys(p))
        

    def whosintersecating(self):
        chi = set()
        for coordinata in self.perimetro():
            x = coordinata[0]
            y = coordinata[1]
            if self.imm[y][x] != self.color:
                chi.add(self.imm[y][x])
        return list(chi)

'''starting point of the procedural program'''

# @profile
def colors(imm):
        
        imm2 = [list(set(r)) for r in imm]
        lista = set()
        
        for x in imm2:
            lista = lista.union(set(x))
        
        lista.remove((0,0,0))
        return list(lista), imm2

# @profile
def p1(imm, imm2, color):
    for i, row in enumerate(imm2):
        if color in row:
            y = i
            break
    x = imm[y].index(color)
    return (x,y)
    
def p2(imm, imm2, color):
    y1 = next(i for i in reversed(range(len(imm2))) if color in imm2[i])
    x1 = max(i for i, col in enumerate(imm[y1]) if col == color)
    return (x1,y1)

@profile
def vertici(imm):
    # imm = images.load(filename)
    rettangoli = []
    colori, imm2 = colors(imm)
    for color in colori:
        
        p11 = p1(imm, imm2,color)
        p22 = p2(imm, imm2,color)
        rettangoli.append(Rectangle(p11, p22, color, imm))
    return rettangoli

# @profile
def diz_int(rettangoli):
    colori = {rettangolo.color:rettangolo for rettangolo in rettangoli}
    
    return {rettangolo: [colori[colore] for colore in rettangolo.whosintersecating()] for rettangolo in rettangoli}
def diz_int(rettangoli):
    colori = {rettangolo.color:rettangolo for rettangolo in rettangoli}
    
    return {rettangolo: [colori[colore] for colore in rettangolo.whosintersecating()] for rettangolo in rettangoli}
       
@profile
def lista_ordine(rettangoli):
    # d = {retta: retta.whosintersecating() for retta in rettangoli}
    # ordine = []
    # while len(set(ordine)) < len(rettangoli):
    #     for rettangolo in d:
    #         if d[rettangolo] == []:
    #             ordine.append(rettangolo)
    #             for lista in d.values():
    #                 if rettangolo.color in lista:
    #                     lista.remove(rettangolo.color)
    # return list(reversed(dict.fromkeys(ordine)))
    
    
    
    
    dic_int = diz_int(rettangoli)
    ordine = []
    while len(set(ordine)) < len(rettangoli):
        for rettangolo in dic_int:
            if dic_int[rettangolo] == []:
                ordine.append(rettangolo)
                for lista in dic_int.values():
                    if rettangolo in lista:
                        lista.remove(rettangolo)
    
    return list(reversed(dict.fromkeys(ordine)))


def converter(number):
    r = 0
    g = 0
    b = 0
    while number > 255:
        if number >= 256**2:
            r = 0
            while number > 256**2:
                number -= 256**2
                r += 1
        number -= 256
        g += 1
    b = number
    return (r,g,b)
        
# @profile
def encodedimage(rettangoli):
    imm = []
    for rett in lista_ordine(rettangoli):
        x = rett.p1[0]
        y = rett.p1[1]
        lista = [converter(x),converter(y),converter(rett.w),converter(rett.h),rett.color]
        imm.append(lista)
    return imm


def boundingbox(rettangoli):
    xmin = min([rettangolo.xmin for rettangolo in rettangoli])
    xmax = max([rettangolo.xmax for rettangolo in rettangoli])
    ymin = min([rettangolo.ymin for rettangolo in rettangoli])
    ymax = max([rettangolo.ymax for rettangolo in rettangoli])
    return (xmin,ymin,xmax,ymax)

@profile 
def ex1(image_filename, encoded_filename):
    image_filename = images.load(image_filename)
    rettangoli = vertici(image_filename)
    enc = encodedimage(rettangoli)
    images.save(enc, encoded_filename)
    return boundingbox(rettangoli)
    
ex1('random-30-1574-1334.png', 'test_random-30-1574-1334.png')

import images


class Rectangle:
    def __init__(self, p1, p2, color,imm): #dove p1 e p2 sono vertici opposti
        self.p1 = p1 #1,2 AS
        self.p2 = p2 #5,0 BD
        self.p3 = (p1[0], p2[1]) #1,0 BS
        self.p4 = (p2[0], p1[1]) #5,2 AD
        self.w = abs(p2[0] - p1[0]) +1
        self.h = abs(p1[1] - p2[1]) +1
        self.color = color
        self.imm = imm
        self.xmax = max([p1[0],p2[0],self.p3[0],self.p4[0]])
        self.ymax = max([p1[1],p2[1],self.p3[1],self.p4[1]])
        self.xmin = min([p1[0],p2[0],self.p3[0],self.p4[0]])
        self.ymin = min([p1[1],p2[1],self.p3[1],self.p4[1]])
        
        
    def __repr__(self):
        return f'Rec{self.color}rectangle with vertices {self.p1}, {self.p2}'
  
    
    def perimetro(self):
        p = [(self.p1[0],i) for i in range(self.p1[1],self.p3[1]+1)]\
                + [(self.p2[0],i) for i in range(self.p4[1],self.p2[1]+1)]\
                + [(i,self.p1[1]) for i in range(self.p1[0],self.p4[0]+1)]\
                + [(i,self.p3[1]) for i in range(self.p3[0],self.p2[0]+1)]
        return list(dict.fromkeys(p))
        

    def whosintersecating(self):
        chi = set()
        for coordinata in self.perimetro():
            x = coordinata[0]
            y = coordinata[1]
            if self.imm[y][x] != self.color:
                chi.add(self.imm[y][x])
        return list(chi)

'''starting point of the procedural program'''


def colors(imm):
        lista = []
        imm2 = [list(set(r)) for r in imm]
        for x in imm2:
            lista += set(x)
        lista = set(lista)
        lista.remove((0,0,0))
        return list(lista), imm2

# @profile
def p1(imm, imm2, color):
    for i, row in enumerate(imm2):
        if color in row:
            y = i
            break
    x = imm[y].index(color)
    return (x,y)
    
def p2(imm, imm2, color):
    # for i in reversed(range(len(imm2))):
    #     if color in imm2[]
    y1 = next(i for i in reversed(range(len(imm2))) if color in imm2[i])
    x1 = max(i for i, col in enumerate(imm[y1]) if col == color)
    return (x1,y1)

# @profile
def vertici(filename):
    imm = images.load(filename)
    rettangoli = []
    colori, imm2 = colors(imm)
    for color in colori:
        
        p11 = p1(imm, imm2,color)
        p22 = p2(imm, imm2,color)
        rettangoli.append(Rectangle(p11, p22, color, imm))
    return rettangoli

# @profile
def diz_int(rettangoli):
    colori = {rettangolo.color:rettangolo for rettangolo in rettangoli}
    
    return {rettangolo: [colori[colore] for colore in rettangolo.whosintersecating()] for rettangolo in rettangoli}
       
# @profile
def lista_ordine(rettangoli):
    dic_int = diz_int(rettangoli)
    ordine = []
    while len(set(ordine)) < len(rettangoli):
        for rettangolo in dic_int:
            if dic_int[rettangolo] == []:
                ordine.append(rettangolo)
                for lista in dic_int.values():
                    if rettangolo in lista:
                        lista.remove(rettangolo)
    
    return list(reversed(dict.fromkeys(ordine)))


def converter(number):
    r = 0
    g = 0
    b = 0
    while number > 255:
        if number >= 256**2:
            r = 0
            while number > 256**2:
                number -= 256**2
                r += 1
        number -= 256
        g += 1
    b = number
    return (r,g,b)
        
# @profile
def encodedimage(rettangoli):
    imm = []
    for rett in lista_ordine(rettangoli):
        x = rett.p1[0]
        y = rett.p1[1]
        lista = [converter(x),converter(y),converter(rett.w),converter(rett.h),rett.color]
        imm.append(lista)
    return imm


def boundingbox(rettangoli):
    xmin = min([rettangolo.xmin for rettangolo in rettangoli])
    xmax = max([rettangolo.xmax for rettangolo in rettangoli])
    ymin = min([rettangolo.ymin for rettangolo in rettangoli])
    ymax = max([rettangolo.ymax for rettangolo in rettangoli])
    return (xmin,ymin,xmax,ymax)

# @profile
def ex1(image_filename, encoded_filename):
    rettangoli = vertici(image_filename)
    enc = encodedimage(rettangoli)
    images.save(enc, encoded_filename)
    return boundingbox(rettangoli)
    
# ex1('random-30-1574-1334.png', 'test_random-30-1574-1334.png')


import images

class Rectangle:
    def __init__(self, p1, p2, color,imm): #dove p1 e p2 sono vertici opposti
        self.p1 = p1 #1,2 AS
        self.p2 = p2 #5,0 BD
        self.p3 = (p1[0], p2[1]) #1,0 BS
        self.p4 = (p2[0], p1[1]) #5,2 AD
        self.w = abs(p2[0] - p1[0]) +1
        self.h = abs(p1[1] - p2[1]) +1
        self.color = color
        self.imm = imm
        self.xmax = max([p1[0],p2[0],self.p3[0],self.p4[0]])
        self.ymax = max([p1[1],p2[1],self.p3[1],self.p4[1]])
        self.xmin = min([p1[0],p2[0],self.p3[0],self.p4[0]])
        self.ymin = min([p1[1],p2[1],self.p3[1],self.p4[1]])
        
        
    def __repr__(self):
        return f'Rec{self.color}rectangle with vertices {self.p1}, {self.p2}'
  
    
    def perimetro(self):
        p = [(self.p1[0],i) for i in range(self.p1[1],self.p3[1]+1)]\
                + [(self.p2[0],i) for i in range(self.p4[1],self.p2[1]+1)]\
                + [(i,self.p1[1]) for i in range(self.p1[0],self.p4[0]+1)]\
                + [(i,self.p3[1]) for i in range(self.p3[0],self.p2[0]+1)]
        return list(dict.fromkeys(p))
        
    # def lato(self):
    #     return [(self.p1[0],i) for i in range(self.p3[1],self.p1[1]+1)]
    
    def whosintersecating(self,imm):
        chi = set()
        for coordinata in self.perimetro():
            x = coordinata[0]
            y = coordinata[1]
            if imm[y][x] != self.color:
                chi.add(imm[y][x])
        return list(chi)

def colors(imm):
        lista = []
        for x in imm:
            lista += set(x)
        lista = set(lista)
        lista.remove((0,0,0))
        return list(lista)
    
def vertici(filename):
    imm = images.load(filename)
    # imm = [list(filter(lambda a: a != (0,0,0), row)) for row in imm]
    rettangoli = []
    for color in colors(imm):
        y = next(i for i in range(len(imm)) if color in imm[i])
        x = imm[y].index(color)
        p1 = (x,y)
        y1 = next(i for i in reversed(range(len(imm))) if color in imm[i])
        x1 = max(i for i, col in enumerate(imm[y1]) if col == color)
        p2 = (x1,y1)
        rettangoli.append(Rectangle(p1, p2, color, imm))
    return rettangoli


'''backup, 26/11/2020'''
import images


class Rectangle:
    def __init__(self, p1, p2, color,imm): #dove p1 e p2 sono vertici opposti
        self.p1 = p1 #1,2 AS
        self.p2 = p2 #5,0 BD
        self.p3 = (p1[0], p2[1]) #1,0 BS
        self.p4 = (p2[0], p1[1]) #5,2 AD
        self.w = abs(p2[0] - p1[0]) +1
        self.h = abs(p1[1] - p2[1]) +1
        self.color = color
        self.imm = imm
        self.xmax = max([p1[0],p2[0],self.p3[0],self.p4[0]])
        self.ymax = max([p1[1],p2[1],self.p3[1],self.p4[1]])
        self.xmin = min([p1[0],p2[0],self.p3[0],self.p4[0]])
        self.ymin = min([p1[1],p2[1],self.p3[1],self.p4[1]])
        
        
    def __repr__(self):
        return f'Rec{self.color}rectangle with vertices {self.p1}, {self.p2}'
  
    
    def perimetro(self):
        p = [(self.p1[0],i) for i in range(self.p1[1],self.p3[1]+1)]\
                + [(self.p2[0],i) for i in range(self.p4[1],self.p2[1]+1)]\
                + [(i,self.p1[1]) for i in range(self.p1[0],self.p4[0]+1)]\
                + [(i,self.p3[1]) for i in range(self.p3[0],self.p2[0]+1)]
        return list(dict.fromkeys(p))
        

    def whosintersecating(self,imm):
        chi = set()
        for coordinata in self.perimetro():
            x = coordinata[0]
            y = coordinata[1]
            if imm[y][x] != self.color:
                chi.add(imm[y][x])
        return list(chi)

'''starting point of the procedural program'''


def colors(imm):
        lista = []
        for x in imm:
            lista += set(x)
        lista = set(lista)
        lista.remove((0,0,0))
        return list(lista)
# imm = images.load('random-50-991-1437.png')
# colors(imm)
@profile
def vertici(filename):
    imm = images.load(filename)
    # imm = [list(filter(lambda a: a != (0,0,0), row)) for row in imm]
    rettangoli = []
    for color in colors(imm):
        y = next(i for i in range(len(imm)) if color in imm[i])
        x = imm[y].index(color)
        p1 = (x,y)
        y1 = next(i for i in reversed(range(len(imm))) if color in imm[i])
        x1 = max(i for i, col in enumerate(imm[y1]) if col == color)
        p2 = (x1,y1)
        rettangoli.append(Rectangle(p1, p2, color, imm))
    return rettangoli

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
    

def diz_int(rettangoli):
    colori = {rettangolo.color:rettangolo for rettangolo in rettangoli}
    
    return {rettangolo: [colori[colore] for colore in rettangolo.whosintersecating(rettangolo.imm)] for rettangolo in rettangoli}
       

def lista_ordine(rettangoli):
    dic_int = diz_int(rettangoli)
    ordine = []
    while len(set(ordine)) < len(rettangoli):
        for rettangolo in dic_int:
            if dic_int[rettangolo] == []:
                ordine.append(rettangolo)
                for lista in dic_int.values():
                    if rettangolo in lista:
                        lista.remove(rettangolo)
    
    return list(reversed(dict.fromkeys(ordine)))


def converter(number):
    r = 0
    g = 0
    b = 0
    while number > 255:
        if number >= 256**2:
            r = 0
            while number > 256**2:
                number -= 256**2
                r += 1
        number -= 256
        g += 1
    b = number
    return (r,g,b)
        
    
def encodedimage(rettangoli):
    imm = []
    for rett in lista_ordine(rettangoli):
        x = rett.p1[0]
        y = rett.p1[1]
        lista = [converter(x),converter(y),converter(rett.w),converter(rett.h),rett.color]
        imm.append(lista)
    return imm


def boundingbox(rettangoli):
    xmin = min([rettangolo.xmin for rettangolo in rettangoli])
    xmax = max([rettangolo.xmax for rettangolo in rettangoli])
    ymin = min([rettangolo.ymin for rettangolo in rettangoli])
    ymax = max([rettangolo.ymax for rettangolo in rettangoli])
    return (xmin,ymin,xmax,ymax)

@profile
def ex1(image_filename, encoded_filename):
    # image_filename = images.load(image_filename)
    rettangoli = vertici(image_filename)
    ordine = lista_ordine(rettangoli)
    enc = encodedimage(rettangoli)
    images.save(enc, encoded_filename)
    return boundingbox(rettangoli)
    








ex1('random-15.png', 'encoded_random-15.png')

import images


class Rectangle:
    def __init__(self, color,imm): #dove p1 e p2 sono vertici opposti
        
        self.color = color
        self.imm = imm
     
        y = next(i for i in range(len(self.imm)) if self.color in self.imm[i])
        x = self.imm[y].index(self.color)
        self.p1 = (x,y)
        y1 = next(i for i in reversed(range(len(self.imm))) if self.color in self.imm[i])
        x1 = max(i for i, col in enumerate(self.imm[y1]) if col == self.color)
        self.p2 = (x1,y1)
        self.p3 = (self.p1[0], self.p2[1]) #1,0 BS
        self.p4 = (self.p2[0], self.p1[1]) #5,2 AD
    
        self.w = abs(self.p2[0] - self.p1[0]) +1
        self.h = abs(self.p1[1] - self.p2[1]) +1
        self.xmax = max([self.p1[0],self.p2[0],self.p3[0],self.p4[0]])
        self.ymax = max([self.p1[1],self.p2[1],self.p3[1],self.p4[1]])
        self.xmin = min([self.p1[0],self.p2[0],self.p3[0],self.p4[0]])
        self.ymin = min([self.p1[1],self.p2[1],self.p3[1],self.p4[1]])
        
        
    def __repr__(self):
        return f'Rec{self.color}rectangle with vertices {self.p1}, {self.p2}'
  
    
    def perimetro(self):
        p = [(self.p1[0],i) for i in range(self.p1[1],self.p3[1]+1)]\
                + [(self.p2[0],i) for i in range(self.p4[1],self.p2[1]+1)]\
                + [(i,self.p1[1]) for i in range(self.p1[0],self.p4[0]+1)]\
                + [(i,self.p3[1]) for i in range(self.p3[0],self.p2[0]+1)]
        return list(dict.fromkeys(p))
        

    def whosintersecating(self,imm):
        chi = set()
        for coordinata in self.perimetro():
            x = coordinata[0]
            y = coordinata[1]
            if imm[y][x] != self.color:
                chi.add(imm[y][x])
        return list(chi)

'''starting point of the procedural program'''


def colors(imm):
        lista = []
        for x in imm:
            lista += set(x)
        lista = set(lista)
        if (0,0,0) in lista:
            lista.remove((0,0,0))
        lista = [Rectangle(color,imm) for color in lista]
        return lista
# imm = images.load('random-50-991-1437.png')
# colors(imm)
# @profile
# def vertici(filename):
#     imm = images.load(filename)
#     # imm = [list(filter(lambda a: a != (0,0,0), row)) for row in imm]
#     rettangoli = []
#     for color in colors(imm):
#         y = next(i for i in range(len(imm)) if color in imm[i])
#         x = imm[y].index(color)
#         p1 = (x,y)
#         y1 = next(i for i in reversed(range(len(imm))) if color in imm[i])
#         x1 = max(i for i, col in enumerate(imm[y1]) if col == color)
#         p2 = (x1,y1)
#         rettangoli.append(Rectangle(p1, p2, color, imm))
#     return rettangoli

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
    

def diz_int(rettangoli):
    colori = {rettangolo.color:rettangolo for rettangolo in rettangoli}
    
    return {rettangolo: [colori[colore] for colore in rettangolo.whosintersecating(rettangolo.imm)] for rettangolo in rettangoli}
       

def lista_ordine(rettangoli):
    dic_int = diz_int(rettangoli)
    ordine = []
    while len(set(ordine)) < len(rettangoli):
        for rettangolo in dic_int:
            if dic_int[rettangolo] == []:
                ordine.append(rettangolo)
                for lista in dic_int.values():
                    if rettangolo in lista:
                        lista.remove(rettangolo)
    
    return list(reversed(dict.fromkeys(ordine)))


def converter(number):
    r = 0
    g = 0
    b = 0
    while number > 255:
        if number >= 256**2:
            r = 0
            while number > 256**2:
                number -= 256**2
                r += 1
        number -= 256
        g += 1
    b = number
    return (r,g,b)
        
    
def encodedimage(rettangoli):
    imm = []
    for rett in lista_ordine(rettangoli):
        x = rett.p1[0]
        y = rett.p1[1]
        lista = [converter(x),converter(y),converter(rett.w),converter(rett.h),rett.color]
        imm.append(lista)
    return imm


def boundingbox(rettangoli):
    xmin = min([rettangolo.xmin for rettangolo in rettangoli])
    xmax = max([rettangolo.xmax for rettangolo in rettangoli])
    ymin = min([rettangolo.ymin for rettangolo in rettangoli])
    ymax = max([rettangolo.ymax for rettangolo in rettangoli])
    return (xmin,ymin,xmax,ymax)

# @profile
def ex1(image_filename, encoded_filename):
    # image_filename = images.load(image_filename)
    # rettangoli = vertici(image_filename)
    rettangoli = colors(image_filename)
    # ordine = lista_ordine(rettangoli)
    enc = encodedimage(rettangoli)
    images.save(enc, encoded_filename)
    return boundingbox(rettangoli)
    



# imm = images.load('random-50-991-1437.png')
# colors(imm)

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
    

# imm = [list(filter(lambda a: a != (0,0,0), row)) for row in imm]

# ex1('random-15.png', 'encoded_random-15.png')
