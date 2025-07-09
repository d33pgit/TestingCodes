# -*- coding: utf-8 -*-
"""
Created on Sat Jun 28 13:56:46 2025

@author: SBUP
"""

def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
def calculate(a,b,cal):
    if cal =='add':
        return add(a,b)
    elif cal=='sub':
        return sub(a,b)
    elif cal=='mul':
        return mul(a,b)
    elif cal=='div':
        return div(a, b)
    else:
        raise ValueError("Invalid Operation")
    
        
        