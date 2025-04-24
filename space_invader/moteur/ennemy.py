import pygame
import os
from ..utils import chemin_absolu_dossier

class Enemy:
    def __init__(self, x, y, speed=2, size=64):
        raw_img = pygame.image.load(chemin_absolu_dossier+"assets/images/ennemy.png").convert_alpha()
        self.image = pygame.transform.scale(raw_img, (size, size))
        self.x = x
        self.y = y
        self.speed = speed
        self.active = True
        self.size = size

    def update(self):
        self.y += self.speed
        if self.y > 768:
            self.active = False

    def draw(self, screen):
        if self.active:
            screen.blit(self.image, (self.x, self.y))
