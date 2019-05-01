import pygame
from pygame.locals import *

#load les images des tuiles
def chargement_images():
	tuiles = []
	for k in range(1, 10):#cercles de 0 - 8
		t = pygame.image.load("pics/"+(str)(k)+".png").convert_alpha()
		tuiles.append(t)
	for k in range(1, 10):#caracteres de 9 - 17
		t = pygame.image.load("pics/a"+(str)(k)+".png").convert_alpha()
		tuiles.append(t)
	for k in range(1, 10):#bambous de 18 - 26
		t = pygame.image.load("pics/b"+(str)(k)+".png").convert_alpha()
		tuiles.append(t)
	for k in range(1, 4):#dragons 27 - 29
		t = pygame.image.load("pics/d"+(str)(k)+".png").convert_alpha()
		tuiles.append(t)
	for k in range(1, 5):#vents 30 - 33
		t = pygame.image.load("pics/v"+(str)(k)+".png").convert_alpha()
		tuiles.append(t)
	return tuiles
	
#return genere un tableau avec lignes = [[image0, (x, y)],...,[imageN, (xN, y)]] en lisant un fichier contenant les chiffres des images
#param tuiles : le tableau contenant les images precharges
#param L, H la largeur et hauteur d'une tuile
def generation_tab_fichier(tuile, nom_fichier = 'tableau'):
	tableau = []
	with open(nom_fichier, 'r') as fichier:
		for y in range(HEIGHT, HEIGHT*10, HEIGHT):
			ligne = fichier.readline()
			col = 0
			t = []
			for x in range(WIDTH, WIDTH*10, WIDTH):
				if col < len(ligne):
					if ligne[col] == '1':
						t.append([tuile[0], (x,y)])
					elif ligne[col] == '2':
						t.append([tuile[1], (x,y)])
					elif ligne[col] == '3':
						t.append([tuile[2], (x,y)])
					elif ligne[col] == '4':
						t.append([tuile[3], (x,y)])
					elif ligne[col] == '5':
						t.append([tuile[4], (x,y)])
					elif ligne[col] == '6':
						t.append([tuile[5], (x,y)])
					elif ligne[col] == '7':
						t.append([tuile[6], (x,y)])
					elif ligne[col] == '8':
						t.append([tuile[7], (x,y)])
					elif ligne[col] == '9':
						t.append([tuile[8], (x,y)])
					elif ligne[col] == 'a':
						col += 1
						if ligne[col] == '1':
							t.append([tuile[9], (x,y)])
						elif ligne[col] == '2':
							t.append([tuile[10], (x,y)])
						elif ligne[col] == '3':
							t.append([tuile[11], (x,y)])
						elif ligne[col] == '4':
							t.append([tuile[12], (x,y)])
						elif ligne[col] == '5':
							t.append([tuile[13], (x,y)])
						elif ligne[col] == '6':
							t.append([tuile[14], (x,y)])
						elif ligne[col] == '7':
							t.append([tuile[15], (x,y)])
						elif ligne[col] == '8':
							t.append([tuile[16], (x,y)])
						elif ligne[col] == '9':
							t.append([tuile[17], (x,y)])
					elif ligne[col] == 'b':
						col += 1
						if ligne[col] == '1':
							t.append([tuile[18], (x,y)])
						elif ligne[col] == '2':
							t.append([tuile[19], (x,y)])
						elif ligne[col] == '3':
							t.append([tuile[20], (x,y)])
						elif ligne[col] == '4':
							t.append([tuile[21], (x,y)])
						elif ligne[col] == '5':
							t.append([tuile[22], (x,y)])
						elif ligne[col] == '6':
							t.append([tuile[23], (x,y)])
						elif ligne[col] == '7':
							t.append([tuile[24], (x,y)])
						elif ligne[col] == '8':
							t.append([tuile[25], (x,y)])
						elif ligne[col] == '9':
							t.append([tuile[26], (x,y)])
					elif ligne[col] == 'd':
						col+=1
						if ligne[col] == '1':
							t.append([tuile[27], (x,y)])
						if ligne[col] == '2':
							t.append([tuile[28], (x,y)])
						if ligne[col] == '3':
							t.append([tuile[29], (x,y)])
					elif ligne[col] == 'v':
						col+=1
						if ligne[col] == '1':
							t.append([tuile[30], (x,y)])
						if ligne[col] == '2':
							t.append([tuile[31], (x,y)])
						if ligne[col] == '3':
							t.append([tuile[32], (x,y)])
						if ligne[col] == '4':
							t.append([tuile[33], (x,y)])
							
					col += 1
			tableau.append(t)
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
def tuile_position(p):
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

#test si deux tuiles à deux positions différentes sont égales et les suppriment si c'est le cas
#@param deux positions à comparer
#return true si tuiles égales/ on peut ajouter les familles ici
def egal(a, b):
	bool = 0
	if a == b:
		bool = 0
	else:
		for y in range(len(tableau)):
			for x in range(len(tableau[y])):
				if tableau[y][x][1] == a:
					a = tableau[y][x]
					y1 = y
				if tableau[y][x][1] == b:
					b = tableau[y][x]
					y2 = y
		if a[0] == b[0]:
			bool = 1
			tableau[y1].remove(a)
			tableau[y2].remove(b)
	return bool

pygame.init()
fenetre = pygame.display.set_mode((630, 480))#Ouverture de la fenetre Pygame
fond = pygame.Surface(fenetre.get_size()).convert()#creation du fond a la taille de la fenetre
fond.fill((100,100,200))#couleur du fond

#Chargement du tableau ([[tuile, (x,y)]]
tuile = chargement_images()
(WIDTH, HEIGHT) = tuile[0].get_size()#setup des constantes de la largeur et hauteur des tuiles en fonction des images

tableau = generation_tab_fichier(tuile)
refresh(tableau)

#initialisation de l'animation de selection
select = (-1, -1)
select_surface = pygame.Surface((WIDTH, HEIGHT))
select_surface.fill((255,255, 0))

#Boucle infinie
continuer = 1
while continuer:
	for event in pygame.event.get():   #On parcours la liste de tous les événements reçus
		if event.type == QUIT:     #Si un de ces événements est de type QUIT
			continuer = 0      #On arrête la boucle
		if event.type == MOUSEBUTTONDOWN:	#Si un est de type click de souris
			if event.button == 1:
				if tuile_position(event.pos) == 0 or select == tuile_position(event.pos):
					refresh(tableau)
					select = (-1, -1)
				elif(select == (-1, -1)):
					select = tuile_position(event.pos)
					fenetre.blit(select_surface, select)
					pygame.display.flip()
				elif egal(select, tuile_position(event.pos)): #remove tuile et score up
					#test si chaque ligne est vide
					continuer = 0
					for tab in tableau:
						if tab:
							continuer = 1
					if continuer == 0: #afficher l'écran de démarrage ou gameover ici
						tableau = generation_tab_fichier(tuile)
						select = (-1, -1)
						continuer = 1
					refresh(tableau)
				else :
					select = tuile_position(event.pos)
					refresh(tableau)
					fenetre.blit(select_surface, select)
					pygame.display.flip() #Rafraichissement









print('EXIT')

