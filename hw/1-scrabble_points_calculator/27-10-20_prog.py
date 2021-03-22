#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 11:22:40 2020

@author: tommasodimario
"""

'''making an histogram (multi-set)'''
def print_histogram(histogram):
    # iterarate over the hsitogram keys
    for the_char in histogram:
        aux_string  = the_char
    # for every key, print out as many | as the number of occurences we have
        aux_string += ' |' * histogram[the_char]
        print(aux_string)
            
# count the occurences of everh character in the string
def create_occurences_histogram(a_string):
    if not isinstance(a_string, str):
        print('strings only')
        return
    # initialize the data strcuture that retains the counts
    histogram = {}
    # go over all the characters in the string
    # and for every charater check if our histogram already has a key for it
    # check_string = 'abcdefghiljkmnopqrstuvzABC.....Z'
    # check_string = string.asciil requires import of a library
    a_string = a_string.lower()
    for a_char in a_string:
        a_char = a_char.lower()
        if (ord('a') <= ord(a_char) <= ord('z')):
            
            if a_char in histogram:
                histogram[a_char] += 1
            else:
                histogram[a_char] = 1
    print_histogram(histogram)
    # then update the value (either to 1, fi the key is new or +1 if the key
    # is not new)
    return histogram