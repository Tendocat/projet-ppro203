import pygame
from pygame.locals import *

#load les images des tuiles
def chargement_images():
	tuiles = []
	for k in range(10):
		t = pygame.image.load(f"{k}.png").convert()#si arrondis faut prendre de l'exemple pour le transparent
		tuiles.append(t)
	return tuiles
	
#return genere un tableau avec lignes = [[image0, (x, y)],...,[imageN, (xN, y]] en lisant un fichier contenant les chiffres des images
#param tuiles : le tableau contenant les images precharges
#param L, H la largeur et hauteur d'une tuile
def generation_tab_fichier(tuile):
	tableau = []
	fichier = open('tableau', 'r')
	for y in range(HEIGHT, HEIGHT*10, HEIGHT):
		ligne = fichier.readline()
		col = 0
		t = []
		for x in range(WIDTH, WIDTH*10, WIDTH):
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
def test(p):
	(x, y) = p
	selection = 0
	for bout in tableau:
		if len(bout) > 0:
			(a, b) = bout[0][1]
			if x > a and y > b and x < a + WIDTH  and y < b + HEIGHT:
				selection = bout[0][1]
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
(WIDTH, HEIGHT) = tuile[0].get_size()#setup des constantes de la largeur et hauteur des tuiles en fonction des images
WIDTH , HEIGHT = 30, 50#tant que images pas bonnes
tableau = generation_tab_fichier(tuile)
refresh(tableau)

#initialisation de l'animation de selection
select = (-1, -1)
select_surface = pygame.Surface((WIDTH, HEIGHT))
select_surface.fill((0,100,200))

print (tableau[0][0][0].get_size())

#Boucle infinie
continuer = 1
while continuer:
	for event in pygame.event.get():   #On parcours la liste de tous les événements reçus
		if event.type == QUIT:     #Si un de ces événements est de type QUIT
			continuer = 0      #On arrête la boucle
		if event.type == MOUSEBUTTONDOWN:	#Si un est de type click de souris
			if event.button == 1:
				if test(event.pos) == 0 or select == test(event.pos):
					refresh(tableau)
					select = (-1, -1)
				elif(select == (-1, -1)):
					select = test(event.pos)
					print(select)
					fenetre.blit(select_surface, select)
					pygame.display.flip()
				#elif egal(select, event.pos): #remove tuile et score up et check si il en reste comme on cherche les valeurs dans egal, on pourrait tout faire dans egal
				#	pass #ça sert à écrire des if vides pour les tests
					
				else :
					select = test(event.pos)
					print(select)
					refresh(tableau)
					fenetre.blit(select_surface, select)
					pygame.display.flip() #Rafraichissement









print('EXIT')

