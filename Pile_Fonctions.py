# -*- coding: utf-8 -*-
"""
Created on Mon Jan  3 15:51:05 2022

@author: evann
"""

def Est_vide(L):
    return L==[]

def Empiler(L,a):
    L.append(a)
    return L

def Depiler(L):
    if Est_vide(L)==False:
        L.pop()
    return L

def Sommet(L):
    return L[-1]