import random
import pygame
import os
from . import boutton
from ..utils import afficher_texte, dict_couleurs, largeur_fenetre, hauteur_fenetre, chemin_absolu_dossier, souris_est_dans_zone
from . import partie_en_cours
arriere_plan = pygame.image.load(chemin_absolu_dossier+"assets/images/menu_arrière_plan.png")
arriere_plan = pygame.transform.scale(arriere_plan, (largeur_fenetre, hauteur_fenetre))
texte_style_histoire = pygame.image.load(chemin_absolu_dossier+"assets/images/textes/texte_style_histoire.png")
texte_style_histoire = pygame.transform.scale(texte_style_histoire, (texte_style_histoire.get_width()*0.7, texte_style_histoire.get_height()*0.8))
boutton_histoire_principale = boutton.BouttonImagé(682, 311, (1496//4), (641//4), chemin_absolu_dossier+"assets/images/bouttons/boutton_histoire_principale.png")
boutton_générée_en_direct = boutton.BouttonImagé(682, 500, (1424//4), (637//4), chemin_absolu_dossier+"assets/images/bouttons/boutton_générée_en_direct.png")
boutton_pré_générée = boutton.BouttonImagé(682, 691, (1233//3), (428//3), chemin_absolu_dossier+"assets/images/bouttons/boutton_pré_générée.png")
boutton_histoire_principale_grossi = boutton.BouttonImagé(682, 311, (1496//4)*1.05, (641//4)*1.05, chemin_absolu_dossier+"assets/images/bouttons/boutton_histoire_principale.png")
boutton_générée_en_direct_grossi = boutton.BouttonImagé(682, 500, (1424//4)*1.05, (637//4)*1.05, chemin_absolu_dossier+"assets/images/bouttons/boutton_générée_en_direct.png")
boutton_pré_générée_grossi = boutton.BouttonImagé(682, 691, (1233//3)*1.05, (428//3)*1.05, chemin_absolu_dossier+"assets/images/bouttons/boutton_pré_générée.png")


def main():
    clock = pygame.time.Clock()
    fenetre = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))
    pygame.display.set_caption("Mode Histoire")
    assombrissement = False
    temps_assombrissement = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
                    return
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE and assombrissement:
                        temps_assombrissement = 255
            if event.type == pygame.MOUSEBUTTONDOWN and not assombrissement:
                if boutton_histoire_principale.boutton_clické(event):
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
                    assombrissement = True
                    temps_assombrissement = 0
                if boutton_générée_en_direct.boutton_clické(event):
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
                    pass
                if boutton_pré_générée.boutton_clické(event):
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
                    pass

        fenetre.blit(arriere_plan, (0, 0))
        mouse_pos = pygame.mouse.get_pos()
        fenetre.blit(texte_style_histoire, (largeur_fenetre//2-texte_style_histoire.get_width()//2, 30))

        if souris_est_dans_zone(mouse_pos, boutton_histoire_principale.rect) and not assombrissement:
            boutton_histoire_principale_grossi.afficher(fenetre)
        else:
            boutton_histoire_principale.afficher(fenetre)
        if souris_est_dans_zone(mouse_pos, boutton_générée_en_direct.rect) and not assombrissement:
            boutton_générée_en_direct_grossi.afficher(fenetre)
        else:
            boutton_générée_en_direct.afficher(fenetre)
        if souris_est_dans_zone(mouse_pos, boutton_pré_générée.rect) and not assombrissement:
            boutton_pré_générée_grossi.afficher(fenetre)
        else:
            boutton_pré_générée.afficher(fenetre)

        if (souris_est_dans_zone(mouse_pos, boutton_histoire_principale.rect) or souris_est_dans_zone(mouse_pos, boutton_générée_en_direct.rect) or souris_est_dans_zone(mouse_pos, boutton_pré_générée.rect)) and not assombrissement:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

        if assombrissement:
            temps_assombrissement = min(temps_assombrissement+3, 255)
            # Create a temporary surface with SRCALPHA for alpha blending.
            fade_surface = pygame.Surface((largeur_fenetre, hauteur_fenetre), pygame.SRCALPHA)
            fade_surface.fill((0, 0, 0, temps_assombrissement))
            fenetre.blit(fade_surface, (0, 0))
            if temps_assombrissement >= 255:
                assombrissement = False
                temps_assombrissement = 0
                print("démarré")
                partie_en_cours.lancer_histoire_principale()


        pygame.display.update()
        clock.tick(60)
