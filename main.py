import pygame
from pygame.locals import *

pygame.init()

fenetre = pygame.display.set_mode((400, 600))


fond = pygame.sprite.Sprite()
pygame.sprite.Sprite.__init__(fond)
fond.image = pygame.image.load("Ground.jpg").convert()
fond.image = pygame.transform.scale(fond.image, (1000, 600))
fond.rect = fond.image.get_rect()
fond.rect.x = 0
fond.rect.y = 0
liste_des_sprites = pygame.sprite.LayeredUpdates()
liste_des_sprites.add(fond)



continuer = True

while continuer:
    liste_des_sprites.draw(fenetre)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == QUIT:
            continuer = False

pygame.quit()


