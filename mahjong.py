import pygame, sys
from pygame.locals import *
import time
from random import *



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

def random_tableau_fichier(ligne = 8, colonne = 6, nom_fichier = 'levels/random.txt'):
	f = open(nom_fichier,'w')
	tableau = []
	
	for c in range(0,(int)(colonne)):
		tableau.append([0]*ligne)
		
	
	for c in range(0,(int)(colonne)):
		for l in range(0,ligne):
			if tableau[c][l] == 0:
				type = randint(0,4)
				if type == 0:
					ajouter = (str)(randint(1,9))
				elif type == 1:
					ajouter = 'a' + (str)(randint(1,9))
				elif type == 2:
					ajouter = 'b' + (str)(randint(1,9))
				elif type == 3:
					ajouter = 'd' + (str)(randint(1,3))
				elif type == 4:
					ajouter = 'v' + (str)(randint(1,4))
				tableau[c][l] = ajouter
				
				a = 0
				while  a != 1:
					cc = randint(0,colonne-1)
					b = randint(0,1)
					if b == 0:
						ll = l
					elif b == 1:
						ll = ligne-1-l
				
					if tableau[cc][ll] == 0:
						tableau[cc][ll] = ajouter
						a = 1
	
	for c in range(0,(int)(colonne)):
		for l in range(0,ligne):
			f.write((str)(tableau[c][l]))
		f.write('\n')
		
	f.close()

def creer_level(level = 0):
	if level == 0:
		random_tableau_fichier(4,3,"levels/0.txt")
	elif level == 1:
		random_tableau_fichier(5,4,"levels/1.txt")
	elif level == 2:
		random_tableau_fichier(6,4,"levels/2.txt")
	elif level == 3:
		random_tableau_fichier(6,5,"levels/3.txt")
	elif level == 4:
		random_tableau_fichier(8,5,"levels/4.txt")
	elif level == 5:
		random_tableau_fichier(7,6,"levels/5.txt")
	elif level == 6:
		random_tableau_fichier(9,6,"levels/6.txt")
	elif level == 7:
		random_tableau_fichier(8,7,"levels/7.txt")
	elif level == 8:
		random_tableau_fichier(10,7,"levels/8.txt")
	elif level == 9:
		random_tableau_fichier(10,8,"levels/9.txt")

#return génère un tableau avec lignes = [[image0, (x, y)],...,[imageN, (xN, y)]] en lisant un fichier contenant les chiffres des images
#param tuiles : le tableau contenant les images prechargées
#param L, H la largeur et hauteur d'une tuile
def generation_tab_fichier(tuile, nom_fichier = 'levels/0', edit = False):
	global global_tableau_nb_cases
	global_tableau_nb_cases = 0
	tableau = []
	if not edit:
		nom_fichier = 'levels/' + (str)(nom_fichier) + '.txt'
	else :
		nom_fichier = 'levels/edit' + (str)(nom_fichier) + '.txt'
	with open(nom_fichier, 'r') as fichier:
		for y in range(HEIGHT, HEIGHT*9, HEIGHT):
			ligne = fichier.readline()
			col = 0
			t = []
			for x in range(WIDTH, WIDTH*11, WIDTH):
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
					else:
						global_tableau_nb_cases-=1
					global_tableau_nb_cases+=1
					col += 1
			tableau.append(t)
	if global_tableau_nb_cases == 0:
		global_tableau_nb_cases = 1
	return tableau

#refresh initialiation affichage tuiles differe	
def refresh_initialiation(tableau, level, nbPaire, startmenu, edit):
	fenetre.blit(fond, (0,0))#ecrase tout avec le fond
	displayScore(nbPaire, level)
	b = displayMenuButton()
	pygame.display.flip() #Rafraichissement
	for ligne in range(len(tableau)):
		for tuile in tableau[ligne]:
			for n in range (2):
				time.sleep(0.1)
				eventInGame(startmenu, level, b[0], b[1], edit)
			fenetre.blit(tuile[0], tuile[1])#0 = image; 1 = coordonnees
			pygame.display.flip() #Rafraichissement
	
#affiche le tableau du mahjong
def refresh(tableau, level, nbPaire):
	fenetre.blit(fond, (0,0))#ecrase tout avec le fond
	displayScore(nbPaire, level)
	b = displayMenuButton()
	for ligne in range(len(tableau)):
		for tuile in tableau[ligne]:
			fenetre.blit(tuile[0], tuile[1])#0 = image; 1 = coordonnees
	pygame.display.flip() #Rafraichissement
	return b
	

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

	
def displayScore(nb, level):
	global global_tableau_nb_cases
	score = buttonmj('{}%'.format((int)(nb*2*100/global_tableau_nb_cases)), WINDOWWIDTH - 120, 35)
	clvl  = buttonmj('Level %d' %(level), WINDOWWIDTH - 120, 10)
	
	
def displayMenuButton():
	buttonsGame =  [0]*2
	menu        =  buttonmj('Menu', WINDOWWIDTH - 120, 5*WINDOWHEIGHT/8)
	restart     =  buttonmj('Start Again', WINDOWWIDTH - 120, 5*WINDOWHEIGHT/8+22)
	buttonsGame[0]=menu[1]
	buttonsGame[1]=restart[1]
	return buttonsGame
	
def buttonmj(content, width, height):
	a = [0]*2
	a[0] = DISPLAYFONT.render(content, True, WHITE)
	a[1] = a[0].get_rect()
	a[1].topleft = (width, height)
	fenetre.blit(a[0], a[1])
	return a
	
def displayStartmenu():
	menu = 1
	diff = 0
	maxilvl = 9
	diffedit = 0
	maxilvledit = 100
	mahjongSurf = pygame.font.Font('freesansbold.ttf', 100).render('MAHJONG', True, BGCOLOR)
	mahjongRect = mahjongSurf.get_rect()
	fenetre.fill(RED)
	mahjongRect.midtop = (WINDOWWIDTH/2 , WINDOWHEIGHT/3)
	fenetre.blit(mahjongSurf, mahjongRect)
	
	
	startu      = buttonmj('Start random', WINDOWWIDTH - 145 , 7*WINDOWHEIGHT/8-44)
	cd          = buttonmj('Choose level', WINDOWWIDTH - 145 , 7*WINDOWHEIGHT/8-22)
	cdminus     = buttonmj('-', WINDOWWIDTH - 155+25, 7*WINDOWHEIGHT/8)
	cddis       = buttonmj('%d     '%(diff), WINDOWWIDTH - 155+65, 7*WINDOWHEIGHT/8)	
	cdplus      = buttonmj('+', WINDOWWIDTH - 155+105, 7*WINDOWHEIGHT/8)
	startedit   = buttonmj('Start edit level', WINDOWWIDTH - 145, 7*WINDOWHEIGHT/8-44-88)
	cdedit      = buttonmj('Choose edit level', WINDOWWIDTH - 155, 7*WINDOWHEIGHT/8-22-88)
	cdminusedit = buttonmj('-', WINDOWWIDTH - 155 + 25, 7*WINDOWHEIGHT/8-88)
	cddisedit   = buttonmj('%d     '%(diffedit), WINDOWWIDTH - 155 + 55, 7*WINDOWHEIGHT/8-88)
	cdplusedit  = buttonmj('+', WINDOWWIDTH - 155 + 105, 7*WINDOWHEIGHT/8-88)
	edit        = buttonmj('Level Editor', WINDOWWIDTH - 155 +12, 7*WINDOWHEIGHT/8+22)
	
	pygame.display.flip()
	while menu :
		for event in pygame.event.get():
			if event.type == KEYDOWN:
				if event.key == pygame.K_s:
					start(diff)
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			if event.type == MOUSEBUTTONDOWN:
				if event.button == 1:
					if (startu[1].collidepoint(event.pos)):
						start(diff)
					elif (cdminus[1].collidepoint(event.pos)):
						cddis[0].fill(RED)
						fenetre.blit(cddis[0], cddis[1])
						if (diff==0):
							diff = maxilvl
						else :
							diff-=1
						cddis[0] = DISPLAYFONT.render('%d' % (diff), True, WHITE)
						fenetre.blit(cddis[0], cddis[1])
						pygame.display.update(cddis[1])
					elif (cdplus[1].collidepoint(event.pos)):
						cddis[0].fill(RED)
						fenetre.blit(cddis[0], cddis[1])
						if (diff<maxilvl):
							diff+=1
						else:
							diff = 0
						cddis[0] = DISPLAYFONT.render('%d' % (diff), True, WHITE)
						fenetre.blit(cddis[0], cddis[1])
						pygame.display.update(cddis[1])
					elif (edit[1].collidepoint(event.pos)):
						levelEditor()
					
					
					elif (startedit[1].collidepoint(event.pos)):
						c = 0
						try:
							f = open("levels/edit%d.txt" %(diffedit),"r")
							f.close()
							c = 1
						except FileNotFoundError:
							pass
						if c:
							start(diffedit, True)
						
					elif (cdminusedit[1].collidepoint(event.pos)):
						cddisedit[0].fill(RED)
						fenetre.blit(cddisedit[0], cddisedit[1])
						if (diffedit==0):
							diffedit = maxilvledit
						else :
							diffedit-=1
						c = 0
						try:
							f = open("levels/edit%d.txt" %(diffedit),"r")
							f.close()
							c = 1
						except FileNotFoundError:
							pass
						if c:
							cddisedit[0] = DISPLAYFONT.render('%d' % (diffedit), True, WHITE)
						else:
							cddisedit[0] = DISPLAYFONT.render('%d' % (diffedit), True, (100,100,100))
						fenetre.blit(cddisedit[0], cddisedit[1])
						pygame.display.update(cddisedit[1])
					elif (cdplusedit[1].collidepoint(event.pos)):
						cddisedit[0].fill(RED)
						fenetre.blit(cddisedit[0], cddisedit[1])
						if (diffedit<maxilvledit):
							diffedit+=1
						else:
							diffedit = 0
						c = 0
						try:
							f = open("levels/edit%d.txt" %(diffedit),"r")
							f.close()
							c = 1
						except FileNotFoundError:
							pass
						if c:
							cddisedit[0] = DISPLAYFONT.render('%d' % (diffedit), True, WHITE)
						else:
							cddisedit[0] = DISPLAYFONT.render('%d' % (diffedit), True, (100,100,100))
						fenetre.blit(cddisedit[0], cddisedit[1])
						pygame.display.update(cddisedit[1])

	
def levelEditor():
	level     = 0
	maxlvl    = 100
	line      = 8
	f         = 0
	cinactive = pygame.Color('lemonchiffon')
	cactive   = pygame.Color('firebrick')
	color     = []
	inputbox  = []
	text      = []
	active    = []
	txt_surface =[]
	fenetre.fill(BLACK)
	pygame.display.flip()
	
	textSurf = pygame.font.Font('freesansbold.ttf', 500).render('::', True, WHITE)
	textSurf.fill(BLACK)
	textRect = textSurf.get_rect()
	textRect.topleft = (4*WINDOWWIDTH/20 -50 , WINDOWHEIGHT/7)
	fenetre.blit(textSurf, textRect)
	
	
	for k in range (line):
		inputbox.append(pygame.Rect(100, 100+ k*24, 140, 22))
		text.append('')
		active.append(False)
		color.append(cinactive)
		txt_surface.append(k)
		
	pygame.display.update(textRect)
	
	nam     =  buttonmj('Choose level', WINDOWWIDTH - 170, 4*WINDOWHEIGHT/8)
	nmp     =  buttonmj('+', WINDOWWIDTH - 40, 4*WINDOWHEIGHT/8-22)
	nm      =  buttonmj('%d     ' % (level), WINDOWWIDTH - 45, 4*WINDOWHEIGHT/8)
	nmm     =  buttonmj('-', WINDOWWIDTH - 38, 4*WINDOWHEIGHT/8+22)
	ed      =  buttonmj('Edit', WINDOWWIDTH - 105, 7*WINDOWHEIGHT/8-44)
	cancel  =  buttonmj('Cancel', WINDOWWIDTH - 105, 7*WINDOWHEIGHT/8-22)
	sav     =  buttonmj('Save', WINDOWWIDTH - 105, 7*WINDOWHEIGHT/8)

	
	fenetre.blit(textSurf, textRect)
	pygame.display.update(textRect)
	for k in range (line):
		txt_surface[k] = DISPLAYFONT.render(text[k], True, color[k])
		width = max(200, txt_surface[k].get_width()+10)
		inputbox[k].w = width
		fenetre.blit(txt_surface[k], (inputbox[k].x+5, inputbox[k].y+5))
		pygame.draw.rect(fenetre, color[k], inputbox[k], 2)
		pygame.display.update(inputbox[k])
	pygame.display.flip()
	#fenetre.blit(mahjongSurf, mahjongRect)
	while True :
		for event in pygame.event.get():
			if event.type == KEYDOWN:
				for k in range (line):
					if active[k]:
						if event.key == pygame.K_BACKSPACE:
							text[k] = (text[k])[:-1]
						else:
							text[k] += event.unicode
					
				fenetre.blit(textSurf, textRect)
				pygame.display.update(textRect)
				for k in range (line):
					txt_surface[k] = DISPLAYFONT.render(text[k], True, color[k])
					width = max(200, txt_surface[k].get_width()+10)
					inputbox[k].w = width
					fenetre.blit(txt_surface[k], (inputbox[k].x+5, inputbox[k].y+5))
					pygame.draw.rect(fenetre, color[k], inputbox[k], 2)
					pygame.display.update(inputbox[k])		
			if event.type == MOUSEBUTTONDOWN:
				if event.button == 1:
					for k in range (line):
						if inputbox[k].collidepoint(event.pos):
							active[k] = True
						else:
							active[k] = False
						color[k] = cactive if active[k] else cinactive
					if (cancel[1].collidepoint(event.pos)):
						if (f!=0):
							u=f.name
							f.close()
							f = open(u,"w+")
							f.write(g)
							f.close()
						displayStartmenu()
					elif (sav[1].collidepoint(event.pos)):
						if f!=0:
							for i in range (line):
								f.write(text[i]+'\n')
								text[i] = ''
							f.close()
							f=0
					elif (ed[1].collidepoint(event.pos)):
						if (f!=0):
							f.close()
						try:
							g=''
							f = open("levels/edit%d.txt" %(level),"r")
							for i in range (line):
								text[i] = f.readline()
								g+=text[i]
							f.close()
						except FileNotFoundError:
							pass
						f = open("levels/edit%d.txt" %(level),"w+")
					elif (nmm[1].collidepoint(event.pos)):
						nm[0].fill(BLACK)
						fenetre.blit(nm[0], nm[1])
						if (level>0):
							level-=1
						else :
							level = maxlvl
						nm[0] = DISPLAYFONT.render('%d' % (level), True, WHITE)
						fenetre.blit(nm[0], nm[1])
						pygame.display.update(nm[1])
					elif (nmp[1].collidepoint(event.pos)):
						nm[0].fill(BLACK)
						fenetre.blit(nm[0], nm[1])
						if (level<maxlvl):
							level+=1
						else :
							level = 0
						nm[0] = DISPLAYFONT.render('%d' % (level), True, WHITE)
						fenetre.blit(nm[0], nm[1])
						pygame.display.update(nm[1])
				fenetre.blit(textSurf, textRect)
				pygame.display.update(textRect)
				for k in range (line):
					txt_surface[k] = DISPLAYFONT.render(text[k], True, color[k])
					width = max(200, txt_surface[k].get_width()+10)
					inputbox[k].w = width
					fenetre.blit(txt_surface[k], (inputbox[k].x+5, inputbox[k].y+5))
					pygame.draw.rect(fenetre, color[k], inputbox[k], 2)
					pygame.display.update(inputbox[k])
				
			if event.type == QUIT:
				pygame.quit()
				sys.exit()


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
	ttSurf = DISPLAYFONT.render('Temps par tuiles : %.3f' % ((tsec+tmin*60)/global_tableau_nb_cases), True, WHITE)
	ttRect = timeSurf.get_rect()
	ttRect.topleft = (WINDOWWIDTH/5, WINDOWHEIGHT/3+25)
	fenetre.blit(ttSurf, ttRect)
	nbcSurf = DISPLAYFONT.render('Nombre de clicks : %d' % (nbclick), True, WHITE)
	nbcRect = nbcSurf.get_rect()
	nbcRect.topleft = (WINDOWWIDTH/5, WINDOWHEIGHT/3+50)
	fenetre.blit(nbcSurf, nbcRect)
	nbciSurf = DISPLAYFONT.render('Nombre de clicks inutiles : %d' % (nbclick-nbPaire*2), True, WHITE)
	nbciRect = nbciSurf.get_rect()
	nbciRect.topleft = (WINDOWWIDTH/5, WINDOWHEIGHT/3+75)
	fenetre.blit(nbciSurf, nbciRect)
	pygame.display.flip()
	nbPaire=0

	
	
def start(level = 0, edit = False, again = False):
	if not again:
		creer_level(level)
	commencer = 1
	global startmenu
	global nbclick
	global nbPaire
	global menuRect
	global restartRect
	global global_tableau_nb_cases
	nbPaire = 0
	nbclick = 0
	debut = time.time() #Temps de début de la partie
	while True:
		if startmenu==0 :
			startmenu = 1
			displayStartmenu()
		if commencer:
			tableau = generation_tab_fichier(tuile, level, edit)
			if global_tableau_nb_cases == 1:
				displayStartmenu()
			refresh_initialiation(tableau, level, nbPaire, startmenu, edit)
			select = (-1, -1)
			commencer = 0
		for event in pygame.event.get():	#On parcours la liste de tous les événements reçus
			if event.type == QUIT:	#Si un de ces événements est de type QUIT
				print('EXIT')
				pygame.quit()
				sys.exit()	#On arrête la boucle
			if event.type == MOUSEBUTTONDOWN:	#Si un est de type click de souris
				if event.button == 1:
					nbclick += 1
					if (menuRect.collidepoint(event.pos)):
						startmenu = 0
						time.sleep(0.2)
						start(level)
					elif (restartRect.collidepoint(event.pos)):
						start(level, edit, True)
					elif tuile_position(event.pos, tableau) == 0 or select == tuile_position(event.pos, tableau):
						b = refresh(tableau, level, nbPaire)
						select = (-1, -1)
					elif(select == (-1, -1)):
						select = tuile_position(event.pos, tableau)
						fenetre.blit(select_surface, select)
						pygame.display.flip()
					elif egal(select, tuile_position(event.pos, tableau), tableau):
						#test si chaque ligne est vide
						over = 1
						for tab in tableau:
							if tab:
								over = 0
						if over :
							b = refresh(tableau, level, nbPaire)
							fin = time.time() #Temps de fin de la partie
							ttotal = fin-debut #Temps total de la partie en secondes
							tsec = ttotal
							tmin = 0 #Temps en minutes
							while tsec>60:
								tmin +=1
								tsec -= 60
							gameOverScreen(tmin, tsec, nbclick, nbPaire)
							nextlvl  = buttonmj('Next Level', WINDOWWIDTH - 120, 5*WINDOWHEIGHT/8+44)
							pygame.display.flip()
							while True:
								eventInGame(startmenu, level, b[0] , b[1], edit, nextlvl[1])
							
						b = refresh(tableau, level, nbPaire)
					else :
						select = tuile_position(event.pos, tableau)
						b = refresh(tableau, level, nbPaire)
						fenetre.blit(select_surface, select)
						pygame.display.flip()
			if event.type == KEYDOWN:
				if event.key == pygame.K_s:
					start(level)
				if event.key == pygame.K_m:
					startmenu = 0
					start(level)

	print('EXIT')
	
def eventInGame(startmenu, level, menuRect, restartRect, edit, nextlvlRect = 0):
	for event in pygame.event.get():
		if event.type == KEYDOWN:
			if event.key == pygame.K_s:
				start(level)
			if event.key == pygame.K_m:
				startmenu = 0
				start(level)
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		if event.type == MOUSEBUTTONDOWN:
			if (menuRect.collidepoint(event.pos)):
				displayStartmenu()
			elif (restartRect.collidepoint(event.pos)):
				start(level, edit, True)
			elif ((nextlvlRect !=0) and (nextlvlRect.collidepoint(event.pos))):
				if ((level+1)<10):
					start(level+1)
				else:
					start(level)
				


pygame.init()
pygame.display.set_caption('mahjong')
fenetre = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))#Ouverture de la fenetre Pygame
fond = pygame.Surface(fenetre.get_size()).convert()#creation du fond a la taille de la fenetre
fond.fill(BGCOLOR)#couleur du fond
DISPLAYFONT = pygame.font.Font('freesansbold.ttf', 18)

#Chargement des images
tuile = chargement_images()
(WIDTH, HEIGHT) = tuile[0].get_size()	#setup des constantes de la largeur et hauteur des tuiles en fonction des images
select_surface = pygame.image.load("pics/0.png").convert_alpha()

startmenu = 0

nbclick = 0
nbPaire = 0




menuRect = pygame.Rect(WINDOWWIDTH - 120,5*WINDOWHEIGHT/8,50,20)
restartRect = pygame.Rect(WINDOWWIDTH - 120,5*WINDOWHEIGHT/8+22,100,20)
if __name__ == '__main__':
	start()


	
