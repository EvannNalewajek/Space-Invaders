# Space-Invaders

1) Fonctionnement du Jeu :

	- Boutons de Commande : Cliquer sur "Start" pour commencer, "Quitter" pour supprimer, "Restart" pour relancer une partie

	- Contrôle du vaisseau : Le vaiseau se déplace de gauche à droite grâce aux touches "Left" et "Right" du clavier,
				 la barre Espace permet de tirer (limité à 1 tir par seconde).

	- Fonctionnement du vaisseau : Possède 3 points de vie. Il perd 1 point de vie lorsqu'il se fait toucher par un tir alien,
				       en plus de clignoter pour indiquer que le vaiseau s'est fait toucher.
				       La partie est terminé lorsque ses points de vie tombent à 0.

	- Fonctionnement des aliens : Limités à 15 aliens sur une ligne, ils se déplacent d'abord vers la gauche. Une fois le bord atteint
				      par le dernier alien, la ligne descend d'un cran puis se déplace vers la droite. Les aliens tirent
				      aléatoirement toutes les 0.5 millisecondes.

	- Fonctionnement de l'alien bonus : Apparaît au bout de 7.5 secondes. Il navigue de gauche à droite sans descendre, en allant
					    2 fois plus vite que les aliens ordinaire. Il donne 150 points s'il est touché.

	- Fonctionnement des protections : Possèdent 5 points de vie. Si un alien tire sur une protection, celui-ci perd un point de vie.
					   Si c'est un tir provenant du vaisseau, le tir ne touche pas le vaisseau et passe à travers.
					   La protection disparaît si ses points de vie tombent à 0.

	- Fonctionnement du score : Si un alien est éliminé, le score augmente de 25 points.
				    Si l'alien bonus est éliminé, le score augmente de 150 points.
				    Le score ne se remet pas à 0 au lancement d'une nouvelle partie.

	- Fonctionnement des booléens : Il y a 2 booléens dans le code : Peut_Tirer et Partie_en_Cours.
					Ils permettent de bloquer certaines fonctions tournant en arrière-plan s'ils sont sur False.
					Tant que Partie_en_Cours est sur True, toutes les fonctions concernant le déplacement des
					éléments dans le canvas tournent.
					Lorsque le vaisseau tire, Peut_Tirer se met sur False, empêchant le vaisseau de tirer à nouveau.
					Au bout d'une seconde, Peut_Tirer se remet sur True, le vaisseau peut à nouveau tirer.

	- Fonctionnement des compteurs : L'utilisation des compteurs dans certaines classes permet de faciliter la navigation dans les
					 listes. C'est le cas pour les classes Alien, Protection et Tirvaisseau qui sont toutes
					 utilisées dans des listes.

	- Les dimensions des objets sont faites pour s'adapter à l'image. Les images ont été récupérées sur internet, grâce à un
	  utilisateur qui a lui-même codé un space invader sur Python (Seul les images ont été récupéré). L'apparence de l'alien
	  bonus est similaire à celui du vaisseau.



2) Intégration de la liste, la file et la pile :

	- La liste est utilisé pour les aliens et les protections. Elle permet de les aligner sur une ligne, et l'alien touché (ou la
	  la protection détruite) est retiré(e) de la liste, peut importe sa position.

	- La file est utilisé pour les tirs. Le premier tir est celui qui va disparaître en premier, d'où l'utilisation de la file.
	  Le temps de rechargement des tirs du vaisseau est pensé pour éviter des conflits dans les situations où le deuxième tir
	  touche un alien, alors que le premier n'a pas réussi (dans tous les cas, le premier tir disparaîtra avant que le deuxième
	  tir ne touche quoi que ce soit).

	- La pile n'est pas implémentée. Nous avons pensé à l'utiliser pour les protections. Une protection aurait donc dû être
	  divisée en plusieurs piles de carré. Le dernier carré étant tout en haut, c'est lui qui sera détruit en premier si
	  un alien le touche. Pour les tirs alliés, Nous avons pensé à inverser la pile, pour éliminer le carré tout en bas.
	  Cela n'a pas été fait par manque de temps.



3) Eléments à rajouter :

	- Utiliser un fichier pour chaque classe. Nous avons essayé, mais la tentative s'est soldée par un échec. Les fichiers ont
	  besoin de communiquer entre eux, mais nous n'avons pas réussi à leur faire reconnaître les variables.

	- Ajouter une sécurité pour les variables des classes (self.__x au lieu de self.x, et vaisseau._Spaceship__.x
	  au lieu de vaisseau.x). Là aussi, nous avons essayé, mais cela a rendu certains éléments illisibles pour certaines
	  fonctions.

	- Limiter l'utilisation du global. Il s'agit d'une mauvaise habitude. Mais son utilisation était parfois nécessaire car
	  nous n'avons pas trouvé de meilleurs solutions.

	- Plusieurs lignes d'aliens : Notre réflexion s'est tournée vers une matrice (liste de listes), mais cela aurait doublé les
	  lignes de code. Par manque de temps, la recherche de cet élément pas nécessaire n'a pas été approfondie.

	- Changer l'apparence des objets, notamment de l'alien bonus. Cela ne s'est pas fait car la convertion du format PNG au
	  format GIF supprime la transparence de l'image.

	- Affichage du meilleur score dans le menu.



4) Bugs :

	- Il est possible de tirer sur l'alien bonus alors que celui-ci n'est pas encore apparu. Cela s'explique par le fait qu'au
	  lancement d'une partie, l'alien bonus est créé dans le canvas, mais en étant invisible.