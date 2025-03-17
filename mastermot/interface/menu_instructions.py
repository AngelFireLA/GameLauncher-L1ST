import pygame

from . import boutton
from ..utils import afficher_texte, dict_couleurs, largeur_fenetre, hauteur_fenetre, chemin_absolu_dossier

largeur_fenetre = largeur_fenetre + 100
arriere_plan = pygame.image.load(chemin_absolu_dossier+"assets/images/menu_arrière_plan.jpg")
arriere_plan = pygame.transform.scale(arriere_plan, (largeur_fenetre, hauteur_fenetre))
boutton_reprendre = boutton.Boutton(largeur_fenetre // 2, hauteur_fenetre // 2 + 300, 400, 100, "Reprendre", dict_couleurs["bleu boutton"])

def main():
    en_cours = True
    clock = pygame.time.Clock()
    fenetre = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))
    pygame.display.set_caption("Instructions")
    while en_cours:
        fenetre.blit(arriere_plan, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if boutton_reprendre.boutton_clické(event):
                    return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return

        afficher_texte(fenetre, largeur_fenetre//2, 75, "Instructions", 100, couleur=dict_couleurs["bleu marin"])
        boutton_reprendre.afficher(fenetre)

        afficher_texte(fenetre, largeur_fenetre//2, 200, "Devinez le mot caché en 5 essais !", 36, couleur=dict_couleurs["bleu marin"])
        afficher_texte(fenetre, largeur_fenetre//2, 275, "Appuyez sur la touche Entrée ", 36, couleur=dict_couleurs["bleu marin"])
        afficher_texte(fenetre, largeur_fenetre//2, 325, "pour soumettre un essai :", 36, couleur=dict_couleurs["bleu marin"])
        afficher_texte(fenetre, largeur_fenetre//2, 400, "Case Rouge: La lettre n'est pas dans le mot.", 36, couleur=dict_couleurs["bleu marin"])
        afficher_texte(fenetre, largeur_fenetre//2, 450, "Case Jaune: La lettre est mal placée.", 36, couleur=dict_couleurs["bleu marin"])
        afficher_texte(fenetre, largeur_fenetre//2, 500, "Case Verte: La lettre est bien placée.", 36, couleur=dict_couleurs["bleu marin"])
        afficher_texte(fenetre, largeur_fenetre//2, 575, "Une lettre n'apparait qu'une fois par mot.", 36, couleur=dict_couleurs["bleu marin"])
        if en_cours: pygame.display.update()
        clock.tick(60)