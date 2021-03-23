#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 11:19:52 2020

@author: tommasodimario
"""

import os

def bytes_and_files(pathname):
    max_size = 0
    size = (0, '')
    for filename in os.listdir(pathname):
        fullname = os.path.join(pathname, filename)
    if os.path.isfile(fullname):
        size[0] = os.stat(fullname).st_size
    if os.path.isdir(fullname):
        pass
    
def cascade(n):
    if len(str(n)) == 1:
        print(n)
    else:
        print(n)
        cascade(n//10)
        print(n)
        
def fibo(n):
    if n == 0:
        return n
    if n == 1:
        return n
    return fibo(n-2) + fibo(n-1)

def fib_iter(n):
    i = 0
    cur, nex = 0,1
    while i < n:
        cur, nex = nex, cur + nex
        i += 1
    return cur

def count_part(n,m):
    if n == 0:
        return 1
    if n < 0:
        return 0
    if m <= 0:
        return 0
    else:
        return count_part(n-m,m) + count_part(n, m-1)
    
count_part(6,4)