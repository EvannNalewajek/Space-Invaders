#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 14:08:38 2021

@author: evann.nalewajek
"""


"""
Fait par : Nalewajek Evann / Nenach Mathis
Fait le : 13/12/21
Objectif : Création de l'interface graphique
"""
from tkinter import Tk, Label, Button, Canvas
import Invaders_classe
import random, math



#Création de la fenêtre graphique
Mafenetre=Tk()
Mafenetre.title('Space Invaders')

#Définition des dimensions de la fenêtre
Mafenetre.geometry('1000x700+400+200')

#Creation d'un widget Canvas
Larg = 800
Haut = 600

Canevas = Canvas(Mafenetre, width = Larg, height = Haut, bg = 'white')
Canevas.pack(padx = 5, pady = 5)

#Position de l'alien
PosAX = Larg/2
PosAY = Haut/2
#Dimension de L'alien
Largeur = 100
Hauteur = 50
#Déplacement de l'alien
vitesse = 5
Dx = vitesse * math.cos(0)
#Création d'un alien
New_Alien = Invaders_classe.Alien(PosAX, PosAY, Largeur/2, Hauteur/2, Dx, Mafenetre, Canevas)

New_Alien.deplacement()


#Création du vaisseau
PosX = Larg/2
PosY = Haut-10
Dx2 = 5
Vaisseau = Invaders_classe.Vaisseau(PosX, PosY, 50, 25, Dx2 ,Mafenetre , Canevas)


#Déplacement du vaisseau
Canevas.bind('<Key>', Vaisseau.deplacement)


#Création du widget SCORE
score = Label(Mafenetre, text = "Score :")
#Positionnement du widget
score.pack()

#Création du widget bouton quitter
buttonQuitt = Button (Mafenetre, text="QUITTER", fg = 'red', command = Mafenetre.destroy)
#Positionnement du widget
buttonQuitt.pack()

#Création du widget bouton "Lancement d'une partie"
buttonStart = Button (Mafenetre, text="START", fg = "blue")
buttonStart.pack()

#Lancement du gestionnaire d'événements
Mafenetre.mainloop()