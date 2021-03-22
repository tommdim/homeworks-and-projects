#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 10:16:19 2020

@author: tommasodimario
"""

'''
accessing files
'''
file_handler = open('ciao.txt','w')
#buffer
file_handler.write('Ciao bro tapppost')
# Files have a sequential access from the first to the last bites











'''
write a funtion that takes as an input a filename and counts how may 0 and 1
are in the file. It returns a dictionary where the keys are '0' and '1'.
'''

def count01(filename):
    with open(filename) as f:
        string = f.read()
    dic = {'0':0, '1':0}
    for letter in string:
        if letter == '0':
            dic['0'] += 1
        elif letter == '1':
            dic['1'] += 1
    return dic



def count01_oneliner(filename):
    return {letter: open(filename).read().count(letter) for letter in ('0','1')}



def count_lines(f1,f2):
    with open(f1) as f1:
        with open(f2, 'w') as g:
            for line in f1:
                g.write(str(len(line)) + '\n')
    
        





































