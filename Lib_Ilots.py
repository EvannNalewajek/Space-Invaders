# -*- coding: utf-8 -*-
"""
Created on Fri Jan 21 14:46:44 2022

@author: mathi
"""

from Lib_vaisseau import tirVaisseau

#création de la classe des ilots

class Ilots : 
    
    def __init__(self,Canvas,Mafenetre) :
        self.canevas = Canvas
        self.fenetre = Mafenetre
        self.x = 50
        self.y = 250
        self.hauteur = 5
        self.largeur = 5
        self.apparence = self.canevas.create_rectangle(self.x - self.largeur,\
                                                       self.y - self.hauteur,\
                                                           self.x + self.largeur,\
                                                               self.y + self.hauteur,\
                                                               fill = "grey")
 
    
    
    def Creation(self) : 
        
        