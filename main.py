import pygame
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





class Missile(pygame.sprite.Sprite):
    def __init__(self, x, y, speed):
       super().__init__()
       self.image = pygame.image.load("diddy.png").convert_alpha()
       self.image = pygame.transform.scale(self.image,[20,30])
       self.rect = self.image.get_rect()
       self.rect.x = x
       self.rect.y = y
       self.speed = speed
    def update(self):
       self.rect.y += self.speed
       if self.rect.bottom < 0:
           self.kill()
       if self.rect.top < 0:
           self.kill()


fenetre = pygame.display.set_mode((500, 600))

clock = pygame.time.Clock()


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

personage_2 = pygame.sprite.Sprite()
pygame.sprite.Sprite.__init__(personage_2)
personage_2.image = pygame.image.load("image-removebg-preview .png").convert_alpha()
personage_2.rect = personage_2.image.get_rect()
personage_2.rect.centerx = fenetre.get_rect().centerx
personage_2.rect.centery = 100
liste_des_sprites.add(personage_2)



continuer = True
missiles_J1 = []
missiles_J2 = []
while continuer:
    clock.tick(100)
    liste_des_sprites.draw(fenetre)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == QUIT:
            continuer = False
        if event.type == KEYDOWN:
            if event.key == K_l:
                nouveau_missile = Missile(personage_1.rect.x + 10, personage_1.rect.y -5, -5)
                missiles_J1.append(nouveau_missile)
                liste_des_sprites.add(nouveau_missile)
            if event.key == K_y:
                nouveau_missile = Missile(personage_2.rect.x + 10, personage_2.rect.y + 65, 4)
                missiles_J2.append(nouveau_missile)
                liste_des_sprites.add(nouveau_missile)
    for missile in missiles_J1:
        missile.update()
        if missile.rect.colliderect(personage_2):
            print("col")
            missiles_J1.remove(missile)
            liste_des_sprites.remove(missile)
            missile.kill()
    for missile in missiles_J2:
        missile.update()
        if missile.rect.colliderect(personage_1):
            print("col")
            missiles_J2.remove(missile)
            liste_des_sprites.remove(missile)
            missile.kill()

    keys = pygame.key.get_pressed()
    if keys [K_s]:
        personage_2.rect.y += 2.3
    if keys [K_w]:
        personage_2.rect.y += -2.3
    if keys [K_d]:
        personage_2.rect.x += 2.3
    if keys [K_a]:
        personage_2.rect.x += -2.3
    if keys [K_DOWN]:
        personage_1.rect.y += 2.3
    if keys [K_UP]:
        personage_1.rect.y += -2.3
    if keys [K_RIGHT]:
        personage_1.rect.x += 2.3
    if keys [K_LEFT]:
        personage_1.rect.x += -2.3


pygame.quit()

