import pygame
import os
import random

from ..moteur.bullet import Bullet
from ..moteur.ennemy import Enemy
from ..utils import chemin_absolu_dossier

def check_collision(obj1, obj2):
    rect1 = obj1.image.get_rect(topleft=(obj1.x, obj1.y))
    rect2 = obj2.image.get_rect(topleft=(obj2.x, obj2.y))
    return rect1.colliderect(rect2)

class Player:
    def __init__(self, start_x=480, start_y=650, speed=10):
        raw_img = pygame.image.load(chemin_absolu_dossier+"assets/images/spaceship.png").convert_alpha()
        self.image = pygame.transform.scale(raw_img, (64, 64))
        self.x = start_x
        self.y = start_y
        self.speed = speed

    def move_left(self):
        self.x -= self.speed
        if self.x < 0:
            self.x = 0

    def move_right(self, max_width):
        if self.x > max_width - 64:
            self.x = max_width - 64
        else:
            self.x += self.speed

    def move_up(self):
        self.y -= self.speed
        if self.y < 0:
            self.y = 0

    def move_down(self, max_height):
        if self.y > max_height - 64:
            self.y = max_height - 64
        else:
            self.y += self.speed

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))


class Partie:
    def __init__(self, screen_width=1024, screen_height=768):
        self.screen_width = screen_width
        self.screen_height = screen_height

        self.player = Player(
            start_x=screen_width // 2 - 32,
            start_y=screen_height - 120
        )

        self.bullets = []
        self.enemies = []
        self.spawn_cooldown = 0
        self.score = 0
        self.lives = 3
        self.shooting_cooldown = 0

        self.wave = 1
        self.enemies_killed_in_wave = 0
        self.enemies_to_kill_this_wave = 10

        self.shoot_sound = pygame.mixer.Sound(chemin_absolu_dossier+"assets/shoot.wav")
        self.explosion_sound = pygame.mixer.Sound(chemin_absolu_dossier+"assets/explosion.wav")
        self.shoot_sound.set_volume(0.2)
        self.explosion_sound.set_volume(0.2)

        pygame.mixer.music.load(chemin_absolu_dossier+"assets/music.mp3")
        pygame.mixer.music.set_volume(0.05)
        pygame.mixer.music.play(-4)

    def spawn_enemy(self):
        enemy_speed = 2 + (self.wave - 1)
        enemy_size = 64
        x = random.randint(0, self.screen_width - enemy_size)
        y = random.randint(-150, -64)
        enemy = Enemy(x, y, speed=enemy_speed, size=enemy_size)
        self.enemies.append(enemy)

    def handle_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] or keys[pygame.K_q]:
            self.player.move_left()
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.player.move_right(self.screen_width)
        if keys[pygame.K_UP] or keys[pygame.K_z]:
            self.player.move_up()
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.player.move_down(self.screen_height)

        if keys[pygame.K_SPACE] and self.shooting_cooldown <= 0:
            bullet_x = self.player.x + 24
            bullet_y = self.player.y
            bullet = Bullet(bullet_x, bullet_y, speed=12)
            self.bullets.append(bullet)
            self.shoot_sound.play()
            self.shooting_cooldown = 15

    def update(self):
        if self.shooting_cooldown > 0:
            self.shooting_cooldown -= 1

        if self.spawn_cooldown <= 0:
            self.spawn_enemy()
            self.spawn_cooldown = 40
        else:
            self.spawn_cooldown -= 1

        for bullet in self.bullets:
            bullet.update()
        self.bullets = [b for b in self.bullets if b.active]

        for enemy in self.enemies:
            enemy.update()
            if enemy.active and enemy.y > (self.screen_height - 64):
                enemy.active = False
                self.lives -= 1

        self.enemies = [e for e in self.enemies if e.active]

        for bullet in self.bullets:
            for enemy in self.enemies:
                if bullet.active and enemy.active and check_collision(bullet, enemy):
                    bullet.active = False
                    enemy.active = False
                    self.score += 1
                    self.enemies_killed_in_wave += 1
                    self.explosion_sound.play()

        if self.enemies_killed_in_wave >= self.enemies_to_kill_this_wave:
            self.wave += 1
            self.enemies_killed_in_wave = 0
            self.enemies_to_kill_this_wave += 5
            self.spawn_cooldown = 0

    def draw(self, screen):

        self.player.draw(screen)

        for bullet in self.bullets:
            bullet.draw(screen)
        for enemy in self.enemies:
            enemy.draw(screen)

        font = pygame.font.Font(None, 36)
        score_text = font.render(f"Score : {self.score}", True, (255, 255, 255))
        lives_text = font.render(f"Vies : {self.lives}", True, (255, 255, 255))
        wave_text = font.render(f"Vague : {self.wave}", True, (255, 255, 255))

        screen.blit(score_text, (10, 10))
        screen.blit(lives_text, (10, 50))
        screen.blit(wave_text, (10, 90))

    def is_game_over(self):
        return self.lives <= 0
