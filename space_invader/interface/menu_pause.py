import pygame

from . import boutton
from ..utils import afficher_texte, dict_couleurs, largeur_fenetre, hauteur_fenetre, chemin_absolu_dossier

#from interface import menu_options

arriere_plan = pygame.image.load(chemin_absolu_dossier+"assets/images/menu_arrière_plan.jpg")
arriere_plan = pygame.transform.scale(arriere_plan, (largeur_fenetre, hauteur_fenetre))


def main():

    en_cours = True
    clock = pygame.time.Clock()
    fenetre = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))
    pygame.display.set_caption("Space Invader")

    boutton_quitter = boutton.Boutton(largeur_fenetre // 2, hauteur_fenetre // 2 + 200, 400, 120, "Quitter",
                                      dict_couleurs["rouge"], (255, 100, 100), (20, 40, 70))
    boutton_reprendre = boutton.Boutton(largeur_fenetre // 2, hauteur_fenetre // 2 - 100, 400, 120, "Reprendre",
                                        dict_couleurs["bleu"], (150, 200, 255), (20, 40, 70))

    while en_cours:
        fenetre.blit(arriere_plan, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if boutton_quitter.est_clique():
                    return False
                if boutton_reprendre.est_clique():
                    return True

        afficher_texte(fenetre, largeur_fenetre//2, 75, "Pause", 100, couleur=(20, 40, 70))
        boutton_quitter.afficher(fenetre)
        boutton_reprendre.afficher(fenetre)
        if en_cours: pygame.display.update()
        clock.tick(60)