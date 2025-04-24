import pygame
import os

def souris_est_dans_zone(souris, zone):
    x, y, largeur, hauteur = zone
    return x < souris[0] < x + largeur and y < souris[1] < y + hauteur


def afficher_texte(fenetre, x, y, texte, taille, couleur=(0, 0, 0), font="freesansbold.ttf"):
    font = pygame.font.Font(font, taille)
    texte = font.render(texte, True, couleur)
    text_rect = texte.get_rect(center=(x, y))
    fenetre.blit(texte, text_rect)


# liste de couleurs nom:rgb
dict_couleurs = {
    "rouge": (255, 0, 0),
    "vert": (0, 255, 0),
    "bleu": (0, 0, 255),
    "jaune": (255, 255, 0),
    "noir": (0, 0, 0),
    "blanc": (255, 255, 255),
    "gris": (128, 128, 128),
    "marron": (73, 48, 27),
    "rose": (255, 105, 180),
    "violet": (128, 0, 128),
    "cyan": (0, 255, 255),
    "orange": (255, 165, 0),
    "bleu marin": (20, 40, 70),
    "boutton": (255, 150, 113),
    "marron clair": (190, 118, 48),
}

largeur_fenetre, hauteur_fenetre = 1400, 900
chemin_absolu_dossier = os.path.dirname(os.path.abspath(__file__)) + "/"


def est_fin_de_phrase(mot, pos_caractère):
    if pos_caractère >= len(mot):
        return False

    char = mot[pos_caractère]
    return char in '.!?:'
