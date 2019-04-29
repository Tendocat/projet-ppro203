import pygame
from pygame.locals import *

pygame.init()

#Ouverture de la fenetre Pygame
fenetre = pygame.display.set_mode((640, 480))

#Chargement et collage du fond
fond = pygame.image.load("background.jpg").convert()
fenetre.blit(fond, (0,0))

#Chargement et collage du personnage
perso = pygame.image.load("perso.png").convert()#convert_alpha() pour transparence 
perso.set_colorkey((255,255,255)) #Rend le blanc (valeur RGB : 255,255,255) de l'image transparent

fenetre.blit(perso, (200,300))#colle perso sur fenetre

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

#cours complet :
#https://openclassrooms.com/fr/courses/1399541-interface-graphique-pygame-pour-python/
#KEY_ENVENT
#https://openclassrooms.com/fr/courses/1399541-interface-graphique-pygame-pour-python/1399995-gestion-des-evenements-1#/id/r-1400784
#MOUSE_EVENT
#https://openclassrooms.com/fr/courses/1399541-interface-graphique-pygame-pour-python/1399995-gestion-des-evenements-1#/id/r-1399994
#WINDOWS_EVENT
#https://openclassrooms.com/fr/courses/1399541-interface-graphique-pygame-pour-python/1400488-gestion-des-evenements-2#/id/r-1400487