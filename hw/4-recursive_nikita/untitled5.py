#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 22:04:19 2020

@author: tommasodimario

[['vendita diamanti rubati ha sedotto ambasciatore zambia', 'MILANO'],
 ['furto di diamanti a buckingham palace', 'MILANO'],
 ['mata hari ha sedotto ambasciatore zambia', 'MILANO']]
"""
'''BACK UP'''
# @profile
def pulisci(lista):
    lista1 = []
    for word in lista:
        if word[0] != '#':
            if word.strip() != '':
                lista1.append(word.strip())
    lista1 = ' '.join(lista1).split()
    return [ups(listina) for listina in lista1]

# @profile
def ups(string):
    # t1 = ''.maketrans('ABCDEFGHILMNOPQRSTUVZ','                     ')
    # s1 = string.translate(t1).split()
    # t2 = ''.maketrans('abcdefghilmnopqrstuvz', '                     ')
    # s2 = string.translate(t2).split()
    s1 = string
    for letter in s1:
        if letter.isupper():
            s1 = s1.replace(letter, ' ')
    s1 = s1.split()
    for letter in string:
        if letter.islower():
            string = string.replace(letter, ' ')
    s2 = string.split()
    return [s2[0],s1[0],s2[1],s1[1]]
        
        
            
    
# @profile
def  ex1(istructions_file, initial_city, clues):
    with open(istructions_file) as f:
        file = f.readlines()
        instr = pulisci(file)
        clues = clues.split()
        dic = {(cucu[0], cucu[1]):[(lista[2], lista[3]) for lista in instr if lista[0] == cucu[0] and lista[1] == cucu[1]] for cucu in instr} 
        # d = {clue: {città[0]: [[lista[2],lista[3]] for lista in instr if  lista[0] == città[0] and lista[1] == clue] for città in instr if [lista for lista in instr if  lista[0] == città[0] and lista[1] == clue] != []} for clue in clues}
        # dc = {città[0]: {clue: [[lista[2],lista[3]] for lista in instr if lista[1] == clue and lista[0] == città[0]] for clue in clues if [lista for lista in instr if lista[1] == clue and lista[0] == città[0]]}  for città in instr}
        x = rec(dic, initial_city, clues)
    return x



# @profile
def rec(dic, city, clues, i=0, segreto = {}):
    tot= set()
    
    if dic == {}:
        return set()
    
    if i == len(clues):
        return {(' '.join(segreto), city)}
        
    for instr in dic.get((city, clues[i]),[]):
        new_segreto = segreto.copy()
        new_segreto.append(instr[1])
        tot.update(rec(dic, instr[0], clues, i + 1, new_segreto))

    return tot

    '''FINE '''
 def up(s):
    lista = []
    pos = 0
    for i, e in enumerate(s):
        if e.isupper() and s[i+1].islower():
            lista.append(s[pos:i+1])
            pos = i + 1
        elif e.isupper() and s[i-1].islower():
            lista.append(s[pos:i])
            pos = i
    lista.append(s[pos:])
    return lista[1:]

    # start = [[lista[3],lista[2]] for lista in instr if lista[0] == initial_city and lista[1] == clues[0]]
        # start = find_r(clues, start, instr, index)
def find_r(clues, start, instr,index):
    #se la lunghezza dell'indizio è uguale alla lunghezza delle clues ritorna l'indizio
    if instr == []:
        return set()
    
    
    # if {len(lista[0].split()) for lista in start}  == {len(clues)}:
    #     return {tuple(lista) for lista in start}
    
    # if index > 5:
    #     return len(instr)
    
    # se trovi l'indizio e la città da cui eravamo aggiungi l'indizio e cambia la città
    for sta in start:    
        for lista in instr:
            if lista[0] == sta[1] and lista[1] == clues[index]:
                sta[0] += f' {lista[3]}'
                sta[1] = lista[2]
                return find_r(clues, start, instr, index + 1)
    
    # se la città da cui vieni ha più indizi sdoppia il segreto
# def ricorsione(cucu, instr, index, initial_city, clues):
#         while index < len(clues):
#             for lista in instr:
#                 for i in range(len(cucu)):
#                     if lista[0] == cucu[i][1] and lista[1] == clues[index]:
#                         cucu[i][1] = lista[2]
#                         cucu[i][0] += f' {lista[3]}'
                        
#             index += 1
        
#         # ricorsione(cucu,instr,index + 1,initial_city,clues)
#         return cucu

# #     pass
# # step = [lista for lista in instr if lista[0] == initial_city and lista[1] == clues[0]]
# # segreti = 
# step = [lista for lista in instr if lista[0] == initial_city and lista[1] == clues[0]]
#         cucu = [[lista[3], lista[2]] for i, lista in enumerate(step)]
#         # cucu = ricorsione(cucu,instr,index,initial_city,clues)

# idea assolutamente spastica
def pulisci(lista):
    lista1 = []
    for word in lista:
        if word[0] != '#':
            if word.strip() != '':
                lista1.append(word.strip())
    lista1 = ' '.join(lista1).split()
    return [up(listina) for listina in lista1]

def up(s):
    lista = []
    pos = 0
    for i, e in enumerate(s):
        if e.isupper() and s[i+1].islower():
            lista.append(s[pos:i+1])
            pos = i + 1
        elif e.isupper() and s[i-1].islower():
            lista.append(s[pos:i])
            pos = i
    lista.append(s[pos:])
    return lista[1:]

def  ex1(istructions_file, initial_city, clues):
    with open(istructions_file) as f:
        file = f.readlines()
        instr = pulisci(file)
        clues = clues.split()
        i = 0
        start = [[lista[3],lista[2]] for lista in instr if lista[0] == initial_city and lista[1] == clues[0]]
        # start = find_r(clues, start, instr, index)
        sdoppia = check_sdoppia(instr)
        x = spastica([], instr, 'ROMA', 0, clues, set(), sdoppia)
        
    return x
# segreto = []
# i = 0
# totalone = set()
# initial_city = 'ROMA'
def spastica(segreto, instr, city, i, clues, totalone, sdoppia):
    if len(totalone) == 4:
        return totalone
    
    
    
        
    if len(segreto) == len(clues):
        totalone.add((' '.join(segreto), city))
        ind = 0
        for lista in reversed(sdoppia):
            if lista[3] in segreto:
                instr.remove(lista)
                break
        return spastica([], instr, initial_city, 0, clues, totalone, sdoppia)
        
    for lista in instr:
        if lista[0] == city and lista[1] == clues[i]:
            segreto.append(lista[3])
            city = lista[2]
            # ind = instr.index(lista)
            return spastica(segreto, instr, city, i+1, clues, totalone, sdoppia)
    
def find_path(instr, city, clues, i, segreto = []):
    if clues[i] == clues[-1]:
        return segreto
    tot = set()
    for i, ins in enumerate(instr)
        for ins in find_path()
    
def permutations(my_list):
    if len(my_list) == 1:
        return [my_list]
    permutation_list = []
    for i, el in enumerate(my_list):
        for permutation in permutations(my_list[:i]+my_list[i+1:]):
            permutation_list.append([el]+permutation)
    return permutation_list


def check_sdoppia(instr):
    ripetizioni = []#set()
    for lista in instr:
        for l in instr:
            if l != lista and lista[0] == l[0] and lista[1] == l[1]:
                if l not in ripetizioni:
                    ripetizioni.append(l)
                elif lista not in ripetizioni:
                    ripetizioni.append(lista)
                break
    return ripetizioni

ex1('esempio.txt','ROMA','la bocca sollevò dal fiero pasto')