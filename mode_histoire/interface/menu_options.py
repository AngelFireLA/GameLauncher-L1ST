import random
import pygame
import os


from . import boutton
from ..utils import afficher_texte, dict_couleurs, largeur_fenetre, hauteur_fenetre, chemin_absolu_dossier, \
    souris_est_dans_zone

arriere_plan = pygame.image.load(chemin_absolu_dossier+"assets/images/menu_arrière_plan.png")
arriere_plan = pygame.transform.scale(arriere_plan, (largeur_fenetre, hauteur_fenetre))
texte_options = pygame.image.load(chemin_absolu_dossier+"assets/images/textes/texte_options.png")
texte_options = pygame.transform.scale(texte_options, (texte_options.get_width()*0.55, texte_options.get_height()*0.55))
def main():
    clock = pygame.time.Clock()
    fenetre = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))
    pygame.display.set_caption("Mode Histoire")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
                    return

            if event.type == pygame.MOUSEBUTTONDOWN:
                pass



        fenetre.blit(arriere_plan, (0, 0))
        mouse_pos = pygame.mouse.get_pos()
        fenetre.blit(texte_options, (largeur_fenetre//2-texte_options.get_width()//2, 10))
        pygame.display.update()
        clock.tick(60)
