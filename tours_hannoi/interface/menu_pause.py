import pygame

from . import boutton
from ..utils import afficher_texte, dict_couleurs, largeur_fenetre, hauteur_fenetre, chemin_absolu_dossier

arriere_plan = pygame.image.load(chemin_absolu_dossier+"assets/images/menu_arrière_plan.jpg")
arriere_plan = pygame.transform.scale(arriere_plan, (largeur_fenetre, hauteur_fenetre))
boutton_quitter = boutton.Boutton(largeur_fenetre // 2, hauteur_fenetre // 2 + 200, 400, 100, "Quitter", dict_couleurs["rouge"], couleur_surlignée=(255, 90, 90))
boutton_reprendre = boutton.Boutton(largeur_fenetre // 2, hauteur_fenetre // 2 - 100, 400, 100, "Reprendre", dict_couleurs["bleu boutton"])
boutton_recommencer = boutton.Boutton(largeur_fenetre // 2, hauteur_fenetre // 2 + 50, 500, 100, "Redémarrer", dict_couleurs["bleu boutton"], amplitude_arrondi=1.6)

def main():
    en_cours = True
    clock = pygame.time.Clock()
    fenetre = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))
    pygame.display.set_caption("Partie en Pause")
    while en_cours:
        fenetre.blit(arriere_plan, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if boutton_quitter.boutton_clické(event):
                    return 0
                if boutton_reprendre.boutton_clické(event):
                    return 1
                if boutton_recommencer.boutton_clické(event):
                    return 2

        afficher_texte(fenetre, largeur_fenetre//2, 75, "Pause", 100, couleur=dict_couleurs["bleu marin"])
        boutton_quitter.afficher(fenetre)
        boutton_reprendre.afficher(fenetre)
        boutton_recommencer.afficher(fenetre)
        if en_cours: pygame.display.update()
        clock.tick(60)