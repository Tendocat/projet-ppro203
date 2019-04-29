import pygame
from pygame.locals import *

def chargement_images():
	tuiles = []
	for k in range(4):
		print(k)
		tuile = pygame.image.load(f"{k}.png").convert()#convert_alpha() pour transparence 
		#tuile.set_colorkey((255,255,255)) #Rend le blanc (valeur RGB : 255,255,255) de l'image transparent
		tuiles.append(tuile)

	return tuiles

pygame.init()

#Ouverture de la fenetre Pygame
fenetre = pygame.display.set_mode((640, 480))

#Chargement des images de tuiles (tuile = [[pic0][pic1]]
tuile = chargement_images()

#Rafraichissement de l'ecran
pygame.display.flip()

continuer = 1

#Boucle infinie
while continuer:
	for event in pygame.event.get():   #On parcours la liste de tous les événements reçus
		if event.type == QUIT:     #Si un de ces événements est de type QUIT
			continuer = 0      #On arrête la boucle
		if event.type == KEYDOWN:
			if event.key == K_SPACE:
				print("Espace")
			if event.key == K_RETURN:
				print("Entrée")
	#Re-collage
	#fenetre.blit(fond, (0,0))
	fenetre.blit(tuile[0], (0, 0))#def generer tableau(): for k in range(len(tuile)): tuile[k].append((x,y)) // bien (x,y) avec parenthèses
	#Rafraichissement
	pygame.display.flip()
	

#cours complet :
#https://openclassrooms.com/fr/courses/1399541-interface-graphique-pygame-pour-python/
#KEY_ENVENT
#https://openclassrooms.com/fr/courses/1399541-interface-graphique-pygame-pour-python/1399995-gestion-des-evenements-1#/id/r-1400784
#MOUSE_EVENT
#https://openclassrooms.com/fr/courses/1399541-interface-graphique-pygame-pour-python/1399995-gestion-des-evenements-1#/id/r-1399994
#WINDOWS_EVENT
#https://openclassrooms.com/fr/courses/1399541-interface-graphique-pygame-pour-python/1400488-gestion-des-evenements-2#/id/r-1400487