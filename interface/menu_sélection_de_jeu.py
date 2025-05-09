import random
import pygame
import os
pygame.init()

import interface.boutton as boutton
from utils import afficher_texte, dict_couleurs, largeur_fenetre, chemin_absolu_dossier
from morpion.interface import menu_principal as morpion_menu_principal
from echecs.interface import menu_principal as echecs_menu_principal
from mastermot.interface import partie_en_cours as mastermot_partie_en_cours
from puissance4.interface import menu_principal as puissance4_menu_principal
from mastermind.interface import partie_en_cours as mastermind_partie_en_cours
from tours_hannoi.interface import partie_en_cours as tours_hannoi_partie_en_cours
from space_invader.interface import menu_principal as space_invader_menu_principal
hauteur_fenetre = 900
arriere_plan = pygame.image.load(chemin_absolu_dossier+"assets/images/menu_arrière_plan_arcade.png")
arriere_plan = pygame.transform.scale(arriere_plan, (largeur_fenetre, hauteur_fenetre))
icone_échecs = pygame.image.load(chemin_absolu_dossier+"assets/images/icones_jeux/échecs.png")
icone_mastermot = pygame.image.load(chemin_absolu_dossier+"assets/images/icones_jeux/mastermot.png")
icone_morpion = pygame.image.load(chemin_absolu_dossier+"assets/images/icones_jeux/morpion.png")
icone_puissance4 = pygame.image.load(chemin_absolu_dossier+"assets/images/icones_jeux/puissance4.png")
icone_mastermind = pygame.image.load(chemin_absolu_dossier+"assets/images/icones_jeux/mastermind.png")
icone_tours_hannoi = pygame.image.load(chemin_absolu_dossier+"assets/images/icones_jeux/tours_hannoi.png")

taille_icone = 80
x_initial, y_initial = 200, 350
espace_x = 90
espace_y = 100
positions_icones = []
for i in range(3):
    for j in range(4):
        position = (x_initial + j*(espace_x + taille_icone//2), y_initial + i*(espace_y + taille_icone//2))
        positions_icones.append(position)


boutton_puissance4 = boutton.BouttonImagé(positions_icones[0][0], positions_icones[0][1], taille_icone, taille_icone, "assets/images/icones_jeux/puissance4.png")
boutton_échecs = boutton.BouttonImagé(positions_icones[4][0], positions_icones[4][1], taille_icone, taille_icone, "assets/images/icones_jeux/échecs.png")
boutton_morpion = boutton.BouttonImagé(positions_icones[2][0], positions_icones[2][1], taille_icone, taille_icone, "assets/images/icones_jeux/morpion.png")
boutton_mastermot = boutton.BouttonImagé(positions_icones[3][0], positions_icones[3][1], taille_icone, taille_icone, "assets/images/icones_jeux/mastermot.png")
boutton_mastermind = boutton.BouttonImagé(positions_icones[1][0], positions_icones[1][1], taille_icone, taille_icone, "assets/images/icones_jeux/mastermind.png")
boutton_tours_hannoi = boutton.BouttonImagé(positions_icones[5][0], positions_icones[5][1], taille_icone, taille_icone, "assets/images/icones_jeux/tours_hannoi.png")
boutton_space_invader = boutton.BouttonImagé(positions_icones[6][0], positions_icones[6][1], taille_icone, taille_icone, "assets/images/icones_jeux/space_invader.png")

boutton_puissance4_grossi = boutton.BouttonImagé(positions_icones[0][0], positions_icones[0][1], taille_icone + 10, taille_icone + 10, "assets/images/icones_jeux/puissance4.png")
boutton_échecs_grossi = boutton.BouttonImagé(positions_icones[4][0], positions_icones[4][1], taille_icone + 10, taille_icone + 10, "assets/images/icones_jeux/échecs.png")
boutton_morpion_grossi = boutton.BouttonImagé(positions_icones[2][0], positions_icones[2][1], taille_icone + 10, taille_icone + 10, "assets/images/icones_jeux/morpion.png")
boutton_mastermot_grossi = boutton.BouttonImagé(positions_icones[3][0], positions_icones[3][1], taille_icone + 10, taille_icone + 10, "assets/images/icones_jeux/mastermot.png")
boutton_mastermind_grossi = boutton.BouttonImagé(positions_icones[1][0], positions_icones[1][1], taille_icone + 10, taille_icone + 10, "assets/images/icones_jeux/mastermind.png")
boutton_tours_hannoi_grossi = boutton.BouttonImagé(positions_icones[5][0], positions_icones[5][1], taille_icone + 10, taille_icone + 10, "assets/images/icones_jeux/tours_hannoi.png")
boutton_space_invader_grossi = boutton.BouttonImagé(positions_icones[6][0], positions_icones[6][1], taille_icone + 10, taille_icone + 10, "assets/images/icones_jeux/space_invader.png")


def main():
    clock = pygame.time.Clock()
    fenetre = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))
    pygame.display.set_caption("Mode Arcade")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return
            if event.type == pygame.MOUSEBUTTONDOWN:
                if boutton_morpion.boutton_clické(event):
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
                    morpion_menu_principal.main()
                    fenetre = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))

                if boutton_échecs.boutton_clické(event):
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
                    echecs_menu_principal.main()
                    fenetre = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))

                if boutton_mastermot.boutton_clické(event):
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
                    mastermot_partie_en_cours.main()
                    fenetre = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))

                if boutton_puissance4.boutton_clické(event):
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
                    puissance4_menu_principal.main()
                    fenetre = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))

                if boutton_mastermind.boutton_clické(event):
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
                    mastermind_partie_en_cours.main()
                    fenetre = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))

                if boutton_tours_hannoi.boutton_clické(event):
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
                    tours_hannoi_partie_en_cours.main()
                    fenetre = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))

                if boutton_space_invader.boutton_clické(event):
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
                    space_invader_menu_principal.main()
                    fenetre = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))

        fenetre.fill((0, 0, 0))
        fenetre.blit(arriere_plan, (0, 0))
        est_sur_un_boutton = False
        pos_souris = pygame.mouse.get_pos()

        if boutton_puissance4.rect.collidepoint(pygame.mouse.get_pos()):
            est_sur_un_boutton = True
            boutton_puissance4_grossi.afficher(fenetre)
        else:
            boutton_puissance4.afficher(fenetre)
        afficher_texte(fenetre, positions_icones[0][0], positions_icones[0][1] + taille_icone // 2 + 20, "Puissance4", 20, dict_couleurs["blanc"])

        if boutton_mastermind.rect.collidepoint(pos_souris):
            boutton_mastermind_grossi.afficher(fenetre)
            est_sur_un_boutton = True
        else:
            boutton_mastermind.afficher(fenetre)
        afficher_texte(fenetre, positions_icones[1][0], positions_icones[1][1] + taille_icone // 2 + 20, "MasterMind",19, dict_couleurs["blanc"])

        if boutton_morpion.rect.collidepoint(pos_souris):
            boutton_morpion_grossi.afficher(fenetre)
            est_sur_un_boutton = True
        else:
            boutton_morpion.afficher(fenetre)
        afficher_texte(fenetre, positions_icones[2][0], positions_icones[2][1] + taille_icone//2 + 20, "Morpion", 20, dict_couleurs["blanc"])

        if boutton_mastermot.rect.collidepoint(pos_souris):
            boutton_mastermot_grossi.afficher(fenetre)
            est_sur_un_boutton = True
        else:
            boutton_mastermot.afficher(fenetre)
        afficher_texte(fenetre, positions_icones[3][0], positions_icones[3][1] + taille_icone//2 + 20, "MasterMot", 20, dict_couleurs["blanc"])

        if boutton_échecs.rect.collidepoint(pos_souris):
            boutton_échecs_grossi.afficher(fenetre)
            est_sur_un_boutton = True
        else:
            boutton_échecs.afficher(fenetre)
        afficher_texte(fenetre, positions_icones[4][0], positions_icones[4][1] + taille_icone//2 + 20, "Echecs", 20, dict_couleurs["blanc"])

        if boutton_tours_hannoi.rect.collidepoint(pos_souris):
            boutton_tours_hannoi_grossi.afficher(fenetre)
            est_sur_un_boutton = True
        else:
            boutton_tours_hannoi.afficher(fenetre)
        afficher_texte(fenetre, positions_icones[5][0]-5, positions_icones[5][1] + taille_icone//2 + 20, "Tours de Hannoï", 18, dict_couleurs["blanc"])

        if boutton_space_invader.rect.collidepoint(pos_souris):
            boutton_space_invader_grossi.afficher(fenetre)
            est_sur_un_boutton = True
        else:
            boutton_space_invader.afficher(fenetre)
        afficher_texte(fenetre, positions_icones[6][0]+15, positions_icones[6][1] + taille_icone//2 + 20, "Space Invader", 20, dict_couleurs["blanc"])

        if est_sur_un_boutton:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

        afficher_texte(fenetre, largeur_fenetre//2, 85, "Mode Arcade", 70, dict_couleurs["bleu marin"])
        pygame.display.update()
        clock.tick(60)
