from ..utils import afficher_texte, dict_couleurs, largeur_fenetre, hauteur_fenetre, chemin_absolu_dossier, couleurs_anneaux
import pygame
from ..moteur.partie import Partie
from . import menu_pause, boutton

arriere_plan = pygame.image.load(chemin_absolu_dossier+"assets/images/menu_arrière_plan.jpg")
arriere_plan = pygame.transform.scale(arriere_plan, (largeur_fenetre, hauteur_fenetre))

support = pygame.image.load(chemin_absolu_dossier+"assets/images/support_tourné.png")
support = pygame.transform.scale(support, (support.get_width(), 75))
niveau_sol = hauteur_fenetre - 100
positions_poteaux = {0: 150, 1:500, 2:850}

def afficher_tours(fenetre, partie, images_anneaux, largeur_anneaux, anneau_sélectionné, image_poteau):
    largeur_poteau = image_poteau.get_width()
    for i in range(3):
        x = positions_poteaux[i]
        fenetre.blit(image_poteau, (x, niveau_sol - image_poteau.get_height()))

    anneaux_rects = {}
    for i, tour in enumerate(partie.tours):
        x = positions_poteaux[i] + largeur_poteau//2
        y = niveau_sol - 20
        for j, anneau in enumerate(tour):

            if anneau == anneau_sélectionné:
                continue

            largeur_anneau = largeur_anneaux[anneau]
            #print("j:", j, "anneau:", anneau, "largeur_anneau:", largeur_anneau, "image_anneau:", images_anneaux[anneau-1])
            hauteur_anneau = 30
            anneau_rect = images_anneaux[anneau - 1].get_rect()
            # make the anneau rect 20 pixels longer

            anneau_rect.topleft = (x - largeur_anneau // 2, y - hauteur_anneau)
            fenetre.blit(images_anneaux[anneau - 1], anneau_rect)
            anneau_rect.width += 50
            anneau_rect.x -= 25
            anneau_rect.height += 50
            anneau_rect.y -= 25
            anneaux_rects[anneau] = anneau_rect
            y -= hauteur_anneau + 10
    return anneaux_rects


def poteau_proche(x):
    proche = None
    max_distance = float("inf")
    for i in range(3):
        distance = abs(positions_poteaux[i]-x)
        if distance < max_distance:
            max_distance = distance
            proche = i
    return proche


def main():
    def résoudre(n, départ, intermédiaire, arrivée):
        if n == 1:
            partie.bouger(départ, arrivée)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            fenetre.blit(arriere_plan, (0, 0))
            fenetre.blit(support, (0, niveau_sol - 20))
            afficher_tours(fenetre, partie, images_anneaux, largeur_anneaux, anneau_selectionner, poteau)
            afficher_texte(fenetre, largeur_fenetre - 175, 50, f"Coups: {partie.coups}", 50,
                           dict_couleurs["bleu marin"])
            pygame.time.wait(10)
            pygame.display.flip()
        else:
            résoudre(n - 1, départ, arrivée, intermédiaire)
            partie.bouger(départ, arrivée)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            fenetre.blit(arriere_plan, (0, 0))
            fenetre.blit(support, (0, niveau_sol - 20))
            afficher_tours(fenetre, partie, images_anneaux, largeur_anneaux, anneau_selectionner, poteau)
            afficher_texte(fenetre, largeur_fenetre - 175, 50, f"Coups: {partie.coups}", 50,
                           dict_couleurs["bleu marin"])
            pygame.time.wait(10)
            pygame.display.flip()

            résoudre(n - 1, intermédiaire, départ, arrivée)

    partie = Partie()
    clock = pygame.time.Clock()
    fenetre = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))
    pygame.display.set_caption("Tours de Hannoï")

    poteau = pygame.image.load(chemin_absolu_dossier + "assets/images/poteau_en_bois.png")
    poteau = pygame.transform.scale(poteau, (poteau.get_width() // 3, partie.taille*40))

    boutton_ajouter = boutton.BouttonImagé(310, 110, 75, 75, chemin_absolu_dossier + "assets/images/boutton_+.png")
    boutton_enlever = boutton.BouttonImagé(85, 110, 75, 75, chemin_absolu_dossier + "assets/images/boutton_-.png")
    boutton_résoudre = boutton.Boutton(largeur_fenetre//2+30, 50, 200, 75, "Résoudre", dict_couleurs["bleu boutton"])
    en_cours = True
    largeur_anneaux = {i: (i + 1) * 20+20 for i in range(1, 65)}
    images_anneaux = []

    for i in range(64):
        image_anneau = pygame.image.load(chemin_absolu_dossier + f"assets/images/anneau_{couleurs_anneaux[i%6]}.png")
        images_anneaux.append(pygame.transform.scale(image_anneau, (largeur_anneaux[i+1], 40)))

    anneau_selectionner = None
    tour_anneau_selectionner = None
    while en_cours:
        fenetre.blit(arriere_plan, (0, 0))
        fenetre.blit(support, (0, niveau_sol - 20))
        anneaux_rects = afficher_tours(fenetre, partie, images_anneaux, largeur_anneaux, anneau_selectionner, poteau)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if boutton_ajouter.boutton_clické(event):
                    if partie.taille < 15:
                        partie.taille += 1
                        partie.tours[0].insert(0, partie.taille)
                        poteau = pygame.transform.scale(poteau, (poteau.get_width(), partie.taille * 40))
                elif boutton_enlever.boutton_clické(event):
                    if partie.taille > 1:
                        if partie.taille in partie.tours[0]:
                            partie.tours[0].remove(partie.taille)
                        elif partie.taille in partie.tours[1]:
                            partie.tours[1].remove(partie.taille)
                        elif partie.taille in partie.tours[2]:
                            partie.tours[2].remove(partie.taille)
                        partie.taille -= 1
                        poteau = pygame.transform.scale(poteau, (poteau.get_width(), partie.taille*40))
                elif boutton_résoudre.boutton_clické(event):
                    résoudre(partie.taille, partie.tours[0], partie.tours[1], partie.tours[2])
                elif not anneau_selectionner and event.button == 1:
                    tour_la_plus_proche = partie.tours[poteau_proche(event.pos[0])]
                    for anneau in range(1, partie.taille+1):
                        if anneaux_rects[anneau].collidepoint(event.pos):
                            if len(tour_la_plus_proche) > 0 and tour_la_plus_proche[-1] == anneau:
                                anneau_selectionner = anneau
                                tour_anneau_selectionner = tour_la_plus_proche
                                break
            if event.type == pygame.MOUSEBUTTONUP:
                if anneau_selectionner and event.button == 1:
                    tour_la_plus_proche = partie.tours[poteau_proche(event.pos[0])]
                    if not tour_la_plus_proche or anneau_selectionner < tour_la_plus_proche[-1]:
                        partie.bouger(tour_anneau_selectionner, tour_la_plus_proche)
                        if partie.tours != [list(range(partie.taille, 0, -1)), [], []]:
                            boutton_résoudre.montrer = False
                        else:
                            boutton_résoudre.montrer = True
                    anneau_selectionner = None
                    tour_anneau_selectionner = None
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    résultat = menu_pause.main()
                    if résultat == 0:
                        return
                    elif résultat == 2:
                        partie = Partie()
                        anneau_selectionner = None
                        tour_anneau_selectionner = None
        if anneau_selectionner:
            fenetre.blit(images_anneaux[anneau_selectionner-1], pygame.mouse.get_pos())

        boutton_résoudre.afficher(fenetre)

        boutton_ajouter.afficher(fenetre)
        boutton_enlever.afficher(fenetre)
        afficher_texte(fenetre, 200, 40, f"Anneaux:", 60, dict_couleurs["bleu marin"])
        afficher_texte(fenetre, 200, 110, str(partie.taille), 70, dict_couleurs["bleu marin"])
        afficher_texte(fenetre, largeur_fenetre-175, 50, f"Coups: {partie.coups}", 50, dict_couleurs["bleu marin"])
        pygame.display.flip()
        clock.tick(60)