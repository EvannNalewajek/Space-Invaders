# -*- coding: utf-8 -*-
"""
Created on Mon Jan 10 10:35:43 2022

@author: mathi
"""
from tkinter import Tk, Label, Button, Canvas, PhotoImage
from Lib_Alien import *
from Lib_Vaisseau import *


#Création de la fenêtre graphique
Mafenetre = Tk()
Mafenetre.title('Space Invaders')

#Création du widget bouton quitter
buttonQuitt = Button (Mafenetre, text="QUITTER", fg = 'red', command = Mafenetre.destroy)
buttonQuitt.grid(row=0,column=2)

#Canevas
hauteurC = 480
largeurC = 640

#Affichage du score
score = Label(Mafenetre,text='Score: 0')
score.grid(row = 1,column=1)

#Affichage de la vie
NbrVies=Label(Mafenetre,text="Vies: 3")
NbrVies.grid(row=1,column=2)

#Importation des images
ImageFond=PhotoImage(file='space.gif')


#nbr d'ennemis
nbre_alien = 15






def NouvellePartie():
    global vaisseau,ennemie,Vies
    canevas.grid()
    canevas.create_image(0,0,image=ImageFond)
    buttonStart.grid_remove()
    vaisseau = Spaceship(canevas, Mafenetre)
    
    ennemie=[]
    for i in range(nbre_alien):
        ennemie.append(Alien(canevas, Mafenetre))
    for i in ennemie:
        i.Creation()
    ennemie[0].MouvementAlien(ennemie)
    Talien = TirAlien(0,ennemie,canevas,Mafenetre)
    Talien.Tir_Alien()
    Talien.Deplacement()
    #vaisseau.Reload()
   




#Création du widget bouton "Lancement d'une partie"
buttonStart = Button (Mafenetre, text="START", fg = "blue", command = NouvellePartie)
buttonStart.grid(row=0,column=1)

#Contrôle du vaisseau
canevas = Canvas(Mafenetre, width = largeurC, height = hauteurC, bg = 'black')
canevas.grid(row=2,column=1,columnspan=2)
canevas.grid_remove()
canevas.focus_set()
canevas.bind('<Key>',Spaceship.MouvementVaisseau)

#Lancement du gestionnaire d'événements
Mafenetre.mainloop()