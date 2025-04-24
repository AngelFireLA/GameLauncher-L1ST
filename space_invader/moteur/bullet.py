import pygame

class Bullet:
    def __init__(self, x, y, speed=10):
        self.width = 16
        self.height = 32
        self.image = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        self.image.fill((255, 255, 0))
        self.x = x
        self.y = y
        self.speed = speed
        self.active = True

    def update(self):
        self.y -= self.speed
        if self.y < 0:
            self.active = False

    def draw(self, screen):
        if self.active:
            screen.blit(self.image, (self.x, self.y))
