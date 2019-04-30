import pygame
from pygame.locals import *

#load les images des tuiles
def chargement_images():
	tuiles = []
	for k in range(10):
		print(k)
		t = pygame.image.load(f"{k}.png").convert()
		tuiles.append(t)
	return tuiles
	
#return genere un tableau avec lignes = [[image0, (x, y)],...,[imageN, (xN, y]] en lisant un fichier contenant les chiffres des images
#param tuiles : le tableau contenant les images precharges
#param L, H la largeur et hauteur d'une tuile
def generation_tab_fichier(tuile):
	tableau = []
	fichier = open('tableau', 'r')
	for y in range(60, 420, HEIGHT):
		ligne = fichier.readline()
		col = 0
		t = []
		for x in range(30, 600, WIDTH):
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
	
#affiche le tableau du mahjong
def refresh(tableau):
	fenetre.blit(fond, (0,0))#ecrase tout avec le fond
	for ligne in range(len(tableau)):
		for tuile in tableau[ligne]:
			fenetre.blit(tuile[0], tuile[1])#0 = image; 1 = coordonnees
	pygame.display.flip() #Rafraichissement

#test si la position est sur une tuile
#return la position (x, y) de la tuile selectionnee
def test(x, y):
	selection = 0
	for bout in tableau:
		if len(bout) > 0:
			(a, b) = bout[0][1]
			if x > a and y > b and x < a + WIDTH  and y < b + HEIGHT:
				selection = bout[0]
			else:
				(a, b) = bout[len(bout)-1][1]
				if x > a and y > b and x < a + WIDTH  and y < b + HEIGHT:
					selection = bout[len(bout)-1][1]
	return selection
	
pygame.init()
fenetre = pygame.display.set_mode((630, 480))#Ouverture de la fenetre Pygame
fond = pygame.Surface(fenetre.get_size()).convert()#creation du fond a la taille de la fenetre
fond.fill((100,100,200))#couleur du fond

#Chargement du tableau ([[tuile, (x,y)]]
tuile = chargement_images()
(WIDTH, HEIGHT) = tuile[0].get_size()#setup des constantes de la largeur et hauteur des tuiles
WIDTH , HEIGHT = 30, 60#tant que images pas bonnes
tableau = generation_tab_fichier(tuile)
refresh(tableau)

print (test(125,70))


print (tableau[0][0][0].get_size())

#Boucle infinie
continuer = 1
while continuer:
	for event in pygame.event.get():   #On parcours la liste de tous les événements reçus
		if event.type == QUIT:     #Si un de ces événements est de type QUIT
			continuer = 0      #On arrête la boucle
		if event.type == KEYDOWN:#c'est plutot mouse qu'on veut, mais ça peut servir
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