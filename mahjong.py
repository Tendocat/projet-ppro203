import pygame, sys
from pygame.locals import *
import time




WINDOWWIDTH  = 630
WINDOWHEIGHT = 480
BGCOLOR      = (100,100,200)
RED          = (255,   0,   0)
WHITE        = (255, 255, 255)
BLACK        = (  0,   0,   0)

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
	
#return génère un tableau avec lignes = [[image0, (x, y)],...,[imageN, (xN, y)]] en lisant un fichier contenant les chiffres des images
#param tuiles : le tableau contenant les images prechargées
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
	
#refresh initialiation affichage tuiles differe	
def refresh_initialiation(tableau):
	global nbPaire
	fenetre.blit(fond, (0,0))#ecrase tout avec le fond
	displayScore(nbPaire)
	displayMenuButton()
	for ligne in range(len(tableau)):
		for tuile in tableau[ligne]:
			for n in range (4):
				time.sleep(0.1)
				for event in pygame.event.get():
					if event.type == QUIT:
						pygame.quit()
						sys.exit()
			fenetre.blit(tuile[0], tuile[1])#0 = image; 1 = coordonnees
			pygame.display.flip() #Rafraichissement
	
#affiche le tableau du mahjong
def refresh(tableau):
	global nbPaire
	fenetre.blit(fond, (0,0))#ecrase tout avec le fond
	displayScore(nbPaire)
	displayMenuButton()
	for ligne in range(len(tableau)):
		for tuile in tableau[ligne]:
			fenetre.blit(tuile[0], tuile[1])#0 = image; 1 = coordonnees
	pygame.display.flip() #Rafraichissement
	

#test si la position est sur une tuile
#return la position (x, y) de la tuile selectionnée
def tuile_position(p, tableau):
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

	
def displayScore(nb):
    scoreSurf = DISPLAYFONT.render('Score: %d' % (nb), True, WHITE)
    scoreRect = scoreSurf.get_rect()
    scoreRect.topleft = (WINDOWWIDTH - 120, 10)
    fenetre.blit(scoreSurf, scoreRect)
	
def displayMenuButton():
	global menuRect
	global restartRect
	menuSurf = DISPLAYFONT.render('Menu', True, WHITE)
	menuRect = menuSurf.get_rect()
	menuRect.topleft = (WINDOWWIDTH - 120, 5*WINDOWHEIGHT/8)
	fenetre.blit(menuSurf, menuRect)
	restartSurf = DISPLAYFONT.render('Start Again', True, WHITE)
	restartRect = restartSurf.get_rect()
	restartRect.topleft = (WINDOWWIDTH - 120, 5*WINDOWHEIGHT/8+22)
	fenetre.blit(restartSurf, restartRect)
	
	
	
def displayStartmenu():
	global startmenu
	menu = 1
	mahjongSurf = pygame.font.Font('freesansbold.ttf', 100).render('MAHJONG', True, BGCOLOR)
	mahjongRect = mahjongSurf.get_rect()
	while menu :
		fenetre.fill(RED)
		mahjongRect.midtop = (WINDOWWIDTH/2 , WINDOWHEIGHT/3)
		fenetre.blit(mahjongSurf, mahjongRect)
		startSurf = DISPLAYFONT.render('Start', True, WHITE)
		startRect = startSurf.get_rect()
		startRect.topleft = (WINDOWWIDTH - 120, 7*WINDOWHEIGHT/8)
		fenetre.blit(startSurf, startRect)
		pygame.display.flip()
		for event in pygame.event.get():
			if event.type == KEYDOWN:
				if event.key == pygame.K_s:
					start()
				if event.key == pygame.K_m:
					startmenu = 0
					start()
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			if event.type == MOUSEBUTTONDOWN:
				if event.button == 1:
					if (startRect.collidepoint(event.pos)):
						start()
					

#test si deux tuiles à deux positions différentes sont égales et les suppriment si c'est le cas
#@param deux positions à comparer
#return true si tuiles égales/ on peut ajouter les familles ici
def egal(a, b, tableau):
	bool = 0
	global nbPaire
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
			nbPaire += 1
	return bool
	

def gameOverScreen(tmin, tsec, nbclick, nbPaire):
	timeSurf = DISPLAYFONT.render('Temps total : %d minutes et %d secondes.' % (tmin, tsec), True, WHITE)
	timeRect = timeSurf.get_rect()
	timeRect.topleft = (WINDOWWIDTH/5, WINDOWHEIGHT/3)
	fenetre.blit(timeSurf, timeRect)
	ttSurf = DISPLAYFONT.render('Temps par tuiles : %d' % (tsec/34), True, WHITE)
	ttRect = timeSurf.get_rect()
	ttRect.topleft = (WINDOWWIDTH/5, WINDOWHEIGHT/3+25)
	fenetre.blit(ttSurf, ttRect)
	nbcSurf = DISPLAYFONT.render('Nombre de clicks : %d' % (nbclick), True, WHITE)
	nbcRect = nbcSurf.get_rect()
	nbcRect.topleft = (WINDOWWIDTH/5, WINDOWHEIGHT/3+50)
	fenetre.blit(nbcSurf, nbcRect)
	nbciSurf = DISPLAYFONT.render('Nombre de clicks inutiles : %d' % (nbclick-34), True, WHITE)
	nbciRect = nbciSurf.get_rect()
	nbciRect.topleft = (WINDOWWIDTH/5, WINDOWHEIGHT/3+75)
	fenetre.blit(nbciSurf, nbciRect)
	pygame.display.flip()
	nbPaire=0


	
pygame.init()
pygame.display.set_caption('mahjong')
fenetre = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))#Ouverture de la fenetre Pygame
fond = pygame.Surface(fenetre.get_size()).convert()#creation du fond a la taille de la fenetre
fond.fill(BGCOLOR)#couleur du fond
DISPLAYFONT = pygame.font.Font('freesansbold.ttf', 18)

#Chargement des images
tuile = chargement_images()
(WIDTH, HEIGHT) = tuile[0].get_size()#setup des constantes de la largeur et hauteur des tuiles en fonction des images
select_surface = pygame.image.load("pics/0.png").convert_alpha()

#Boucle infinie
startmenu = 0
debut = time.time() #Temps de début de la partie
nbclick = 0
nbPaire = 0

firsttime=1


menuRect = 0
restartRect = 0

def start():
	commencer = 1
	global startmenu
	global nbclick
	global nbPaire
	global menuRect
	global restartRect
	nbPaire = 0
	while True:
		if startmenu==0 :
			startmenu = 1
			displayStartmenu()
		if commencer:
			tableau = generation_tab_fichier(tuile)
			refresh_initialiation(tableau)
			select = (-1, -1)
			commencer = 0
		for event in pygame.event.get():	#On parcours la liste de tous les événements reçus
			if event.type == QUIT:	#Si un de ces événements est de type QUIT
				print('EXIT')
				pygame.quit()
				sys.exit()	#On arrête la boucle
			if event.type == MOUSEBUTTONDOWN:	#Si un est de type click de souris
				if event.button == 1:
					if (menuRect.collidepoint(event.pos)):
						startmenu = 0
						time.sleep(0.2)
						start()
					elif (restartRect.collidepoint(event.pos)):
						start()
					elif tuile_position(event.pos, tableau) == 0 or select == tuile_position(event.pos, tableau):
						refresh(tableau)
						select = (-1, -1)
						nbclick += 1
					elif(select == (-1, -1)):
						select = tuile_position(event.pos, tableau)
						fenetre.blit(select_surface, select)
						pygame.display.flip()
					elif egal(select, tuile_position(event.pos, tableau), tableau): #remove tuile et score up
						#test si chaque ligne est vide
						over = 1
						for tab in tableau:
							if tab:
								over = 0
						if over :
							refresh(tableau)
							fin = time.time() #Temps de fin de la partie
							ttotal = fin-debut #Temps total de la partie en secondes
							tsec = ttotal
							tmin = 0 #Temps en minutes
							while tsec>60:
								tmin +=1
								tsec -= 60
							while True:
								gameOverScreen(tmin, tsec, nbclick, nbPaire)
								for event in pygame.event.get():
									if event.type == KEYDOWN:
										if event.key == pygame.K_s:
											start()
										if event.key == pygame.K_m:
											startmenu = 0
											start()
									if event.type == QUIT:
										pygame.quit()
										sys.exit()
									if event.type == MOUSEBUTTONDOWN:
										if event.button == 1:
											print('s')
											start()
							
						refresh(tableau)
					else :
						select = tuile_position(event.pos, tableau)
						refresh(tableau)
						fenetre.blit(select_surface, select)
						pygame.display.flip()
			if event.type == KEYDOWN:
				if event.key == pygame.K_s:
					start()
				if event.key == pygame.K_m:
					startmenu = 0
					start()

	print('EXIT')
if firsttime:
	firsttime = 0
	start()
	