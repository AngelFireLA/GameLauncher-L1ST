import random
import time

import pygame
pygame.init()
import os

from . import boutton
from . import menu_options
from . import partie_en_cours
from ..utils import afficher_texte, dict_couleurs, largeur_fenetre, hauteur_fenetre, chemin_absolu_dossier, souris_est_dans_zone

arriere_plan = pygame.image.load(chemin_absolu_dossier+"assets/images/menu_arrière_plan_full.png")
arriere_plan = pygame.transform.scale(arriere_plan, (largeur_fenetre, hauteur_fenetre))
boutton_commencer = boutton.BouttonImagé(682, 411, 485, 115, chemin_absolu_dossier+"assets/images/bouttons/boutton_commencer.png")
boutton_continuer = boutton.BouttonImagé(682, 551, 485, 115, chemin_absolu_dossier+"assets/images/bouttons/boutton_continuer.png")
boutton_options = boutton.BouttonImagé(682, 691, 485, 115, chemin_absolu_dossier+"assets/images/bouttons/boutton_options.png")
boutton_quitter = boutton.BouttonImagé(1186, 829, 340, 110, chemin_absolu_dossier+"assets/images/bouttons/boutton_quitter.png")
boutton_commencer_grossi = boutton.BouttonImagé(682, 411, 484*1.05, 115*1.05, chemin_absolu_dossier+"assets/images/bouttons/boutton_commencer.png")
boutton_continuer_grossi = boutton.BouttonImagé(682, 551, 485*1.05, 115*1.05, chemin_absolu_dossier+"assets/images/bouttons/boutton_continuer.png")
boutton_options_grossi = boutton.BouttonImagé(682, 691, 485*1.05, 115*1.05, chemin_absolu_dossier+"assets/images/bouttons/boutton_options.png")
boutton_quitter_grossi = boutton.BouttonImagé(1186, 829, 340*1.05, 110*1.05, chemin_absolu_dossier+"assets/images/bouttons/boutton_quitter.png")
def main():
    clock = pygame.time.Clock()
    fenetre = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))
    pygame.display.set_caption("Mode Histoire")
    fichier_de_sauvegarde = os.path.join(chemin_absolu_dossier, "sauvegarde.txt")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if boutton_quitter.boutton_clické(event):
                    return
                if boutton_options.boutton_clické(event):
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
                    menu_options.main()
                if boutton_commencer.boutton_clické(event):
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
                    partie_en_cours.lancer_histoire_principale()
                if boutton_continuer.boutton_clické(event) and os.path.exists(fichier_de_sauvegarde):
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
                    with open(fichier_de_sauvegarde, "r", encoding="utf-8") as f:
                        dernier_texte = f.read()
                    partie_en_cours.lancer_histoire_principale(dernier_texte)

        fenetre.blit(arriere_plan, (0, 0))
        mouse_pos = pygame.mouse.get_pos()
        if souris_est_dans_zone(mouse_pos, boutton_commencer.rect):
            boutton_commencer_grossi.afficher(fenetre)
        else:
            boutton_commencer.afficher(fenetre)

        if souris_est_dans_zone(mouse_pos, boutton_continuer.rect) and os.path.exists(fichier_de_sauvegarde):
            boutton_continuer_grossi.afficher(fenetre)
        else:
            boutton_continuer.afficher(fenetre)

        if souris_est_dans_zone(mouse_pos, boutton_options.rect):
            boutton_options_grossi.afficher(fenetre)
        else:
            boutton_options.afficher(fenetre)

        if souris_est_dans_zone(mouse_pos, boutton_quitter.rect):
            boutton_quitter_grossi.afficher(fenetre)
        else:
            boutton_quitter.afficher(fenetre)

        if souris_est_dans_zone(mouse_pos, boutton_commencer.rect) or souris_est_dans_zone(mouse_pos, boutton_continuer.rect) or souris_est_dans_zone(mouse_pos, boutton_options.rect) or souris_est_dans_zone(mouse_pos, boutton_quitter.rect):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)


        pygame.display.update()
        clock.tick(60)

if __name__ == "__main__":
    main()