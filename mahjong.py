import pygame
from pygame.locals import *

#load les images des tuiles
def chargement_images():
	tuiles = []
	for k in range(10):
		print(k)
		tuile = pygame.image.load(f"{k}.png").convert()#convert_alpha() pour transparence 
		#tuile.set_colorkey((255,255,255)) #Rend le blanc (valeur RGB : 255,255,255) de l'image transparent
		tuiles.append(tuile)
	return tuiles
	
#affiche le tableau du mahjong
def refresh(tableau):
	#Re-collage
	#fenetre.blit(fond, (0,0))
	for ligne in range(len(tableau)):
		for tuile in tableau[ligne]:
			fenetre.blit(tuile[0], tuile[1])#0 = image; 1 = coordonnees
	pygame.display.flip() #Rafraichissement
	
#return genere un tableau avec lignes = [[image0, (x, y)],...,[imageN, (xN, y]] en lisant un fichier contenant les chiffres des images
#param tuiles : le tableau contenant les images precharges
#param L, H la largeur et hauteur d'une tuile
def generation_tab_fichier(tuiles, L = 30, H = 60):
	tableau = []
	fichier = open('tableau', 'r')
	for y in range(60, 420, H):
		ligne = fichier.readline()
		col = 0
		t = []
		for x in range(30, 600, L):
			if col < len(ligne) :
				if ligne[col] == '0':
					t.append([tuile[0], (x,y)])
				elif ligne[col] == '1':
					t.append([tuile[1], (x,y)])
				elif ligne[col] == '2':
					t.append([tuile[2], (x,y)])
				elif ligne[col] == '3':
					t.append([tuile[3], (x,y)])
				elif ligne[col] == '4':
					t.append([tuile[4], (x,y)])
				elif ligne[col] == '5':
					t.append([tuile[5], (x,y)])
				elif ligne[col] == '6':
					t.append([tuile[6], (x,y)])
				elif ligne[col] == '7':
					t.append([tuile[7], (x,y)])
				col += 1
				print (col)
		tableau.append(t)
	fichier.close()
	print (tableau)
	if tableau[0][0][0] == tableau [1][3][0]:
		print ("\n\nOn peut comparer les refs de chaque image!!!!\n")
	return tableau
	
pygame.init()

#Ouverture de la fenetre Pygame
fenetre = pygame.display.set_mode((630, 480))

#Chargement du tableau ([[tuile, (x,y)]]
tuile = chargement_images()
tableau = generation_tab_fichier(tuile)

refresh(tableau)

#Boucle infinie
continuer = 1
while continuer:
	for event in pygame.event.get():   #On parcours la liste de tous les événements reçus
		if event.type == QUIT:     #Si un de ces événements est de type QUIT
			continuer = 0      #On arrête la boucle
		if event.type == KEYDOWN:
			if event.key == K_SPACE:
				print("Espace")
			if event.key == K_RETURN:
				print("Entrée")

	
	

#cours complet :
#https://openclassrooms.com/fr/courses/1399541-interface-graphique-pygame-pour-python/
#KEY_ENVENT
#https://openclassrooms.com/fr/courses/1399541-interface-graphique-pygame-pour-python/1399995-gestion-des-evenements-1#/id/r-1400784
#MOUSE_EVENT
#https://openclassrooms.com/fr/courses/1399541-interface-graphique-pygame-pour-python/1399995-gestion-des-evenements-1#/id/r-1399994
#WINDOWS_EVENT
#https://openclassrooms.com/fr/courses/1399541-interface-graphique-pygame-pour-python/1400488-gestion-des-evenements-2#/id/r-1400487