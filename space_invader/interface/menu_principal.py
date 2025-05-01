import pygame, sys, os
from .boutton import Boutton
from ..utils import afficher_texte, largeur_fenetre, hauteur_fenetre, dict_couleurs, chemin_absolu_dossier
from . import partie_en_cours
def main():
    pygame.init()
    screen = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))
    pygame.display.set_caption("Space Invader")
    clock = pygame.time.Clock()

    # Fond
    bg = pygame.image.load(chemin_absolu_dossier+"assets/images/menu_arrière_plan.jpg")
    bg = pygame.transform.scale(bg, (largeur_fenetre, hauteur_fenetre))

    # Boutons : Jouer et Quitter
    bouton_jouer = Boutton(largeur_fenetre//2, hauteur_fenetre//2, 400, 120,
                           "Jouer", dict_couleurs["bleu"],(150,200,255),(20, 40, 70))
    bouton_quitter = Boutton(largeur_fenetre//2, hauteur_fenetre//2 + 300, 200, 60,
                             "Quitter", dict_couleurs["rouge"], (255,100,100),(20, 40, 70))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()

        if bouton_jouer.est_clique():
            os.chdir(os.path.join(os.path.dirname(__file__), os.pardir))

            partie_en_cours.main()

        if bouton_quitter.est_clique():
            return

        screen.blit(bg, (0,0))
        # Titre en noir pour plus de contraste
        afficher_texte(screen, largeur_fenetre//2, 75, "Space Invader", 100, (20, 40, 70))

        bouton_jouer.afficher(screen)
        bouton_quitter.afficher(screen)

        pygame.display.update()
        clock.tick(60)

if __name__=='__main__':
    main()