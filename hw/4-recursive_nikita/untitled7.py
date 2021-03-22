#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 14:15:23 2020

@author: tommasodimario
"""

from bintree import BinTree
from random import randint

def gen_random_tree(n, a, b, root = None, free = None):
    if n == 0:
        return root
    if root == None:
        root = BinTree(randint(a,b))
        free = [(root, 0), (root, 1)]
    else:
        node, side = free.pop(randint(0,len(free)-1))
        new_node = BinTree(randint(a,b))
        free.extend([(new_node,0), (new_node,1)])
        if side:
            node.right = new_node
        else:
            node.left = new_node
    return gen_random_tree(n-1, a,b,root,free)