#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 14:03:32 2020

@author: tommasodimario
"""
'''
Write a function that takes a list of strings as an input and returns a 
list with the same strings, ordered by length of the strings
'''

def order(string_list):
    dic = {}
    
    for string in string_list:
        l = len(string)
        if l in dic:
            dic[l] += string
        else:
            dic[l] = [string]
    new = []
    for k in sorted(dic):
        new.extend(dic[k])
    return new

string_list = ['caio','oare','cucu','franchina']
sorted(string_list, key=len)
def alphalen(s):
    return len(s), s
sorted (string_list, key = alphalen)
sorted(string_list, key = lambda x: (len(x),x))
'''write a key function that sorts the words according to the last letter 
of the string'''
def key_function(s):
    return s[-1]

sorted(string_list, key = key_function)

'''
write a key function for sorting a list of integers according to the 
remainder for the division of 7 and, in case of a tie, according to the value
of the integers
'''
def key_function1(n):
    remainder = n % 7
    return remainder, n

'''
Write a funtion that takes as an input a string containing a series of words
separated by spaces and builds a dictionary where the keys are the last 
letters of the words in the string and the associated valus are lists with 
the words in the string and athe associated values are lists with the words
ending with that letter 
The lists must be ordered lexicographically.
'''
def dict_last_letter(string):
    dic = {}
    list_strings = string.split()
    for word in list_strings:
       dic[word[-1]] = dic.get(word[-1], []) + [word]
        # if word[-1] in dic:
        #     dic[word[-1]] += [word]
        # else:
        #     dic[word[-1]] = [word]
    return {k: sorted(dic[k]) for k in dic}
    
    
    






