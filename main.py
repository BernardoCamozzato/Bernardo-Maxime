import pygame
from pygame.examples.grid import WINDOW_WIDTH, WINDOW_HEIGHT
from pygame.locals import *


def render_multi_line(text, x, y, fsize):
    police = pygame.font.Font(None, 25)  # Taille de la police: 36, None signifie la police par défaut
    lines = text.splitlines()
    for i, l in enumerate(lines):
        fenetre.blit(police.render(l, 0, (206,206,206), ), (x, y + fsize * i))

def afficher_game_over(fenetre, gagnant):
    fenetre.fill((0, 0, 0))  # Fond noir
    police = pygame.font.Font(None, 50)
    texte = f"Game Over! {gagnant} gagne!"
    text_surface = police.render(texte, True, (255, 0, 0))
    text_rect = text_surface.get_rect(center=(250, 300))
    fenetre.blit(text_surface, text_rect)
    pygame.display.flip()
    pygame.time.wait(3000)  # Pause de 3 secondes avant de quitter
    pygame.quit()
    exit()



pygame.init()
class Obstacle(pygame.sprite.Sprite):
    def __init__(self,x,y,image,point_de_vie):
        super().__init__()
        self.image = pygame.image.load(image).convert_alpha()
        self.image = pygame.transform.scale_by(self.image, 0.15)
        self.rect = self.image.get_rect()
        self.point_de_vie= point_de_vie
        self.rect.x=x
        self.rect.y=y
        liste_des_sprites.add(self)

    def casser(self):
        self.point_de_vie-=1
        if self.point_de_vie<=0:
            self.kill()
            self.rect.x = 1000000000

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
obstacle_1 = Obstacle(130,360,"barril.png",6)
obstacle_2 = Obstacle(370,190,"barril.png",7)
obstacle_3 = Obstacle(60,150,"pierre.png",10)
obstacle_4 = Obstacle(255,260,"pierre_2.png",15)

continuer = True
missiles_J1 = []
missiles_J2 = []
while continuer:
    clock.tick(100)
    liste_des_sprites.draw(fenetre)
    render_multi_line("Joueur 1\nW\nASD\n R pour tirer", 10, 10, 25)
    render_multi_line("Joueur 2\n flèches directionelles\n L pour tirer", 300, 20, 25)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == QUIT:
            continuer = False
        if event.type == KEYDOWN:
            if event.key == K_l:
                nouveau_missile = Missile(personage_1.rect.x + 10, personage_1.rect.y -5, -7)
                missiles_J1.append(nouveau_missile)
                liste_des_sprites.add(nouveau_missile)
            if event.key == K_r:
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

        if missile.rect.colliderect(obstacle_1):
            obstacle_1.casser()
            missiles_J1.remove(missile)
            liste_des_sprites.remove(missile)
            missile.kill()
        if missile.rect.colliderect(obstacle_2):
            obstacle_2.casser()
            missiles_J1.remove(missile)
            liste_des_sprites.remove(missile)
            missile.kill()
        if missile.rect.colliderect(obstacle_3):
            obstacle_3.casser()
            missiles_J1.remove(missile)
            liste_des_sprites.remove(missile)
            missile.kill()
        if missile.rect.colliderect(obstacle_4):
            obstacle_4.casser()
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

        if missile.rect.colliderect(obstacle_1):
            obstacle_1.casser()
            missiles_J2.remove(missile)
            liste_des_sprites.remove(missile)
            missile.kill()
        if missile.rect.colliderect(obstacle_2):
            obstacle_2.casser()
            missiles_J2.remove(missile)
            liste_des_sprites.remove(missile)
            missile.kill()
        if missile.rect.colliderect(obstacle_3):
            obstacle_3.casser()
            missiles_J2.remove(missile)
            liste_des_sprites.remove(missile)
            missile.kill()
        if missile.rect.colliderect(obstacle_4):
            obstacle_4.casser()
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
    # Vérification du Game Over
    if personage_1.pdv <= 0:
        afficher_game_over(fenetre, "Joueur 2")
    elif personage_2.pdv <= 0:
        afficher_game_over(fenetre, "Joueur 1")

    keys = pygame.key.get_pressed()

    rect_perso2 = personage_2.rect.copy()
    rect_perso2.y += 5

    if keys [K_s] and not rect_perso2.colliderect(obstacle_1) and not rect_perso2.colliderect(obstacle_2) and not rect_perso2.colliderect(obstacle_3) and not rect_perso2.colliderect(obstacle_4):
        personage_2.rect.y += 2.3

    rect_perso2 = personage_2.rect.copy()
    rect_perso2.y -= 5

    if keys [K_w] and not rect_perso2.colliderect(obstacle_1)and not rect_perso2.colliderect(obstacle_2) and not rect_perso2.colliderect(obstacle_3) and not rect_perso2.colliderect(obstacle_4):
        personage_2.rect.y += -2.3

    rect_perso2 = personage_2.rect.copy()
    rect_perso2.x += 5
    if keys [K_d] and not rect_perso2.colliderect(obstacle_1)and not rect_perso2.colliderect(obstacle_2) and not rect_perso2.colliderect(obstacle_3) and not rect_perso2.colliderect(obstacle_4):
        personage_2.rect.x += 2.3

    rect_perso2 = personage_2.rect.copy()
    rect_perso2.x -= 5
    if keys [K_a] and not rect_perso2.colliderect(obstacle_1)and not rect_perso2.colliderect(obstacle_2) and not rect_perso2.colliderect(obstacle_3) and not rect_perso2.colliderect(obstacle_4):
        personage_2.rect.x += -2.3

    rect_perso1 = personage_1.rect.copy()
    rect_perso1.y += 5

    if keys [K_DOWN] and not rect_perso1.colliderect(obstacle_1)and not rect_perso1.colliderect(obstacle_2) and not rect_perso1.colliderect(obstacle_3) and not rect_perso1.colliderect(obstacle_4):
        personage_1.rect.y += 2.3

    rect_perso1 = personage_1.rect.copy()
    rect_perso1.y -= 5
    if keys [K_UP]  and not rect_perso1.colliderect(obstacle_1)and not rect_perso1.colliderect(obstacle_2) and not rect_perso1.colliderect(obstacle_3) and not rect_perso1.colliderect(obstacle_4):
        personage_1.rect.y += -2.3

    rect_perso1 = personage_1.rect.copy()
    rect_perso1.x += 5
    if keys [K_RIGHT]  and not rect_perso1.colliderect(obstacle_1)and not rect_perso1.colliderect(obstacle_2) and not rect_perso1.colliderect(obstacle_3) and not rect_perso1.colliderect(obstacle_4):
        personage_1.rect.x += 2.3

    rect_perso1 = personage_1.rect.copy()
    rect_perso1.x -= 5
    if keys [K_LEFT]  and not rect_perso1.colliderect(obstacle_1)and not rect_perso1.colliderect(obstacle_2) and not rect_perso1.colliderect(obstacle_3) and not rect_perso1.colliderect(obstacle_4):
        personage_1.rect.x += -2.3





pygame.quit()
