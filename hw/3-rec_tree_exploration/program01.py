#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" Nikita, a clever spy, needs to follow a series of clues (namely a
sequence of words) that will lead her to discover one or more secret
information (sequences of words).  To find the secret(s) Nikita has to
visit different cities: in each city Nikita will find which is the
next city she has to move to and will also get a new word of the
secret.  The next city you have to move to depends on the next clue.

It is a bit like a treasure hunt, in which Nikita explores a network
of cities, collecting information.

NOTE: From the same city, the same clue can lead to multiple
    alternative cities.  So the paths to explore could be multiple and
    the secrets more than one.

NOTE: if in a certain city the instruction corresponding to the next
    clue is missing, this means that the enemy spy network has
    captured and destroyed the information. This also means the secret
    that Nikita was following with that sequence cannot be completed
    anymore.  Thus, our spy quits that sequence and she tries to
    complete all the other secrets she has already collected.

We want to reconstruct all the secrets that Nikita could reconstruct,
given the available clues and the pieces of instructions scattered
throughout the different cities.

The instructions about how to move between the cities are contained in
a text file, according to the following format:
- every line starting with the '#' character should be ignored
- cities are always written in UPPERCASE
- the clues and words of the secret(s) to be discovered are always
  written in lowercase letters

The file contains, separated by at least one space/tab/return, zero or
more instructions to follow.  Each instruction is written as the
concatenation of four words:
    - city 	  (UPPERCASE word)
    - clue 	  (lowercase word)
    - destination (UPPERCASE word)
    - secret 	  (lowercase word)

Example:
    the instruction ROMAcarciofoPARIGIchampagne indicates that
        - when the spy is in                         'ROME'
        - if the following clue is                   'carciofo'
        - the spy must go to                         'PARIGI'.
        - and add to the secret the word             'champagne'

NOTE: You can assume that the each line of instruction is unique.
NOTE: There may be different instructions that even starting from the
      same city AND having the same clue, lead to different cities and/or
      produce different secrets.
    Example:
    ROMAcarciofoPARIGIchampagne
    ROMAcarciofoCANCANCANCUNchampagne
    ROMAcarciofoPARIGImitraglietta
    ROMAcarciofoCATANZAROcommissario

Design and implement the function ex1(instructions_file, initial_city, clues)
recursive or using recursive functions or methods, which receives as
arguments:
 - instructions_file: the name of a text file that contains
                      instructions to follow in each city
 - initial_city:      the name of the initial city from which Nikita
                      starts her journey (UPPERCASE word)

 - clues:             a list of clues (string of lowercase words separated
                      by spaces) 

that reconstructs all the possible secrets Nikita can discover and that
returns the set of ALL possible pairs (secret, CITY), where:

- secret is one of the possible secrets Nikita can discover, namely a
         string obtained by the concatenation of the words collected,
         separated by space
- CITY   is the city reached by Nikita when she completed that secret.

Example:

If the file is 'example.txt', the starting city is 'ROMA' and the
clues are "la bocca sollevò dal fiero pasto", then all the possible
secret/city pairs will be:
     ('vendita diamanti rubati stanotte ad anversa', 'CANCUN')
     ('vendita cannoni mercato nero del cairo',      'CANCUN')
     ('furto di diamanti a buckingham palace',       'MILANO')
     ('mata hari ha sedotto ambasciatore zambia',    'MILANO')


NOTE: it is forbidden to import/use other libraries or open files
      except the one indicated

NOTE: The test system recognizes recursion ONLY if the recursive
      function/method is defined in the outermost level.  DO NOT
      define the recursive function within another function/method
      otherwise you will fail all the tests.

"""

def  ex1(instructions_file, initial_city, clues):
	# @profile
	def clean_input(lista):
		lista1 = []
		for word in lista:
			if not word.startswith('#'):
					lista1.append(word.strip())
		lista1 = ' '.join(lista1).split()
		return [ups(lista) for lista in lista1]

	# @profile
	def ups(s):
		v = ''
		for l in s:
			if l.islower():
				v += l
				s = s.replace(l, ' ')
			else:
				v += ' '
		s1 = v.split()
		s2 = s.split()
		return [s2[0],s1[0],s2[1],s1[1]]
		

	# @profile
	def  ex1(istructions_file, initial_city, clues):
		with open(istructions_file) as f:
			file = f.readlines()
			instr = clean_input(file)
			clues = clues.split()
			dizionario = {}
			for lista in instr:
				dizionario[(lista[0], lista[1])] = dizionario.get((lista[0], lista[1]), []) + [(lista[2], lista[3])]
			if dizionario == {}:
				return set()
			leng = len(clues)
			x = rec(dizionario, initial_city, clues, leng)
		return x


	# @profile
	def rec(dic, city, clues, leng, tot = set(), i=0, segreto = ''):
	
		if i == leng:
			return {(segreto.strip(), city)}
		
		for instr in dic.get((city, clues[i]), []):
			seg = segreto + f'{instr[1]} '
			tot.update(rec(dic, instr[0], clues, leng, tot, i + 1, seg))#reto + instr[1]+ ' '))

		return tot


