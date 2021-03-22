#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 09:30:55 2020






@author: tommasodimario
"""
f = ['pea', 'rpai', 'rpai', 'schiai', 'pea', 'rpe', 'zoi', 'zoi', 'briai', 'rpe']
# @profile
def prosodic_verses(length_verses,final_es):
    
    prosodic_zip = []
    
    prosodic_list=[]
    dic = {}
    prosodic_zip=list(zip(final_es,length_verses))
    setting_zip= list(dict.fromkeys(prosodic_zip))
    count = 0
    for element in setting_zip:
        if dic[element] not in dic:
            dic[element] = count
    for x in prosodic_zip:
        prosodic_list.append()
        
    
    
    return dic

def lista_prosodia(escount, finali):
    tuples = list(zip(escount,finali))
    number = 0
    dic = {}
    for tupla in list(dict.fromkeys(tuples)):
        dic[tupla] = number
        number += 1
    prosodia = [dic[tupla] for tupla in tuples]
    return prosodia

[('pea', 13),
 ('rpai', 14),
 ('rpai', 14),
 ('schiai', 8),
 ('pea', 13),
 ('rpe', 13),
 ('zoi', 14),
 ('zoi', 14),
 ('briai', 8),
 ('rpe', 13)]
# prosodic_verses([13, 14, 14, 8, 13, 13, 14, 14, 8, 13],['pea', 'rpai', 'rpai', 'schiai', 'pea', 'rpe', 'zoi', 'zoi', 'briai', 'rpe'])
'''def periodo(prosodia):
    
    lista = sorted(divisors(prosodia))
    if len(prosodia) == len(set(prosodia)):
        return min(lista)
    for d in lista:
        lista1 = prosodia[:d]
        lista2 = prosodia[d:d*2]
        if periodinho(prosodia, d) == True:
            zipp = list(zip(lista1,lista2))
            szipp = set(zip(lista1,lista2))
            if len(set(lista1)) == len(set(lista2)) and len(set(zip(lista1,lista2))) < len(list(zip(lista1,lista2))):
                return d'''
"""
Sia dato un testo che contiene un poema, ovvero una successione di versi in rima.
Il poema è contenuto in un file, un verso per riga.

Vogliamo analizzarlo per estrarne la struttura prosodica, ovvero lo schema poetico in esso usato.
Per far questo sono utili le seguenti definizioni:
    - un 'elemento sonoro' (ES) è una successione massimale di 1 o più consonanti seguite da 1 o più vocali
        - prima tutte le consonanti
        - poi tutte le vocali (aeiouyj)
        - ignorando eventuali caratteri non alfabetici come spazi, numeri e segni di interpunzione 
        - togliendo gli accenti dalle lettere accentate
        - e ignorando la differenza tra maiuscole e minuscole
        NOTA:   fanno eccezione il primo ES di un verso, che può essere composto da sole vocali
                e l'ultimo ES, che può essere composto di sole consonanti
    - un verso è composto da una successione di elementi sonori, l'ultimo dei quali è chiamato 'finale'
        Esempio:      
        Se il verso è "Paperino andò al mare a pescare" 
            - gli elementi sonori sono     ["pa", "pe", "ri", "noa", "ndoa", "lma", "rea", "pe", "sca", "re"]
            - la finale è                   "re"
            - il verso è lungo              10 ES
        notate che le lettere accentate hanno perso l'accento e non ci interessa la distinzione tra maiuscole e minuscole
    - la struttura prosodica di una poesia è una lista di interi, uno per ciascun verso
    - per ciascun verso si considerano sia il numero di ES (#ES) che la sua finale
    - al primo verso va associato il numero 0
    - a ciascuno dei versi successivi va associato:
        - l'intero che è stato già associato ad un verso precedente che ha stesso #ES e finale
        - altrimenti un nuovo intero (che segue l'ultimo già usato)
    Esempio:
        se la poesia è quella qui sotto                     gli elementi sonori sono                                    #ES finale   prosodia
        '''
        Dì pestaggio tessessi allarmai, Partenopea!         di pe sta ggio te sse ssia lla rmai pa rte no pea'           13  pea         0
        Sembrò svieremo imbarcate, aumentarono usurpai?     se mbro svie re moi mba rca teau me nta ro nou su rpai      14  rpai        1
        Flash privé spirereste? Pentecoste deturpai         fla shpri ve spi re re ste pe nte co ste de tu rpai         14  rpai        1
        scrost, direttamante arrischiai,                    scro stdi re tta ma ntea rri schiai                          8  schiai      2
        odi attuazione vernicera Partenopea.                o dia ttua zio ne ve rni ce ra pa rte no pea                13  pea         0
        Psion trentacinque preesistiti calzascarpe          psio ntre nta ci nque pree si sti ti ca lza sca rpe         13  rpe         3
        nobilt fiacchi vedesti avvertirsi spermatozoi?      no bi ltfia cchi ve de stia vve rti rsi spe rma to zoi      14  zoi         4
        Igloo rubi incassando giurati spermatozoi!          i gloo ru bii nca ssa ndo giu ra ti spe rma to zoi          14  zoi         4
        Saprai reputasse inebriai                           sa prai re pu ta ssei ne briai                               8  briai       5
        man l'ballaste segnaleremo soprascarpe.             ma nlba lla ste se gna le re mo so pra sca rpe             13  rpe         3
        '''
        l'elenco dei numeri di ES è     [13,    14,     14,     8,        13,    13,    14,    14,    8,       13   ]
        l'elenco delle finali è         ['pea', 'rpai', 'rpai', 'schiai', 'pea', 'rpe', 'zoi', 'zoi', 'briai', 'rpe']
        quindi la struttura prosodica è [0,     1,      1,      2,        0,     3,     4,     4,     5,       3    ]

        Dalla struttura prosodica dovete determinare il periodo, ovvero la lunghezza minima di un gruppo di versi che si ripete
        con lo stesso schema. 
        In questo esempio il modulo = 5, infatti la prosodia è formata da due sequenze uguali di 5 elementi 
        che seguono lo schema [0, 1, 1, 2, 0], infatti [0, 1, 1, 2, 0] è equivalente a [3, 4, 4, 5, 3]

        La funzione deve tornare la tupla che contiene nell'ordine i 4 valori: 
            - prosodia: ovvero la lista di interi che avete calcolato da #ES e lunghezza dei versi
            - periodo:  ovvero la lunghezza minima dello schema prosodico che si ripete
            - lunghezze: ovvero la lista delle lunghezze (#ES) dei versi
            - finali:   ovvero la lista degli ES finali di ciascun verso

        Quindi per questo esempio la funzione deve tornare la tupla:
          ( [0, 1, 1, 2, 0, 3, 4, 4, 5, 3], 5, [13, 14, 14, 8, 13, 13, 14, 14, 8, 13 ], 
            ['pea', 'rpai', 'rpai', 'schiai', 'pea', 'rpe', 'zoi', 'zoi', 'briai', 'rpe'])

    ATTENZIONE: non potete usare altre librerie o aprire altri file.
    TIMEOUT: Il timeout per questo esercizio è di 100ms (0.1 secondi)
"""
# @profile'''
'''def remove_schar(filename):
    with open(filename) as f:
        string = f.read()
    s_char = {228: 97,225: 97,224: 97, 226: 97,227: 97,229: 97,
               235: 101,233: 101,232: 101,234: 101,283: 101,
               239: 105,237: 105,236: 105,238: 105,
               246: 111,243: 111,337: 111,242: 111,244: 111,245: 111,248: 111,
               252: 117, 250: 117,369: 117,249: 117,251: 117,
               255: 121, 253: 121,
               192: 97, 193: 97,194: 97,195: 97,196: 97,197: 97,
               200: 101,201: 101,202: 101,203: 101, 204: 105,205: 105,206: 105,207: 105,
               210: 111,211: 111,212: 111,213: 111,214: 111,216: 111,
               217: 117,218: 117,219: 117,220: 117,221: 121,376: 121,
               65: 97,66: 98,67: 99,68: 100,69: 101, 70: 102,71: 103,72: 104,73: 105,
               74: 106,75: 107,76: 108,77: 109,78: 110,79: 111,80: 112,81: 113,
               82: 114,84: 116,83: 115,85: 117,86: 118,87: 119,88: 120,
               89: 121,90: 122,
               32: '', 33:'', 34:'', 39:'', 44:'', 46:'', 58:'', 59:'', 63:'',
               48:'',49:'',50:'',51:'',52:'',53:'',54:'',55:'',56:'',57:''} 
    string = string.translate(s_char)
    return string.split('\n')[:-1] 



# def es_counter(verso):
#     counter = 0
#     for i, c in enumerate(verso[:-1]):
#         if c in 'aeioujy' and verso[i+1] not in 'aeioujy':
#             counter += 1
            
#     return counter +1

# @profile
# def es_counter(verso):
#     v_c = ''.maketrans('aeioujybcdfghklmnpqrstvwxz','vvvvvvvccccccccccccccccccc')
#     lista = verso.translate(v_c)
#     es_count = len(lista.split('vc'))
#     return es_count
# @profile
# def es_counter(lista):
#     v_c = ''.maketrans('aeioujybcdfghklmnpqrstvwxz','vvvvvvvccccccccccccccccccc')
#     lista_len = []
#     # lista_finali = []
#     for verso in lista:
#         versotrans = verso.translate(v_c)
#         index_fin = versotrans.rfind('vc')
        
#         lista_finali.append(verso[index_fin +1:])
#         es_count = len(versotrans.split('vc'))
#         lista_len.append(es_count)
   
        
#     return lista_len

# def final_es(lista):
#     v_c = ''.maketrans('aeioujybcdfghklmnpqrstvwxz','vvvvvvvccccccccccccccccccc')
#     lista_finali = []
#     for verso in lista:
#         versotrans = verso.translate(v_c)
#         index_fin = versotrans.rfind('vc')
#         lista_finali.append(verso[index_fin +1:])
#     return lista_finali
            
    
# @profile
def lista_prosodia(escount, finali):
    tuples = list(zip(escount,finali))
    number = 0
    dic = {}
    for tupla in list(dict.fromkeys(tuples)):
        dic[tupla] = number
        number += 1
    prosodia = [dic[tupla] for tupla in tuples]
    return prosodia

# @profile
# def final_es(lista):
#     finali = []
#     for verso in lista:
#         for i in range(len(verso) -1,0,-1):
#                 if not verso[i] in 'aeioujy' and verso[i-1] in 'aeioujy':
#                     finali.append(verso[i:])
#                     break
#     return finali
# def final_es(lista):
#     lista_finali = []
#     for verso in lista:
#         rev = verso[::-1]
#         for i, char in enumerate(rev):
#             if not char in 'aeioujy' and rev[i + 1] in 'aeioujy':
#                 lista_finali.append( rev[:i+1][::-1])
#                 break
#     return lista_finali             
    
def divisors(prosodia):
    n = len(prosodia)
    lista = []
    for i in range(2, int(n ** 0.5 + 1)):   
        if n % i == 0:
            lista.extend([i, n//i])
    if 2 in lista:
        lista.remove(2)
    return set(lista)

def periodinho(prosodia , d):
    lista1 = prosodia[:d]
    for i in range(1, d//2):
            listan = prosodia[d*i:d+d*i]
            if len(set(lista1)) == len(set(listan)) or len(set(zip(lista1,listan))) < len(list(zip(lista1, listan))):
                    return True
    return False
# @profile   
def periodo(prosodia):
    # get max difference
    lista = sorted(divisors(prosodia))
    for d in lista:
        lista1 = prosodia[:d]
        lista2 = prosodia[d:d*2]
        # if len(set(lista1)) == len(set(lista2)) and len(set(zip(lista1,lista2))) < len(list(zip(lista1,lista2))):
        # for i in range(1, d//2):
        #     listan = prosodia[d*i:d+d*i]
        #     if not len(set(lista1)) == len(set(listan)) and len(set(zip(lista1,listan))) < len(list(zip(lista1, listan))):
        #             break
        if periodinho(prosodia, d) == True:
            
            if len(set(lista1)) == len(set(lista2)) and len(set(zip(lista1,lista2))) < len(list(zip(lista1,lista2))):
                return d

# @profile
def ex1(poem_filename):
    lista = remove_schar(poem_filename)
    v_c = ''.maketrans('aeioujybcdfghklmnpqrstvwxz','vvvvvvvccccccccccccccccccc')
    finali = []
    lunghezze = []
    for verso in lista:
        versotrans = verso.translate(v_c)
        index_fin = versotrans.rfind('vc')
        
        finali.append(verso[index_fin +1:])
        es_count = len(versotrans.split('vc'))
        lunghezze.append(es_count)
    
     
    # lunghezze = es_counter(lista)#list(map(es_counter, lista))
    # finali = final_es(lista)
    prosodia = lista_prosodia(lunghezze,finali)
    period = periodo(prosodia)
    return (prosodia,period,lunghezze,finali)

# ex1('random-2592-rnd.txt')
'''''''
def remove_schar(filename):
    with open(filename) as f:
        string = f.read()
    s_char = {228: 97,225: 97,224: 97, 226: 97,227: 97,229: 97,
               235: 101,233: 101,232: 101,234: 101,283: 101,
               239: 105,237: 105,236: 105,238: 105,
               246: 111,243: 111,337: 111,242: 111,244: 111,245: 111,248: 111,
               252: 117, 250: 117,369: 117,249: 117,251: 117,
               255: 121, 253: 121,
               192: 97, 193: 97,194: 97,195: 97,196: 97,197: 97,
               200: 101,201: 101,202: 101,203: 101, 204: 105,205: 105,206: 105,207: 105,
               210: 111,211: 111,212: 111,213: 111,214: 111,216: 111,
               217: 117,218: 117,219: 117,220: 117,221: 121,376: 121,
               65: 97,66: 98,67: 99,68: 100,69: 101, 70: 102,71: 103,72: 104,73: 105,
               74: 106,75: 107,76: 108,77: 109,78: 110,79: 111,80: 112,81: 113,
               82: 114,84: 116,83: 115,85: 117,86: 118,87: 119,88: 120,
               89: 121,90: 122,
               32: '', 33:'', 34:'', 39:'', 44:'', 46:'', 58:'', 59:'', 63:'',
               48:'',49:'',50:'',51:'',52:'',53:'',54:'',55:'',56:'',57:''} 
    string = string.translate(s_char)
    return string.split('\n')[:-1] 


# @profile
def lista_prosodia(escount, finali):
    tuples = list(zip(escount,finali))
    number = 0
    dic = {}
    for tupla in list(dict.fromkeys(tuples)):
        dic[tupla] = number
        number += 1
    prosodia = [dic[tupla] for tupla in tuples]
    return prosodia


def divisors(prosodia):
    n = len(prosodia)
    lista = []
    for i in range(2, int(n ** 0.5 + 1)):   
        if n % i == 0:
            lista.extend([i, n//i])
    if 2 in lista:
        lista.remove(2)
    return set(lista)


def periodinho(prosodia , d):
    lista1 = prosodia[:d]
    for i in range(1, d//2):
            listan = prosodia[d*i:d+d*i]
            if len(set(lista1)) == len(set(listan)) or len(set(zip(lista1,listan))) < len(list(zip(lista1, listan))):
                    return True
    return False
# @profile   
def periodo(prosodia):
    lista = sorted(divisors(prosodia))
    for d in lista:
        lista1 = prosodia[:d]
        lista2 = prosodia[d:d*2]
        if periodinho(prosodia, d) == True:
            
            if len(set(lista1)) == len(set(lista2)) and len(set(zip(lista1,lista2))) < len(list(zip(lista1,lista2))):
                return d
def casistrani(prosodia):
    lista = sorted(divisors(prosodia))
    if len(set(prosodia)) == len(list(prosodia)):
        return min(lista)
# @profile
def ex1(poem_filename):
    lista = remove_schar(poem_filename)
    v_c = ''.maketrans('aeioujybcdfghklmnpqrstvwxz','vvvvvvvccccccccccccccccccc')
    finali = []
    lunghezze = []
    for verso in lista:
        versotrans = verso.translate(v_c)
        index_fin = versotrans.rfind('vc')
        
        finali.append(verso[index_fin +1:])
        es_count = len(versotrans.split('vc'))
        lunghezze.append(es_count)
    prosodia = lista_prosodia(lunghezze,finali)
    period = periodo(prosodia)
    return (prosodia,period,lunghezze,finali)
'''