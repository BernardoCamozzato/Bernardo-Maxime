import pygame
from pygame.examples.sprite_texture import sprite
from pygame.locals import *

pygame.init()
class Obstacle(pygame.sprite.Sprite):
    def __init__(self,x,y, point_de_vie):
        super().__init__()
        self.point_de_vie= point_de_vie
        self.position_x= x
        self.position_y=y

    def casser(self, point_de_vie):
        self.point_de_vie=point_de_vie
        if self.point_de_vie<=0:
            sprite.kill()

class Bonus(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()



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

personage_1 = pygame.sprite.Sprite()
pygame.sprite.Sprite.__init__(personage_1)
personage_1.image = pygame.image.load("Personage_1.png").convert_alpha()
personage_1.rect = personage_1.image.get_rect()
personage_1.rect.centerx = fenetre.get_rect().centerx
personage_1.rect.centery = 500
liste_des_sprites.add(personage_1)





continuer = True

while continuer:
    liste_des_sprites.draw(fenetre)
    pygame.display.flip()
    pygame.key.set_repeat(10, 50)
    for event in pygame.event.get():
        if event.type == QUIT:
            continuer = False
        if event.type == KEYDOWN:
            if event.key == K_UP :
                personage_1.rect = personage_1.rect.move(0,-10)
            if event.key == K_DOWN:
                personage_1.rect = personage_1.rect.move(0,10)
            if event.key == K_LEFT :
                personage_1.rect = personage_1.rect.move(-10,0)
            if event.key == K_RIGHT :
                personage_1.rect = personage_1.rect.move(10,0)





pygame.quit()
