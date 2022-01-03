# -*- coding: utf-8 -*-
"""
Created on Sun Jan  2 17:03:43 2022

@author: evann
"""

from tkinter import Tk, Label, Button, Canvas, PhotoImage
import File_Fonctions as ff
import Pile_Fonctions as pf

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
largeur_alien=22      
hauteur_alien=16
ecart_alien=10
hauteur_ligne=50
nbre_alien=15
descente_alien=10
VitesseDeplacement=10
VitesseAlien=0.5

#Caractéristiques des tirs
vitesse_tir_vaisseau=2
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
        
        
class tirVaisseau:
    
    def __init__(self,X,Y):
        self.x=X
        self.y=Y
        self.apparence=canevas.create_line(self.x, self.y, self.x, self.y+5,fill='white')
        
    def Affichage(self):
        canevas.coords(self.apparence,self.x,self.y,self.x,self.y+5)
        
    def Fin(self):
        canevas.delete()



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
    
def MouvementTir():
    global Tir
    if ff.Est_vide(Tir)==False:
        for i in Tir:
            if i.y>-5:
                i.y-=vitesse_tir_vaisseau
            else:
                i.Fin()
                ff.Retirer(Tir)
            i.Affichage()
    Mafenetre.after(5,MouvementTir)

def NouvellePartie():
    global vaisseau,ennemie,Tir
    canevas.grid()
    canevas.create_image(0,0,image=ImageFond)
    buttonStart.grid_remove()
    vaisseau=Spaceship()
    ennemie=[]
    for i in range(nbre_alien):
        ennemie.append(Alien())
    for i in ennemie:
        i.Creation()
    MouvementAlien()
    Tir=[]
    MouvementTir()
    
def Reload():
    global Peut_Tirer
    Peut_Tirer=True
    return Peut_Tirer
        

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
            print(Peut_Tirer)
            global Tir
            ff.Ajouter(Tir,tirVaisseau(vaisseau.x,vaisseau.y))
            Peut_Tirer=False
        Mafenetre.after(1000,Reload)
                
        
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