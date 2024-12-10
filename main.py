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
    degat = 1
    pdv = 1
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

class personnage (pygame.sprite.Sprite):
    def __init__(self,liste_des_sprites, x,y, image, points_de_vie):
        super().__init__()
        self.image = pygame.image.load(image).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y =  y
        liste_des_sprites.add(self)
        self.pdv = points_de_vie
    def perdre_pdv(self):
        self.pdv-=1
        if self.pdv <= 0 :
            self.kill()
            liste_des_sprites.remove(self)
            self.rect.x = 1000000000


personage_1 = personnage(liste_des_sprites, 220, 475, "Personage_1.png",10)
personage_2 = personnage(liste_des_sprites,230,20,"image-removebg-preview .png",10)


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
                nouveau_missile = Missile(personage_1.rect.x + 10, personage_1.rect.y -5, -7)
                missiles_J1.append(nouveau_missile)
                liste_des_sprites.add(nouveau_missile)
            if event.key == K_y:
                nouveau_missile = Missile(personage_2.rect.x + 10, personage_2.rect.y + 65, 7)
                missiles_J2.append(nouveau_missile)
                liste_des_sprites.add(nouveau_missile)
    for missile in missiles_J1:
        missile.update()
        if missile.rect.colliderect(personage_2):
            personage_2.perdre_pdv()
            missiles_J1.remove(missile)
            liste_des_sprites.remove(missile)
            missile.kill()
    for missile in missiles_J2:
        missile.update()
        if missile.rect.colliderect(personage_1):
            personage_1.perdre_pdv()
            missiles_J2.remove(missile)
            liste_des_sprites.remove(missile)
            missile.kill()
        for autre_missile in missiles_J1 :
            if missile.rect.colliderect(autre_missile) :
                missiles_J2.remove(missile)
                liste_des_sprites.remove(missile)
                missile.kill()
                missiles_J1.remove(autre_missile)
                liste_des_sprites.remove(autre_missile)
                autre_missile.kill()

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

