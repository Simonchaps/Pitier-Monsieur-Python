import pygame
from pygame.locals import *
pygame.init()
from random import *
pygame.mixer.init()


# Ouvrir une fenêtre Pygame
taille = largeur, hauteur = 716, 656
fenetre = pygame.display.set_mode(taille)

pygame.display.set_caption("Pitié monsieur") # Nommer la fenêtre
menu= pygame.image.load("Frame 1.jpg").convert()

son = pygame.mixer.Sound("son/musique.wav") #Charger la musique de fond
son.play(loops=-1, maxtime=0, fade_ms=0)#Lire la musique de fond en boucle

continuer=1
continuer2=1
progression=1

while continuer==1 :
    fenetre.blit(menu, (0,0))
    while continuer2==1:
        for event in pygame.event.get() :

            #Fermeture
            if event.type == QUIT :
                continuer2=0
                continuer=0
            
            
        pygame.display.flip()

pygame.quit()