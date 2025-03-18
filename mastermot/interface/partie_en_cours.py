import pygame
pygame.init()

from ..moteur.partie import Partie
from ..utils import largeur_fenetre, hauteur_fenetre, afficher_texte, dict_couleurs, souris_est_dans_zone, chemin_absolu_dossier
from . import menu_pause, boutton, menu_instructions

decalage = 50
arriere_plan = pygame.image.load(chemin_absolu_dossier+"assets/images/menu_arrière_plan.jpg")
arriere_plan = pygame.transform.scale(arriere_plan, (largeur_fenetre, hauteur_fenetre))


def dessiner_cases(fenetre, grille_lettres, grille_couleurs, ligne_actuelle, case_selectionnee):

    largeur_case = 95
    hauteur_case = 95
    espacement_horizontal = 5
    espacement_vertical = 20

    x_initial = (largeur_fenetre - (5 * largeur_case + 4 * espacement_horizontal)) // 2
    y_initial = 100

    for ligne in range(5):
        for colonne in range(5):
            x = x_initial + colonne * (largeur_case + espacement_horizontal)
            y = y_initial + ligne * (hauteur_case + espacement_vertical)

            if grille_couleurs[ligne][colonne] == 0:
                if ligne == ligne_actuelle:
                    couleur_interieur = dict_couleurs["blanc"]
                elif ligne < ligne_actuelle:
                    couleur_interieur = dict_couleurs["rouge"]
                else:
                    couleur_interieur = dict_couleurs["gris clair"]
            elif grille_couleurs[ligne][colonne] == 1:
                couleur_interieur = dict_couleurs["jaune"]
            elif grille_couleurs[ligne][colonne] == 2:
                couleur_interieur = dict_couleurs["vert"]
            else:
                couleur_interieur = dict_couleurs["blanc"]

            pygame.draw.rect(fenetre, couleur_interieur, (x, y, largeur_case, hauteur_case))

            epaisseur_bordure = 6 if (ligne == ligne_actuelle and colonne == case_selectionnee) else 5
            couleur_bordure = dict_couleurs["bleu marin"] if (ligne == ligne_actuelle and colonne == case_selectionnee) else dict_couleurs["gris"]

            pygame.draw.rect(fenetre, couleur_bordure, (x, y, largeur_case, hauteur_case), epaisseur_bordure)

            if grille_lettres[ligne][colonne] != "":
                afficher_texte(fenetre, x + largeur_case // 2, y + hauteur_case // 2, grille_lettres[ligne][colonne].upper(), 45, dict_couleurs["bleu marin"])

    grille_coordonnées_cases = []
    for ligne in range(5):
        ligne_coordonnées_cases = []
        for colonne in range(5):
            x = x_initial + colonne * (largeur_case + espacement_horizontal)
            y = y_initial + ligne * (hauteur_case + espacement_vertical)
            ligne_coordonnées_cases.append((x, y, largeur_case, hauteur_case))
        grille_coordonnées_cases.append(ligne_coordonnées_cases)

    return grille_coordonnées_cases


def main():
    fenetre = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))
    pygame.display.set_caption("MasterMot")
    horloge = pygame.time.Clock()
    partie = Partie()

    ligne_actuelle = 0
    case_selectionnee = None
    grille_lettres = [["" for _ in range(5)] for _ in range(5)]
    grille_couleurs = [[0 for _ in range(5)] for _ in range(5)]
    est_victoire = False
    est_perdu = False
    boutton_instructions = boutton.Boutton(largeur_fenetre // 2, hauteur_fenetre - 75, 400, 75, "Instructions", dict_couleurs["bleu boutton"])
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if menu_pause.main():
                        return
                    else:
                        fenetre = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))

                if not est_victoire and not est_perdu:
                    if event.key == pygame.K_RETURN:
                        toutes_cases_remplies = True
                        for colonne in range(5):
                            if grille_lettres[ligne_actuelle][colonne] == "":
                                toutes_cases_remplies = False
                                break
                        if toutes_cases_remplies:
                            mot_saisi = "".join(grille_lettres[ligne_actuelle])
                            if partie.tester_mot(mot_saisi):
                                est_victoire = True
                                for colonne in range(5):
                                    grille_couleurs[ligne_actuelle][colonne] = 2
                            else:
                                for colonne in range(5):
                                    grille_couleurs[ligne_actuelle][colonne] = partie.progrès[colonne]

                                ligne_actuelle += 1
                                case_selectionnee = None

                                if ligne_actuelle >= 5:
                                    est_perdu = True

                    elif event.key == pygame.K_BACKSPACE:
                        grille_lettres[ligne_actuelle][case_selectionnee] = ""

                    elif event.unicode.isalpha():
                        lettre = event.unicode.lower()
                        replacements = {
                            'é': 'e', 'è': 'e', 'ê': 'e', 'ë': 'e',
                            'à': 'a', 'â': 'a', 'ä': 'a',
                            'ù': 'u', 'û': 'u', 'ü': 'u',
                            'î': 'i', 'ï': 'i',
                            'ô': 'o', 'ö': 'o',
                            'ç': 'c'
                        }
                        for lettre_avec_accent, lettre_sans_accent in replacements.items():
                            if lettre == lettre_avec_accent:
                                lettre = lettre_sans_accent
                        if lettre.isalpha():
                            grille_lettres[ligne_actuelle][case_selectionnee] = lettre

            if event.type == pygame.MOUSEBUTTONDOWN and not est_victoire and not est_perdu:
                if boutton_instructions.boutton_clické(event):
                    menu_instructions.main()
                    fenetre = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))
                else:
                    pos_souris = pygame.mouse.get_pos()
                    cases = dessiner_cases(fenetre, grille_lettres, grille_couleurs, ligne_actuelle, case_selectionnee)

                    for colonne in range(5):
                        if souris_est_dans_zone(pos_souris, cases[ligne_actuelle][colonne]):
                            case_selectionnee = colonne
                            break
                        else:
                            case_selectionnee = None

        fenetre.blit(arriere_plan, (0, 0))
        afficher_texte(fenetre, largeur_fenetre//2, 50, "MasterMot", 75, couleur=dict_couleurs["bleu marin"])
        dessiner_cases(fenetre, grille_lettres, grille_couleurs, ligne_actuelle, case_selectionnee)

        if est_victoire:
            afficher_texte(fenetre, largeur_fenetre // 2, hauteur_fenetre - 60, "Bravo! Vous avez trouvé le mot!", 43, dict_couleurs["vert"])
        elif est_perdu:
            afficher_texte(fenetre, largeur_fenetre // 2, hauteur_fenetre - 60, f"Dommage! Le mot était: {partie.mot}", 43, dict_couleurs["rouge"])
        else:
            boutton_instructions.afficher(fenetre)
        pygame.display.flip()
        horloge.tick(60)