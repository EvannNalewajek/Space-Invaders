# -*- coding: utf-8 -*-
"""
Created on Sun Jan  2 17:03:43 2022

@author: evann
"""

from tkinter import Tk, Label, Button, Canvas, PhotoImage
import File_Fonctions as ff
import Pile_Fonctions as pf
from random import randint

#Création de la fenêtre graphique
Mafenetre=Tk()
Mafenetre.title('Space Invaders')

#Création du widget bouton quitter
buttonQuitt = Button (Mafenetre, text="QUITTER", fg = 'red', command = Mafenetre.destroy)
buttonQuitt.grid(row=0,column=2)

#Canevas
hauteur=480
largeur=640

#Affichage du score
score=Label(Mafenetre,text='Score: 0')
score.grid(row=1,column=1)

#Affichage de la vie
NbrVies=Label(Mafenetre,text="Vies: 3")
NbrVies.grid(row=1,column=2)

#Importation des images
ImageVaisseau=PhotoImage(file='spaceship.gif')
ImageDestroy=PhotoImage(file='spaceshipdestroy.gif')
ImageAlien=PhotoImage(file='invader.gif')
ImageFond=PhotoImage(file='space.gif')



#Caractéristiques du vaisseau
largeur_vaisseau=30
hauteur_vaisseau=32
posX=largeur/2
posY=hauteur-hauteur_vaisseau-5

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

#Création des classes
class Spaceship:
    
    def __init__(self):
        self.x=posX
        self.y=posY
        self.apparence=canevas.create_image(self.x,self.y,image=ImageVaisseau)


    def deplacement(self,dir):
        if self.x>=largeur_vaisseau and dir==-1:
            self.x+=VitesseDeplacement*dir
        elif self.x<=largeur-largeur_vaisseau and dir==1:
            self.x+=VitesseDeplacement*dir
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
        canevas.itemconfig(self.apparence,image=ImageDestroy)
        
    def Etat2(self):
        canevas.itemconfig(self.apparence,image=ImageVaisseau)
    

class Alien:
    
    Compteur=0
    def __init__(self):
        Alien.Compteur += 1
        self.Compteur=Alien.Compteur
        self.vivant=True
        self.x=self.Compteur*(ecart_alien+largeur_alien)
        self.y=hauteur_ligne
        self.dir=1
        self.vitesse=VitesseAlien
    
    def Creation(self):
        self.apparence=canevas.create_image(self.x,self.y,image=ImageAlien)

    def Affichage(self):
        canevas.coords(self.apparence,self.x,self.y)
    
    def Destruction(self): 
        if self.vivant == False : 
            canevas.delete(self.apparence)
        
        
class tirVaisseau:
    
    Compteur=0
    def __init__(self,X,Y):
        self.x=X
        self.y=Y
        self.mouvement=True
        self.apparence=canevas.create_line(self.x, self.y, self.x, self.y+5,fill='white')
        tirVaisseau.Compteur += 1
        
    def Affichage(self):
        canevas.coords(self.apparence,self.x,self.y,self.x,self.y+5)
        
    def Deplacement(self):
        if self.mouvement:
            self.y-=vitesse_tir
            self.Affichage()
            self.Toucher()
            Mafenetre.after(5,self.Deplacement)

    def Toucher(self):
        if self.y<0:
            self.mouvement=False
            canevas.delete(self.apparence)
            ff.Retirer(FileTir)
            tirVaisseau.Compteur-=1
        else:
            for i in ennemie:
                if i.vivant and self.y>=i.y and self.y<=i.y+hauteur_alien and self.x<=i.x+largeur_alien and self.x>=i.x:
                    self.Fin()
                    # canevas.delete(i.apparence)
                    i.vivant = False
                    i.Destruction()
        
    def Fin(self):
        self.mouvement=False
        canevas.delete(self.apparence)
        ff.Retirer(FileTir)
        tirVaisseau.Compteur-=1

class TirAlien:
    
    def __init__(self,i):
        self.x=ennemie[i].x
        self.y=ennemie[i].y
        self.apparence=canevas.create_line(self.x , self.y-4 , self.x ,\
        self.y , fill='red')
        self.mouvement=True
        self.Deplacement()

    def Affichage(self):
        canevas.coords(self.apparence , self.x , self.y-4 , self.x , self.y)
        
    def Deplacement(self):
        if self.mouvement:
            self.y+=vitesse_tir
            self.Affichage()
            self.Toucher()
            Mafenetre.after(5,self.Deplacement)
            
    def Toucher(self):
        global Vies
        if self.y>hauteur:
            self.mouvement = False
            canevas.delete(self.apparence)
            ff.Retirer(FileTirAlien)
        elif self.y>=vaisseau.y-5 and self.y<=vaisseau.y+5 and\
            self.x<=vaisseau.x+largeur_vaisseau/2 and\
            self.x>=vaisseau.x-largeur_vaisseau/2 :
                self.mouvement=False
                canevas.delete(self.apparence)
                ff.Retirer(FileTirAlien)
                Vies-=1
                vaisseau.Blesser()
                #if Vies==0:
                    #C'est la défaite koi


def MouvementAlien():
    global ennemie
    if (ennemie[-1].x+largeur_alien>=largeur and ennemie[-1].dir==1) or (ennemie[0].x-largeur_alien<=0 and ennemie[0].dir==-1):
        for i in ennemie:
            i.dir*=-1
            i.y+=descente_alien
    for i in ennemie:
        i.x+=i.vitesse*i.dir
        i.Affichage()  
    Mafenetre.after(5,MouvementAlien)
    
def Tir_Alien():
    global ennemie,FileTirAlien
    L=[i.vivant for i in ennemie]
    i=randint(0,len(ennemie)-1)
    if L[i]:
        ff.Ajouter(FileTirAlien,TirAlien(i))
        Mafenetre.after(200,Tir_Alien)
    else:
        Mafenetre.after(5,Tir_Alien)

def NouvellePartie():
    global vaisseau,ennemie,Vies
    canevas.grid()
    canevas.create_image(0,0,image=ImageFond)
    buttonStart.grid_remove()
    vaisseau=Spaceship()
    Vies=3
    ennemie=[]
    for i in range(nbre_alien):
        ennemie.append(Alien())
    for i in ennemie:
        i.Creation()
    MouvementAlien()
    Tir_Alien()
    
def Reload():
    global Peut_Tirer
    Peut_Tirer=True
    return Peut_Tirer

    # AlienB = Alien_Bonus()
    # Mafenetre.after(200,AlienB.Affichage)
    # AlienB.Mouvement()
       

#Mouvement du vaisseau
def MouvementVaisseau(event):
    global Peut_Tirer
    touche=event.keysym
    if touche=='Left':
        vaisseau.deplacement(-1)
    elif touche=='Right':
        vaisseau.deplacement(1)
    elif touche=='space':
        if Peut_Tirer:
            global FileTir
            ff.Ajouter(FileTir,tirVaisseau(vaisseau.x,vaisseau.y))
            FileTir[tirVaisseau.Compteur-1].Deplacement()
            Peut_Tirer=False
            Mafenetre.after(1000, Reload)
            

     
    
class Alien_Bonus :
    def __init__(self) : 
       self.vivant = True
       self.x = posX
       self.y = hauteur_ligne
       self.dir = 1
       self.vitesse = VitesseAlien * 2
       self.apparence = canevas.create_image(self.x,self.y, image = ImageVaisseau)
       


    def Affichage(self):
        canevas.coords(self.apparence,self.x,self.y)
         
        
    def Mouvement(self):
        if self.x + largeur_alien>=largeur and self.dir == 1 : 
            self.dir = -1
        elif self.x-largeur_alien<=0 and self.dir == -1 :
            self.dir = 1
        self.x += self.vitesse * self.dir
        self.Affichage()
        Mafenetre.after(5,self.Mouvement)

#Création du widget bouton "Lancement d'une partie"
buttonStart = Button (Mafenetre, text="START", fg = "blue", command=NouvellePartie)
buttonStart.grid(row=0,column=1)

#Contrôle du vaisseau
canevas = Canvas(Mafenetre, width = largeur, height = hauteur, bg = 'black')
canevas.grid(row=2,column=1,columnspan=2)
canevas.grid_remove()
canevas.focus_set()
canevas.bind('<Key>',MouvementVaisseau)

#Lancement du gestionnaire d'événements
Mafenetre.mainloop()