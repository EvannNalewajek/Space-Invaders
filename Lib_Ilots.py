# -*- coding: utf-8 -*-
"""
Created on Fri Jan 21 14:46:44 2022

@author: mathi
"""

from Lib_vaisseau import tirVaisseau
from Lib_Alien import TirAlien

#création de la classe des ilots

class Ilots : 
    
    def __init__(self,Canvas,Mafenetre) :
        self.canevas = Canvas
        self.fenetre = Mafenetre
        self.x = 50
        self.y = 250
        self.hauteur = 3
        self.largeur = 20 
        self.vies = 3
        self.vivant = True
        self.apparence = self.canevas.create_rectangle(self.x - self.largeur,\
                                                       self.y - self.hauteur,\
                                                           self.x + self.largeur,\
                                                               self.y + self.hauteur,\
                                                               fill = "grey")
 
    
    
    def Creation(self) : 
        self.apparence
        
    def Destruction(self) : 
        if self.vivant == False:
            self.canevas.delete(self.apparence)
            
            
    def Entame(self) : 
        if 
        
        
        