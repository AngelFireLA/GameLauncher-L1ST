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

boutton_effacer_sauvegarde = boutton.BouttonImagé(682, 411, 674, 289, chemin_absolu_dossier+"assets/images/bouttons/boutton_effacer_sauvegarde.png")

def main():
    clock = pygame.time.Clock()
    fenetre = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))
    pygame.display.set_caption("Mode Histoire")
    sauvegarde_effacee = 0
    while True:
        est_sur_un_boutton = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
                    return

            if event.type == pygame.MOUSEBUTTONDOWN:
                if boutton_effacer_sauvegarde.boutton_clické(event):
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
                    if os.path.exists(os.path.join(chemin_absolu_dossier, "sauvegarde.txt")):
                        os.remove(os.path.join(chemin_absolu_dossier, "sauvegarde.txt"))
                        boutton_effacer_sauvegarde.afficher(fenetre)
                        sauvegarde_effacee = 2
                    else:
                        sauvegarde_effacee = 1



        fenetre.blit(arriere_plan, (0, 0))
        mouse_pos = pygame.mouse.get_pos()
        if souris_est_dans_zone(mouse_pos, boutton_effacer_sauvegarde.rect):
            est_sur_un_boutton = True

        boutton_effacer_sauvegarde.afficher(fenetre)

        if est_sur_un_boutton:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

        if sauvegarde_effacee == 1:
            afficher_texte(fenetre, largeur_fenetre//2, hauteur_fenetre//2+200,"Aucune sauvegarde à effacer", 70, dict_couleurs["rouge"], font=chemin_absolu_dossier+"assets/fonts/EBGaramond.ttf")
        elif sauvegarde_effacee == 2:
            afficher_texte(fenetre, largeur_fenetre//2, hauteur_fenetre//2+200,"Sauvegarde effacée", 70, dict_couleurs["vert"], font=chemin_absolu_dossier+"assets/fonts/EBGaramond.ttf")

        fenetre.blit(texte_options, (largeur_fenetre//2-texte_options.get_width()//2, 10))
        pygame.display.update()
        clock.tick(60)
