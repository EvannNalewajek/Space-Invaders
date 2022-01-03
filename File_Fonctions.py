# -*- coding: utf-8 -*-
"""
Created on Mon Jan  3 15:36:34 2022

@author: evann
"""

def Est_vide(L):
    return L==[]

def Ajouter(L,a):
    L.append(a)
    return L

def Retirer(L):
    if Est_vide(L)==False:
        L.pop(0)
    return L

def Premier(L):
    return L[0]