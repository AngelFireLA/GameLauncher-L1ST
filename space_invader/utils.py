import pygame
import os

largeur_fenetre = 1024
hauteur_fenetre = 768

def afficher_texte(fenetre, x, y, texte, taille, couleur=(255,255,255)):
    font = pygame.font.SysFont(None, taille)
    surf = font.render(texte, True, couleur)
    rect = surf.get_rect(center=(x, y))
    fenetre.blit(surf, rect)


dict_couleurs = {
    "noir": (0, 0, 0),
    "bleu": (115, 154, 255),
    "rouge": (255,50,50),
    "blanc": (255,255,255),
    "gris": (30,30,30),
}

chemin_absolu_dossier = os.path.dirname(os.path.abspath(__file__)) + "/"
