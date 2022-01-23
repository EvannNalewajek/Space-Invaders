# -*- coding: utf-8 -*-
"""
Created on Sun Jan  2 17:03:43 2022

Dernière modification faite le 23/01/2022

Fait par : NALEWAJEK Evann / NENACH Mathis
Groupe B

to-do liste (plus d'informations dans le README) :
             - Séparer les classes dans plusieurs fichiers
             - Utiliser des Piles pour les protections
             - Ajouter plusieurs lignes d'aliens
             - Difficulté croissance au fil des nouveaux (augmentation de la fréquence de tir)
             - Ajout de la collision entre le tir du vaisseau et la protection
             - Ajout de la sécurité pour les variables des classes (self.__x au lieu de self.x,
                                                                    et vaisseau._Spaceship__.x au lieu de vaisseau.x)
             - Ajout d'un affichage du meilleur score dans le menu
"""

# Importation des bibliothèques 
from tkinter import Tk, Label, Button, Canvas, PhotoImage, Menu
import File_Fonctions as ff
import Pile_Fonctions as pf
from random import randint

# Création de la fenêtre
Mafenetre=Tk()
Mafenetre.title('Space Invaders')

# Création du bouton Quitter
buttonQuitt = Button (Mafenetre, text="QUITTER", fg = 'red', command = Mafenetre.destroy)
buttonQuitt.grid(row=0,column=2)

# Dimensions du Canevas
hauteur=480
largeur=640

# Affichage du score
Score=0
scoreDisplay=Label(Mafenetre,text='Score : 0')
scoreDisplay.grid(row=1,column=1)

# Affichage de la vie
NbrVies=Label(Mafenetre,text="Vie : 3")
NbrVies.grid(row=1,column=2)

# Importation des images
ImageVaisseau = PhotoImage(file = 'spaceship.gif')
ImageDestroy = PhotoImage(file = 'spaceshipdestroy.gif')
ImageAlien = PhotoImage(file = 'invader.gif')
ImageFond = PhotoImage(file = 'space.gif')

# Caractéristiques du vaisseau
largeur_vaisseau = 30
hauteur_vaisseau = 32
posX = largeur/2
posY = hauteur - hauteur_vaisseau -5

# Caractéristiques des aliens
ennemie = []
largeur_alien = 22      
hauteur_alien = 16
ecart_alien = 10
hauteur_ligne = 50
nbre_alien = 15
descente_alien = 10
VitesseDeplacement = 10
VitesseAlien = 0.35

# Caractéristiques des protections
nbre_protections = 3
posY_protections = posY-55
largeur_protections = 50
hauteur_protections = 30
PdV_protections = 5

# Caractéristiques des tirs
FileTir = []
FileTirAlien = []
vitesse_tir = 1
Peut_Tirer = True

# Booléen permettant de bloquer des fonctions tant que la partie n'a pas commencé
Partie_en_Cours = False


# Création de la classe vaisseau (contrôlé par l'utilisateur), définie par sa position 
# dans le canvas et son apparence
class Spaceship :
    
    def __init__(self) :
        self.x = posX
        self.y = posY
        self.apparence = canevas.create_image(self.x, self.y, image = ImageVaisseau)


# Méthode qui permet au vaisseau de gérer les collisions avec le bord du canvas 
# s'il se dirigeait vers la gauche mais arrive au bord il ne peut que se déplacer vers la droite 
# de même pour la droite
    def deplacement(self,dir) :
        if Partie_en_Cours:
            if self.x >= largeur_vaisseau and dir ==-1:
                self.x += VitesseDeplacement * dir
            elif self.x <= largeur - largeur_vaisseau and dir == 1:
                self.x += VitesseDeplacement * dir
            self.Affichage()
            
            
# Méthode qui permet d'afficher le vaisseau sur le canvas aux positions qui lui sont attribués 
    def Affichage(self) :
        canevas.coords(self.apparence, self.x, self.y)
        
        
# Méthode purement esthétique qui permet d'indiquer si le vaisseau est touché par un tir ennemi       
    def Blesser(self) :
        self.Etat1()
        Mafenetre.after(100,self.Etat2)
        Mafenetre.after(200,self.Etat1)
        Mafenetre.after(300,self.Etat2)
        Mafenetre.after(400,self.Etat1)
        Mafenetre.after(500,self.Etat2)
        
# Etat du vaisseau blessé par un tir ennemi
    def Etat1(self) :
        canevas.itemconfig(self.apparence,image = ImageDestroy)
        
# Etat du vaisseau "retour a la normale" après avoir été touché      
    def Etat2(self):
        canevas.itemconfig(self.apparence,image = ImageVaisseau)
    


# Création de la classe Alien (ennemi du joueur) définie par sa position dans le canvas,
# son état (vivant ou pas), sa vitesse et un compteur du nombre d'alien
class Alien :
    
    Compteur = 0 
    def __init__(self) :
        Alien.Compteur += 1
        self.Compteur = Alien.Compteur
        self.vivant = True
        self.x = self.Compteur*(ecart_alien+largeur_alien)
        self.y = hauteur_ligne
        self.dir=1
        self.vitesse = VitesseAlien

# Méthode de création de l'alien dans le canvas    
    def Creation(self) :
        self.apparence = canevas.create_image(self.x, self.y, anchor='nw', image = ImageAlien)

# Méthode affichage de l'Alien selon sa position dans le canvas
    def Affichage(self) :
        canevas.coords(self.apparence,self.x,self.y)
  
# Méthode qui permet de détruire l'alien si son etat n'est pas "vivant", s'il n'y a plus d'ennemi
# dans la liste, on utilise la fonction fin de partie  
    def Destruction(self) : 
        if self.vivant == False : 
            canevas.delete(self.apparence)
        if ennemie == []:
            FinDePartie()
            

# Création de la classe Alien Bonus qui est un autre type d'ennemi définie comme les aliens
# mais qui rapporte plus de points et se déplace plus rapidement
class Alien_Bonus :
    def __init__(self) : 
       self.vivant = True
       self.x = posX
       self.y = hauteur_ligne
       self.dir = 1
       self.vitesse = VitesseAlien * 2

# Méthode qui permet d'afficher l'alien bonus dans le canvas selon sa position
    def Affichage(self) :
        canevas.coords(self.apparence, self.x, self.y)
 
#Méthode qui permet de créer l'alien bonus dans le canvas
    def Creation(self) :
        self.apparence = canevas.create_image(self.x, self.y, image = ImageVaisseau)
        Alien_Bonus.Mouvement(self)


# Méthode qui permet de déplacer l'alien automatiquement tant que la partie est en cours 
    def Mouvement(self) :
        if Partie_en_Cours:
            if self.x + largeur_alien >= largeur and self.dir == 1 : 
                self.dir = -1
            elif self.x-largeur_alien <=0 and self.dir == -1 :
                self.dir = 1
            self.x += self.vitesse * self.dir
            self.Affichage()
        Mafenetre.after(5,self.Mouvement)
 
# Création de la classe protections qui est défini par un rectangle avec un nombre de points 
# de vies 
class Protections :
    Compteur = 0
    def __init__(self) :
        Protections.Compteur += 1
        self.Compteur = Protections.Compteur
        self.x = largeur * self.Compteur / (nbre_protections + 1)
        Protections.y = posY_protections
        self.Resistance = PdV_protections
        self.Apparence = canevas.create_rectangle(self.x, self.y, self.x + largeur_protections,\
                                                  self.y + hauteur_protections,\
                                                width = 2, outline = 'black',fill = 'white')
        self.VieProtection = canevas.create_text(self.x + largeur_protections/2,\
                                                 self.y + hauteur_protections/2,\
                                                text = str(self.Resistance), fill = 'black')

            
# Méthode qui permet de retirer un point de vie à la protection si celle-ci est touché par un tir alien
    def Blesser(self) :
        self.Resistance -= 1
        if self.Resistance > 0:
            canevas.itemconfig(self.VieProtection,text = (str(self.Resistance)))
        else:
            self.Destruction()
 
# Méthode qui permet de supprimer la protection
    def Destruction(self) :
        canevas.delete(self.Apparence)
        canevas.delete(self.VieProtection)
        
# Création de la classe des tirs du vaisseau qui est défini par une ligne, 
# sa position, et de la condition de déplacement
class tirVaisseau :
    
    Compteur = 0
    def __init__(self,X,Y) :
        self.x = X
        self.y = Y
        self.mouvement = True
        self.apparence = canevas.create_line(self.x, self.y, self.x, self.y + 5, fill = 'white')
        tirVaisseau.Compteur += 1

# Méthode qui permet d'afficher le tir dans le canvas selon sa position        
    def Affichage(self) :
        canevas.coords(self.apparence, self.x, self.y, self.x, self.y + 5)

# Méthode qui permet aux tirs de se déplacer tant que la condition est respectée     
    def Deplacement(self) :
        if Partie_en_Cours:
            if self.mouvement:
                self.y -= vitesse_tir
                self.Affichage()
                self.Toucher()
                Mafenetre.after(5, self.Deplacement)

# Méthode qui permet de supprimer l'alien si le tir le touche, et actualise le score
    def Toucher(self) :
        global AB, Score
        if self.y < 0 :
            self.Fin()
            
        elif self.y >= AB.y - 5 and self.y <= AB.y + 5 and\
            self.x <= AB.x + largeur_vaisseau/2 and\
            self.x >= AB.x - largeur_vaisseau/2 :
                canevas.delete(AB.apparence)
                self.Fin()
                Score += 150
                ScoreMAJ()     
        
        else:
            for i in ennemie:
                if i.vivant and self.y >= i.y and self.y <= i.y + hauteur_alien and\
                    self.x <= i.x + largeur_alien and self.x >= i.x :
                    self.Fin()
                    i.vivant = False
                    ennemie.pop(ennemie.index(i))
                    i.Destruction()
                    Score += 25
                    ScoreMAJ()

# Méthode qui permet de retirer le tir de la file des tirs et de le retirer du canvas    
    def Fin(self) :
        self.mouvement = False
        canevas.delete(self.apparence)
        ff.Retirer(FileTir)
        tirVaisseau.Compteur -= 1


# Création de la classe Tir alien qui est définie par une ligne + sa position dans le canvas
class TirAlien:
    
    def __init__(self,i):
        self.x = ennemie[i].x
        self.y = ennemie[i].y
        self.apparence = canevas.create_line(self.x , self.y - 4 , self.x ,\
        self.y , fill = 'red')
        self.mouvement = True
        self.Deplacement()

# Méthode qui permet d'afficher le tir dans le canvas selon sa position        
    def Affichage(self):
        canevas.coords(self.apparence , self.x , self.y - 4 , self.x , self.y)

# Méthode qui permet au tir de se déplacer         
    def Deplacement(self):
        if Partie_en_Cours:
            if self.mouvement:
                self.y += vitesse_tir
                self.Affichage()
                self.Toucher()
                Mafenetre.after(5,self.Deplacement)

# Méthode qui retire le tir du canvas s'il a touché le vaisseau, une protection, ou rien.
# Retire un point de vie au vaisseau en cas de collision et si le nombre de vies du
# vaisseau tombe à 0, alors c'est la fin de la partie .   
    def Toucher(self):
        global Vies
        if self.y > hauteur:
            self.mouvement = False
            canevas.delete(self.apparence)
            ff.Retirer(FileTirAlien)
        elif self.y >= vaisseau.y - 5 and self.y <= vaisseau.y + 5 and\
            self.x <= vaisseau.x + largeur_vaisseau/2 and\
            self.x >= vaisseau.x - largeur_vaisseau/2 :
                self.mouvement = False
                canevas.delete(self.apparence)
                ff.Retirer(FileTirAlien)
                Vies -= 1
                vaisseau.Blesser()
                VieMAJ()
                if Vies == 0:
                    FinDePartie()
        else:
            for i in Murs:
                if i.Resistance > 0 and self.x >= i.x and\
                    self.x <= i.x + largeur_protections and\
                    self.y >= Protections.y and\
                    self.y <= Protections.y + hauteur_protections :
                    i.Blesser()
                    self.mouvement = False
                    canevas.delete(self.apparence)
                    ff.Retirer(FileTirAlien)



# Fonction qui permet aux aliens des se déplacer et de gérer les collisions avec le bord 
# du canvas, et s'ils rencontrent le bord alors ils descendent d'une ligne
def MouvementAlien():
        global ennemie, Partie_en_Cours
        if Partie_en_Cours:
            if (ennemie[-1].x + largeur_alien >= largeur and ennemie[-1].dir == 1) or\
                (ennemie[0].x - largeur_alien <= 0 and ennemie[0].dir == -1):
                for i in ennemie:
                    i.dir *= - 1
                    i.y += descente_alien
            for i in ennemie:
                i.x += i.vitesse*i.dir
                i.Affichage() 
        Mafenetre.after(5,MouvementAlien)
 
# Fonction qui permet aux aliens de tirer de manière aléatoire selon leur position dans la liste
def Tir_Alien() :
    global ennemie, FileTirAlien, Partie_en_Cours
    if Partie_en_Cours:
        L = [i.vivant for i in ennemie]
        i = randint(0, len(ennemie) - 1)
        if L[i] :
            ff.Ajouter(FileTirAlien,TirAlien(i))
            Mafenetre.after(500,Tir_Alien)
        else :
            Mafenetre.after(1,Tir_Alien)
    else : 
        Mafenetre.after(5, Tir_Alien)


# Fonction qui permet de jouer une partie, donc affiche les différents élements des classes
# et qui permet à l'utilisateur de jouer
def NouvellePartie() :
    global vaisseau, AB, ennemie, Vies, Score, Partie_en_Cours, Murs
    canevas.grid()
    canevas.create_image(0, 0, image = ImageFond)
    buttonStart.grid_remove()
    vaisseau = Spaceship()
    Protections.Compteur = 0
    Murs = [Protections() for i in range(nbre_protections)]
    Vies = 3
    for i in range(nbre_alien) :
        ennemie.append(Alien())
    for i in ennemie :
        i.Creation()
    AB = Alien_Bonus()
    Mafenetre.after(7500, AB.Creation)
    Partie_en_Cours = True
 
    
# Fonction qui fait "fin de partie" pour le joueur, donc qui retire tout les éléments 
# du canvas 
def FinDePartie() :
    global Partie_en_Cours, Perdu
    canevas.delete("all")
    canevas.grid_remove()
    Partie_en_Cours = False
    while not (ennemie == []) :
        ennemie.pop()
    while not (FileTir == []) :
        ff.Retirer(FileTir)
    while not (FileTirAlien == []) :
        ff.Retirer(FileTirAlien)
    buttonRejouer.grid()
    Perdu = Label(Mafenetre,text = "Game Over", fg = "red")
    Perdu.grid(row = 2,column = 1)

# Fonction qui permet de rejouer une partie en réinitialisant les valeurs  
def Rejouer() :
    global NbrVies, Score
    buttonRejouer.grid_remove()
    Perdu.destroy()
    Score = 0
    ScoreMAJ()
    Alien.Compteur = 0
    NbrVies.destroy()
    NbrVies = Label(Mafenetre,text="Vie : 3")
    NbrVies.grid(row = 1,column = 2)
    NouvellePartie()
    
 
# Fonction qui permet de recharger le tir du vaisseau
def Reload() :
    global Peut_Tirer
    Peut_Tirer = True
    return Peut_Tirer

    
# Fonction qui permet de mettre à jour l'affichage du nombre de vies    
def VieMAJ() :
    global Vies, NbrVies
    carac = "Vie : " + str(Vies)
    NbrVies.destroy()
    NbrVies = Label(Mafenetre,text = carac)
    NbrVies.grid(row = 1,column = 2)

# Fonction qui permet de mettre à jour l'affichage du score   
def ScoreMAJ() :
    global Score, scoreDisplay
    carac = "Score : " + str(Score)
    scoreDisplay.destroy()
    scoreDisplay = Label(Mafenetre,text = carac)
    scoreDisplay.grid(row = 1,column = 1)
    
     
    

# Fonction qui permet au vaisseau de se déplacer et de tirer selon les touches du clavier
# Après utilisation, le tir a une condition qui le bloque et a besoin de la fonction Reload
# pour que le vaisseau puisse de nouveau tirer
def MouvementVaisseau(event) :
    global Peut_Tirer
    touche = event.keysym
    if touche == 'Left' :
            vaisseau.deplacement(-1)
    elif touche == 'Right' :
            vaisseau.deplacement(1)
    elif touche == 'space' :
            if Peut_Tirer :
                global FileTir
                ff.Ajouter(FileTir, tirVaisseau(vaisseau.x, vaisseau.y))
                FileTir[tirVaisseau.Compteur - 1].Deplacement()
                Peut_Tirer = False
                Mafenetre.after(1000, Reload)
            

#Création du bouton "Lancement d'une partie"
buttonStart = Button (Mafenetre, text="START", fg = "blue", command = NouvellePartie)
buttonStart.grid(row = 0,column = 1)

#Création du bouton "Relancer une partie"
buttonRejouer = Button (Mafenetre, text = "REJOUER", fg = "blue", command = Rejouer)
buttonRejouer.grid(row = 0,column = 1)
buttonRejouer.grid_remove()

#création d'un menu
menubar = Menu(Mafenetre)
menuJeu = Menu(menubar, tearoff = 0)
menuJeu.add_command(label = "Retry" , command = Rejouer)
menuJeu.add_command(label = "Best Score" )
menubar.add_cascade(label = "Menu" , menu = menuJeu)

Mafenetre.config(menu = menubar)


#Contrôle du vaisseau
canevas = Canvas(Mafenetre, width = largeur, height = hauteur, bg = 'black')
canevas.grid(row=2,column=1,columnspan=2)
canevas.grid_remove()
canevas.focus_set()
canevas.bind('<Key>',MouvementVaisseau)

MouvementAlien()
Tir_Alien()
#Lancement du gestionnaire d'événements
Mafenetre.mainloop()