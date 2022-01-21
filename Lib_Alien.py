# -*- coding: utf-8 -*-
"""
Created on Mon Jan 10 10:12:39 2022

@author: mathi
"""

from tkinter import Tk , PhotoImage
import File_Fonctions as ff
from random import randint
from Lib_Vaisseau import Spaceship 
from newVersion import FinDePartie

#Canevas
hauteurC = 480
largeurC = 640

#Caractéristiques des aliens
nbre_alien = 15



class Alien:
    
    Compteur=0
    def __init__(self, Canvas, Mafenetre):
        self.Canvas = Canvas
        self.fenetre = Mafenetre
        Alien.Compteur += 1
        self.Compteur = Alien.Compteur
        self.largeur = 22
        self.hauteur = 16
        self.ecartEntre = 10
        self.vivant = True
        self.x = self.Compteur*(self.ecartEntre + self.largeur)
        self.y = 50
        self.dir = 1
        self.vitesse = 0.5
        self.descente = 10
        self.image = PhotoImage(file='invader.gif')
    
    def Creation(self):
        self.apparence = self.Canvas.create_image(self.x,self.y,image = self.image)

    def Affichage(self):
        self.Canvas.coords(self.apparence,self.x,self.y)
    
    def Destruction(self): 
        if self.vivant == False : 
            self.Canvas.delete(self.apparence)
            
    def MouvementAlien(self,ennemie):
        if (ennemie[-1].x + self.largeur >= largeurC and ennemie[-1].dir==1) or (ennemie[0].x - self.largeur <= 0 and ennemie[0].dir==-1):
            for i in ennemie:
                i.dir *= -1
                i.y += self.descente
        for i in ennemie:
            i.x += i.vitesse*i.dir
            i.Affichage()  
        self.fenetre.after(5,lambda : self.MouvementAlien(ennemie))
            
    def VictoireAlien(self,ennemie):
        for i in ennemie :
            if ennemie[i].x + self.hauteur >= Spaceship.x - Spaceship.hauteur : 
                FinDePartie()
        print("Perdu")
        
        
        
        
        
        
            
class TirAlien:
    
    def __init__(self,i, ennemie, Canvas, Mafenetre):
        self.Canvas = Canvas
        self.Mafenetre = Mafenetre
        self.x = ennemie[i].x
        self.y = ennemie[i].y
        self.apparence = self.Canvas.create_line(self.x , self.y-4 , self.x ,\
        self.y , fill='red')
        self.mouvement=True
        self.Deplacement()
        self.TirA = []
        self.Joueur = Spaceship.Spaceship()

    def Affichage(self):
        self.Canvas.coords(self.apparence , self.x , self.y-4 , self.x , self.y)
        
    def Deplacement(self):
        if self.mouvement:
            self.y += self.vitesseTir
            self.Affichage()
            self.Toucher()
            self.fenetre.after(5,self.Deplacement)
            
    def Toucher(self):
        if self.y > hauteurC :
            self.mouvement = False
            self.Canvas.delete(self.apparence)
            ff.Retirer(self.TirA)
        elif self.y >= self.Joueur.y-5 and self.y <= self.Joueur.y + 5 and \
            self.x <= self.Joueur.x + self.Joueur.largeur / 2  and \
            self.x >= self.Joueur.x - self.Joueur.largeur / 2 :
                self.mouvement = False
                self.Canvas.delete(self.apparence)
                ff.Retirer(self.TirA)
                self.Joueur.Vies -= 1
                self.Joueur.Blesser()
                #if Vies==0:
                    #C'est la défaite koi
                    
    def Tir_Alien(self,ennemie):
        L = [i.vivant for i in ennemie]
        i = randint(0,len(ennemie)-1)
        if L[i] :
            ff.Ajouter(self.TirA, TirAlien(i))
            self.fenetre.after(200,self.Tir_Alien)
        else:
            self.fenetre.after(5, self.Tir_Alien)

    

    
    
# class Alien_Bonus :
#     def __init__(self) : 
#        self.vivant = True
#        self.x = posX
#        self.y = hauteur_ligne
#        self.dir = 1
#        self.vitesse = VitesseAlien * 2
#        self.apparence = canevas.create_image(self.x,self.y, image = ImageVaisseau)
       


#     def Affichage(self):
#         canevas.coords(self.apparence,self.x,self.y)
         
        
#     def Mouvement(self):
#         if self.x + largeur_alien>=largeur and self.dir == 1 : 
#             self.dir = -1
#         elif self.x-largeur_alien<=0 and self.dir == -1 :
#             self.dir = 1
#         self.x += self.vitesse * self.dir
#         self.Affichage()
#         Mafenetre.after(5,self.Mouvement)
        
        
        
