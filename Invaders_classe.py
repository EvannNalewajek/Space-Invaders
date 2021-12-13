#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 14:29:05 2021

@author: evann.nalewajek
"""

class Alien : 
    def __init__(self,PosX, PosY, largeur, hauteur, deplacement, fenetre, Canvas):
        self.PosX = PosX
        self.PosY = PosY
        self.largeur = largeur
        self.hauteur = hauteur
        self.dpl = deplacement
        self.fenetre = fenetre
        self.canvas  = Canvas
        self.bob = self.canvas.create_rectangle(self.PosX-self.largeur,self.PosY-self.hauteur,self.PosX+self.largeur,self.PosY+self.hauteur,fill='green')
        
        
        

    #Déplacement de l'alien
    def deplacement(self):
        
        #Rebond à droite du Canvas
        if self.PosX + self.largeur + self.dpl > self.canvas.winfo_width() : 
            self.PosX = 2*(self.canvas.winfo_width()-self.largeur) - self.PosX
            self.dpl = -self.dpl
        
        #Rebond à gauche du Canvas
        if self.PosX  - self.largeur + self.dpl < 0 :
            self.PosX = 2*self.largeur - self.PosX
            self.dpl = -self.dpl
            
        
        self.PosX = self.PosX + self.dpl
        
       
        self.canvas.coords(self.bob, self.PosX-self.largeur, self.PosY-self.hauteur, self.PosX+self.largeur ,self.PosY+self.hauteur)
        self.fenetre.after(50,self.deplacement)    
            
class Vaisseau :
    def __init__(self,PosX, PosY, largeur, hauteur, deplacement, fenetre, Canvas):
        self.PosX = PosX
        self.PosY = PosY
        self.largeur = largeur
        self.hauteur = hauteur
        self.dpl = deplacement
        self.fenetre = fenetre
        self.canvas  = Canvas
        self.spoutnik = self.canvas.create_rectangle(self.PosX-self.largeur,self.PosY-self.hauteur,self.PosX+self.largeur,self.PosY+self.hauteur,fill='blue')
        
   
    def deplacement(self,event):
        print("bouge")
        if event.keysym == 'Left' :
            print("gauche")
            self.PosX -= self.dpl
            self.canvas.coords(self.spoutnik, self.PosX-self.largeur, self.PosY-self.hauteur, self.PosX+self.largeur ,self.PosY+self.hauteur)
        if event.keysym == 'Right' :
            print("droite")
            self.PosX += self.dpl
            self.canvas.coords(self.spoutnik, self.PosX-self.largeur, self.PosY-self.hauteur, self.PosX+self.largeur ,self.PosY+self.hauteur)
            
        