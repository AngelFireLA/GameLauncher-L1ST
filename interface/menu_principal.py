import random
import pygame
import os
pygame.init()

import interface.boutton as boutton
from utils import afficher_texte, dict_couleurs, largeur_fenetre, hauteur_fenetre, chemin_absolu_dossier
from interface import menu_sélection_de_jeu

arriere_plan = pygame.image.load(chemin_absolu_dossier+"assets/images/menu_arrière_plan_principal.jpg")
arriere_plan = pygame.transform.scale(arriere_plan, (largeur_fenetre, hauteur_fenetre))

boutton_mode_arcade = boutton.BouttonImagé(largeur_fenetre//2, 520, 420, 190, chemin_absolu_dossier+"assets/images/bouttons/boutton_arcade.png")
boutton_mode_histoire = boutton.BouttonImagé(largeur_fenetre//2, 270, 420, 245, chemin_absolu_dossier+"assets/images/bouttons/boutton_histoire.png")
boutton_mode_arcade_grossi = boutton.BouttonImagé(largeur_fenetre//2, 520, 420 + 10, 190 + 10, chemin_absolu_dossier+"assets/images/bouttons/boutton_arcade.png")
boutton_mode_histoire_grossi = boutton.BouttonImagé(largeur_fenetre//2, 270, 420 + 10, 245 + 10, chemin_absolu_dossier+"assets/images/bouttons/boutton_histoire.png")

def main():
    clock = pygame.time.Clock()
    computer_width = pygame.display.Info().current_w
    window_x = computer_width//2 - largeur_fenetre//2
    os.environ['SDL_VIDEO_WINDOW_POS'] = f"{window_x},100"
    fenetre = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))
    pygame.display.set_caption("Portail de Jeux")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if boutton_mode_arcade.boutton_clické(event):
                    menu_sélection_de_jeu.main()
                    fenetre = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))
                if boutton_mode_histoire.boutton_clické(event):
                    print("mode histoire")
        fenetre.blit(arriere_plan, (0, 0))
        if boutton_mode_arcade.rect.collidepoint(pygame.mouse.get_pos()):
            boutton_mode_arcade_grossi.afficher(fenetre)
        else:
            boutton_mode_arcade.afficher(fenetre)
        if boutton_mode_histoire.rect.collidepoint(pygame.mouse.get_pos()):
            boutton_mode_histoire_grossi.afficher(fenetre)
        else:
            boutton_mode_histoire.afficher(fenetre)
        pygame.display.update()
        clock.tick(60)

if __name__ == "__main__":
    main()