# -*- coding: utf-8 -*-
"""
Created on Mon Jan 10 10:26:24 2022

@author: mathi
"""
from tkinter import Tk, Label, Button, Canvas, PhotoImage
import File_Fonctions as ff
import Lib_Alien


#Création de la fenêtre graphique
Mafenetre=Tk()
Mafenetre.title('Space Invaders')

#Création du widget bouton quitter
buttonQuitt = Button (Mafenetre, text="QUITTER", fg = 'red', command = Mafenetre.destroy)
buttonQuitt.grid(row=0,column=2)

#Canevas
hauteurC = 480
largeurC = 640


#Importation des images
ImageVaisseau=PhotoImage(file='spaceship.gif')
ImageDestroy=PhotoImage(file='spaceshipdestroy.gif')
ImageAlien=PhotoImage(file='invader.gif')
ImageFond=PhotoImage(file='space.gif')



#Caractéristiques des aliens
largeur_alien = 22      
hauteur_alien = 16
ecart_alien = 10
hauteur_ligne = 50
nbre_alien = 15
descente_alien = 10
VitesseDeplacement = 10
VitesseAlien = 0.5

#Caractéristiques des tirs
FileTir=[]
FileTirAlien=[]
vitesse_tir=1
Peut_Tirer=True


class Spaceship:
    
    def __init__(self):
        self.largeur = 30
        self.hauteur = 32
        self.x = 15
        self.y = hauteurC - self.hauteur - 5
        self.vitesse = 10
        self.image = PhotoImage(file='spaceship.gif')
        self.apparence=canevas.create_image(self.x,self.y,image = self.image)
        
    def deplacement(self,dir):
        if self.x >= self.largeur and dir==-1:
            self.x += self.vitesse * dir
        elif self.x <= largeurC - self.largeur and dir==1:
            self.x += self.VitesseDeplacement * dir
        self.Affichage()
        
    def Affichage(self):
        canevas.coords(self.apparence,self.x,self.y)
        
    def Blesser(self):
        self.Etat1()
        Mafenetre.after(100,self.Etat2)
        Mafenetre.after(200,self.Etat1)
        Mafenetre.after(300,self.Etat2)
        Mafenetre.after(400,self.Etat1)
        Mafenetre.after(500,self.Etat2)

    def Etat1(self):
        canevas.itemconfig(self.apparence,image = ImageDestroy)
        
    def Etat2(self):
        canevas.itemconfig(self.apparence,image = self.image)
        
        
        
        
class tirVaisseau:
    
    Compteur=0
    def __init__(self,X,Y):
        self.x=X
        self.y=Y
        self.mouvement=True
        self.apparence=canevas.create_line(self.x, self.y, self.x, self.y + 5, fill = 'white')
        tirVaisseau.Compteur += 1
        
    def Affichage(self):
        canevas.coords(self.apparence,self.x,self.y,self.x,self.y+5)
        
    def Deplacement(self):
        if self.mouvement:
            self.y -= vitesse_tir
            self.Affichage()
            self.Toucher()
            Mafenetre.after(5,self.Deplacement)

    def Toucher(self):
        global ennemie
        if self.y < 0 :
            self.mouvement=False
            canevas.delete(self.apparence)
            ff.Retirer(FileTir)
            tirVaisseau.Compteur -= 1
        else:
            for i in ennemie:
                if i.vivant and self.y>=i.y and self.y <= i.y+hauteur_alien and self.x <= i.x+largeur_alien and self.x >= i.x:
                    self.Fin()
                    # canevas.delete(i.apparence)
                    i.vivant = False
                    i.Destruction()
        
    def Fin(self):
        self.mouvement=False
        canevas.delete(self.apparence)
        ff.Retirer(FileTir)
        tirVaisseau.Compteur-=1 
        
def Reload():
    global Peut_Tirer
    Peut_Tirer=True
    return Peut_Tirer
        
        
        
def MouvementVaisseau(event):
    global Peut_Tirer
    touche=event.keysym
    if touche=='Left':
        Spaceship.deplacement(-1)
    elif touche=='Right':
        Spaceship.deplacement(1)
    elif touche=='space':
        if Peut_Tirer:
            global FileTir
            ff.Ajouter(FileTir,tirVaisseau(Spaceship.x,Spaceship.y))
            FileTir[tirVaisseau.Compteur-1].Deplacement()
            Peut_Tirer=False
            Mafenetre.after(1000, Reload)
            
            
            
#Contrôle du vaisseau
canevas = Canvas(Mafenetre, width = largeurC, height = hauteurC, bg = 'black')
canevas.grid(row=2,column=1,columnspan=2)
canevas.grid_remove()
canevas.focus_set()