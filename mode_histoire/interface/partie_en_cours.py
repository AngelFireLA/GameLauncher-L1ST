import os
from math import tanh, exp
from morpion.interface import partie_en_cours as morpion_partie
from puissance4.interface import partie_en_cours as puissance4_partie
import pygame
from ..utils import chemin_absolu_dossier, largeur_fenetre, hauteur_fenetre, dict_couleurs, afficher_texte
from .texte_apparaissant import TexteApparaissant

arrière_plan = pygame.image.load(chemin_absolu_dossier+"assets/images/parchemin.png")
logo_histoire_principale = pygame.image.load(chemin_absolu_dossier+"assets/images/logo_histoire.png")
logo_histoire_principale = pygame.transform.scale(logo_histoire_principale, (largeur_fenetre, hauteur_fenetre))
histoire_principale_en_liste = story = [
    "Le joueur se réveilla dans un endroit inconnu.\n Il ne sait pas qui il est, ni où il est.\nAprès avoir observé ses environs, il en déduit être sur une île.\nIl peut voir des sortes de chapiteaux au loin, et différents faisceaux de lumière.",
    "Après avoir marché un peu le long du seul chemin présent devant lui, il rencontra un clown gardant un pont.",
    "Assis sur une fine colonne de pierre, celui-ci interpella le joueur :\n“Hé toi, ne pense même pas à passer sans me payer le passage. T’as bien pris de quoi jouer avec toi ?” lança-t-il.",
    "Voyant le regard confus du joueur, il fut un peu surpris. “Me dis pas que tu es venu dans ce bourbier volontairement sans te préparer un minimum ?” continua-t-il.",
    "Le joueur, toujours confus, répondit :\n“De quoi jouer … ? Désolé, je ne me souviens plus de rien, je veux juste rentrer chez moi…”",
    "Le clown lui répondit : “Bon, je vais t'expliquer : sur cette île, tu vas jouer à beaucoup de jeux, c’est un peu la monnaie d’échange sur cette île. Donc si tu veux t’échapper va falloir être bon, très bon même.”",
    "Après avoir répondu ça, il sourit de manière déconcertante et annonça : “Et justement, pour passer ce pont, tu vas devoir me battre à un jeu auquel j'ai toujours gagner, le morpion !”",
    "Il s’arrêta un moment pour réfléchir. “Bon, pour que ça soit un peu plus juste je vais te laisser commencer. Sur ce, c’est parti !”\nLe champ de vision du joueur s’assombrit rapidement...",
    1,
    "“Im-impossible ! Moi, je n'ai pas réussi à gagner ?” dit le clown choqué, avant de se redresser rapidement. “C’était qu’une partie de chauffe ok ?” insista le clown, même s’il bégayait un peu.",
    "Ayant vu clair dans son jeu, le joueur rétorqua : “C’est TOI qui m’a dit que si je gagnais tu me laisserais passer. J’ai gagné à ton jeu, donc selon les règles à la noix de cette île que tu m’as raconté, tu n’as pas le choix.” insista-t-il fermement.",
    "Le clown, un peu en panique, formula une réplique : “Bon, je vais te faire une offre que tu ne pourras pas refuser : quitte ou double. On refait une partie, et si tu obtiens une victoire contre moi, je te donnerai des infos cruciales à propos de l'île, c’est pas un très bon deal ça ?”",
    "Il continua : “Enfin, je risque de passer un sale quart d’heure si on découvre que j’en ai trop dit à un participant…” dit-il en se grattant la tête d’une main. “Donc bon, deal ou pas deal? Par contre, cette fois-ci c’est moi qui commence !”",
    "Le joueur y réfléchit quelques temps. Il se dit que de toute façon il avait déjà battu ce clown, qu'il avait crucialement besoin d'informations sur cette île, donc cette offre valait le coup.",
    "“D’accord, j’accepte ces conditions” affirma-t-il.\nÀ l’instant même où il prononça ces mots, sa vision s’assombrit.",
    2, # [partie où le joueur fait égalité au mieux...]
    "Peu de temps après la fin de la partie, le joueur retrouva ses esprits. Il remarqua que le sol était plus dur que l’herbe où il avait marché avant ; c’était presque métallique. Il n’y pensa pas grand-chose puisqu’autre chose le préoccupait.",
    "Une sensation de défaite. Pourtant… il n’avait pas perdu ? Donc c’est bon non ?\nLe clow interrompit ses pensées : “Dommage, tu gagneras peut être la prochaine fois, au moins ça me fait une victoire supplémentaire” dit-il en souriant.",
    "Il descendit de la mini-colonne de pierre, “À la prochaine !”\nSoudainement, le joueur sentit le sol vibrer sous ses pieds, assez fort pour le faire tomber.\nIl lança : “Attends, comment ça ? Pourtant je n’ai pas perdu ! On a fait égalité...”",
    "Le joueur se rendit compte que le clown l’avait piégé avec la formulation du second défi. Et sur ce, une trappe s’ouvrit sous ses pieds, et le joueur commença à tomber…",
    "Il faisait sombre, dans le trou jusqu’à ce que soudainement le joueur fut ébloui par des lumières vives, et très peu de temps après, il y eut l'impact.",
    "Sa chute avait été arrêtée, et surprenamment, il n’était pas en trop mauvais état. Il sentait qu’il était tombé sur quelque chose d’un peu mou.",
    "Il se releva avec un peu de mal pour pouvoir voir sur quoi il était atterri : c’était juste un vieux matelas qui avait pu stopper sa chute.",
    "Il décida d’observer son environnement. Après tout, il était quand même tombé d’assez haut. Où est-ce qu’il aurait bien pu atterrir qui serait sous-terre ?",
    "Il commença à se déplacer, et reconnut une sorte de chapiteau, comme on en voit dans les cirques, mais il avait l’air un peu vide. Même les cages d’animaux avaient l'air abandonnées.",
    "Après avoir marché un peu, il trouva une porte. Comme ça, une porte en bois, qui n’avait pas l’air à sa place ici. Il essaya de tourner la poignée pour l’ouvrir mais rien n’y fit.",
    "Soudainement, trois ombres sortirent du sol rapidement, ce qui fit sursauter et reculer le joueur. 3 clowns apparurent devant lui, ils avaient l’air identiques.\n“Effrayant” pensa le joueur.",
    "Le clown du milieu prit la parole : “Bienvenue au Cirque des Jetons ! Je devine que c’est Marc qui t’as fait atterrir ici, il faut vraiment qu’il arrête de faire ça.” dit-il un peu agacé.",
    "Il se reprit avec un ton progressivement plus sombre : “Bref, si tu veux passer, il va falloir tous nous battre à un jeu, sinon, tu préfères ne pas savoir…” Son expression retourna très rapidement à une expression joyeuse, même si le joueur pensa que ce n’était qu’un masque.",
    "“À quel jeu doit-on jouer ? Je ne comprends pas trop ce qu’il se passe, mais ce dont je suis sûr c’est que je dois sortir de cette île, donc finissons-en !” s’exclama le joueur.",
    "Un des clowns, celui de droite cette fois, avait l’air confus après avoir entendu le joueur : “Ah bon ? Tu veux partir après ce qu’il a fallu faire pour venir ? Pas tout le monde n’est prêt à-”",
    "Avant qu’il puisse finir, le clown central l’interrompit : “Chut, tu sais qu’on ne doit pas dire ça aux participants, t’as oublié qu’ils perdent leur mémoire tant qu’ils sont sur cette île ?!” dit-il au clown qui venait de parler.",
    "Il se retourna ensuite vers le joueur : “N’écoute pas mon frère qui radote, jouons ! Le jeu choisi est le Puissance 4. Bats-nous tous et on te laissera franchir cette porte. Tu es prêt? Sur ce, c’est parti” dit-il avec un grand sourire.",
    "Le joueur essaya de répliquer : “Attends-” mais sa vision s’assombrissait déjà.",
    3,
    "La vision du joueur lui revint progressivement. Son adversaire vaincu était déjà en train de rouspéter : “Tu as eu de la chance du débutant c’est tout ! On verra bien si tu arrives à gagner avec de la chance contre mon frère, il est encore meilleur que moi !”",
    "Le joueur réagit rapidement : “Mais attendez, je ne suis pas venu là pour jouer-”\nSa vision s’assombrit avant qu’il ne puisse dire quoi que ce soit d’autre.",
    4,
    "Comme le précédent, ce clown n’accepta pas sa défaite : “Quoi ?! Tu as triché c’est sûr ! C’est la seule explication de ma défaite !”\nAvant qu’il ne puisse continuer à se plaindre, le dernier clown l’interrompit. Il avait l’air plus calme que ses deux frères.",
    "“Stop, il a gagné équitablement, sinon il ne serait plus là.” Il se tourna ensuite vers le joueur : “Je reconnais ton niveau. Je serai ton dernier adversaire pour l’instant. Si tu me bats, on te laissera passer sans soucis, et qui sait, on répondra peut-être à quelques-unes de tes questions.”",
    "“Il faut vraiment arrêter avec ça” s’écria le joueur pendant que son regard sombrait.",
    5,
    "Le joueur réémergea encore une fois, son adversaire déjà debout.\n“Mes frères n’ont donc pas perdu pour rien.” dit-il avec un faux sourire, visiblement un peu énervé à cause de sa défaite. “Pars vite, et que je ne te revois pas.”",
    "Le joueur ne perdit pas de temps et traversa la porte sans regarder en arrière, entrant dans un tunnel peu éclairé, avec plus loin, des escaliers de pierre. \n\n [FIN] (pour l'instant)"
]
def lancer_histoire_principale(dernier_texte=None):
    clock = pygame.time.Clock()
    fenêtre = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))
    pygame.display.set_caption("Histoire Principale")
    font = pygame.font.Font(chemin_absolu_dossier+"assets/fonts/EBGaramond.ttf", 60)
    zone_de_texte = pygame.Rect(130, 225, 1140, 500)
    try:
        indexe_histoire = histoire_principale_en_liste.index(dernier_texte) if dernier_texte is not None else 0
    except:
        indexe_histoire = 0
    histoire_apparaissante = None
    histoire_en_cours = False
    assombrissement = True
    temps_assombrissement = 0
    fichier_sauvegarde = chemin_absolu_dossier+"sauvegarde.txt"
    while assombrissement:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    temps_assombrissement = 255
        fenêtre.blit(logo_histoire_principale, (0, 0))
        temps_assombrissement = min(temps_assombrissement + 1.5, 255)
        fade_surface = pygame.Surface((largeur_fenetre, hauteur_fenetre), pygame.SRCALPHA)
        fade_surface.fill((0, 0, 0, 255-temps_assombrissement))
        fenêtre.blit(fade_surface, (0, 0))
        pygame.display.update()
        clock.tick(60)
        if temps_assombrissement >= 255:
            assombrissement = False
            temps_assombrissement = 0
            pygame.time.wait(2500)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if histoire_en_cours:
                        histoire_en_cours = False
                        histoire_apparaissante.force_arrêt()
                    else:
                        if indexe_histoire < len(histoire_principale_en_liste)-1:
                            if histoire_apparaissante is not None:
                                indexe_histoire += 1
                            prochaine_partie = histoire_principale_en_liste[indexe_histoire]
                            if type(prochaine_partie) == int:
                                if prochaine_partie in [1, 2]:
                                    veut_gagner = False if prochaine_partie == 1 else True
                                    morpion_partie.main(veut_gagner)
                                    fenêtre = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))


                                    indexe_histoire += 1
                                    histoire_en_cours = True
                                    histoire_apparaissante = TexteApparaissant(surface=fenêtre, font=font, texte=histoire_principale_en_liste[indexe_histoire], rect=zone_de_texte,couleur_texte=dict_couleurs["marron"])
                                if prochaine_partie in [3, 4, 5]:
                                    if prochaine_partie == 3:
                                        profondeur = 2
                                    elif prochaine_partie == 4:
                                        profondeur = 4
                                    elif prochaine_partie == 5:
                                        profondeur = 6

                                    résultat = puissance4_partie.main(profondeur)
                                    fenêtre = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))

                                    if résultat != 1:
                                        texte_défaite = "Quand le joueur revint à lui, il se rendit compte que tout autour de lui était figé.\nIl entendit une voix lui chuchoter “Je ne peux pas te laisser perdre comme ça”. Le joueur cligna des yeux, et il était de retour juste avant le début de la partie..."
                                        histoire_principale_en_liste.insert(indexe_histoire + 1, texte_défaite)
                                        histoire_principale_en_liste.insert(indexe_histoire + 2, prochaine_partie)
                                    indexe_histoire += 1
                                    histoire_en_cours = True
                                    histoire_apparaissante = TexteApparaissant(surface=fenêtre, font=font, texte=histoire_principale_en_liste[indexe_histoire], rect=zone_de_texte,couleur_texte=dict_couleurs["marron"])
                            else:
                                histoire_en_cours = True
                                histoire_apparaissante = TexteApparaissant(surface=fenêtre, font=font, texte=histoire_principale_en_liste[indexe_histoire], rect=zone_de_texte, couleur_texte=dict_couleurs["marron"])
                                if os.path.exists(fichier_sauvegarde):
                                    with open(fichier_sauvegarde, "w", encoding="utf-8") as f:
                                        f.write(str(prochaine_partie))



        fenêtre.fill((148, 106, 58))
        fenêtre.blit(arrière_plan, (0, 0))
        if histoire_apparaissante: histoire_apparaissante.draw()
        if histoire_en_cours:
            histoire_apparaissante.update()
        if histoire_apparaissante and histoire_apparaissante.fini:
            afficher_texte(fenêtre, largeur_fenetre//2, 800, texte="Appuyer sur Espace pour continuer...", taille=60, font=chemin_absolu_dossier+"assets/fonts/EBGaramond.ttf", couleur=dict_couleurs["marron"])
            histoire_en_cours = False


        pygame.display.update()
        clock.tick(60)
