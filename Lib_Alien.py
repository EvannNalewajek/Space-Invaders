# -*- coding: utf-8 -*-
"""
Created on Mon Jan 10 10:12:39 2022

@author: mathi
"""

from tkinter import Tk , PhotoImage
import File_Fonctions as ff
from random import randint
from Lib_Vaisseau import Spaceship as vaisseau


#Canevas
hauteurC = 480
largeurC = 640

#Caractéristiques des aliens
nbre_alien = 15



#Importation des images
ImageVaisseau=PhotoImage(file='spaceship.gif')
ImageDestroy=PhotoImage(file='spaceshipdestroy.gif')
ImageAlien=PhotoImage(file='invader.gif')
ImageFond=PhotoImage(file='space.gif')




#Caractéristiques des tirs
FileTirAlien=[]
vitesse_tir=1


class Alien:
    
    Compteur=0
    def __init__(self, Canvas, Mafenetre):
        self.Canvas = Canvas
        self.Mafenetre = Mafenetre
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
            
    def MouvementAlien(self):
        global ennemie
        if (ennemie[-1].x + self.largeur >= largeurC and ennemie[-1].dir==1) or (ennemie[0].x - self.largeur <= 0 and ennemie[0].dir==-1):
            for i in ennemie:
                i.dir *= -1
                i.y += self.descente
        for i in ennemie:
            i.x += i.vitesse*i.dir
            i.Affichage()  
        self.fenetre.after(5,self.MouvementAlien)
            
            
class TirAlien:
    
    def __init__(self,i, Canvas, Mafenetre):
        self.Canvas = Canvas
        self.Mafenetre = Mafenetre
        self.x = ennemie[i].x
        self.y = ennemie[i].y
        self.apparence = self.Canvas.create_line(self.x , self.y-4 , self.x ,\
        self.y , fill='red')
        self.mouvement=True
        self.Deplacement()

    def Affichage(self):
        self.Canvas.coords(self.apparence , self.x , self.y-4 , self.x , self.y)
        
    def Deplacement(self):
        if self.mouvement:
            self.y+=vitesse_tir
            self.Affichage()
            self.Toucher()
            self.fenetre.after(5,self.Deplacement)
            
    def Toucher(self):
        global Vies
        if self.y > hauteurC :
            self.mouvement = False
            self.Canvas.delete(self.apparence)
            ff.Retirer(FileTirAlien)
        elif self.y >= vaisseau.y-5 and self.y <= vaisseau.y + 5 and \
            self.x <= vaisseau.x + vaisseau.largeur / 2  and \
            self.x >= vaisseau.x - vaisseau.largeur / 2 :
                self.mouvement = False
                self.Canvas.delete(self.apparence)
                ff.Retirer(FileTirAlien)
                Vies -= 1
                vaisseau.Blesser()
                #if Vies==0:
                    #C'est la défaite koi
                    
                    

    
def Tir_Alien():
    global ennemie,FileTirAlien
    L = [i.vivant for i in ennemie]
    i = randint(0,len(ennemie)-1)
    if L[i] :
        ff.Ajouter(FileTirAlien, TirAlien(i))
        Tk().after(200, Tir_Alien)
    else:
        Tk().after(5, Tir_Alien)
    
    
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
        
        
        
