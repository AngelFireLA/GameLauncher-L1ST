import pygame
import time
from ..utils import est_fin_de_phrase

class TexteApparaissant:
    def __init__(self, surface, font, texte, rect, couleur_texte=(255, 255, 255), caractères_par_seconde=20, pause_après_phrase=0.75, pause_après_virgule=0.25, espace_entre_lignes=1):
        self.surface = surface
        self.font = font
        self.texte = texte
        self.rect = rect
        self.couleur_texte = couleur_texte
        self.espace_entre_lignes = espace_entre_lignes

        self.caractères_par_seconde = caractères_par_seconde
        self.temps_entre_caractères = 1.0 / self.caractères_par_seconde

        self.pause_après_phrase = pause_après_phrase
        self.pause_après_virgule = pause_après_virgule
        self.timer_pause = 0
        self.en_pause_de_fin_de_phrase = False
        self.en_pause_de_virugle = False
        self.données_mots = self.calcul_position_mots()

        self.caractères_totaux = sum(len(mot['texte']) for mot in self.données_mots if mot['texte'] != '\n')
        self.caractères_montrés = 0
        self.temps_depuis_update = time.time()
        self.fini = False


    def reset(self):
        self.caractères_montrés = 0
        self.fini = False
        self.en_pause_de_fin_de_phrase = False
        self.données_mots = self.calcul_position_mots()
        self.caractères_totaux = sum(len(mot['texte']) for mot in self.données_mots if mot['texte'] != '\n')
        self.timer_pause = 0
        self.temps_depuis_update = time.time()



    def calcul_position_mots(self):
        données_mots = []
        mots = []

        for line in self.texte.split('\n'):
            mots.extend(line.split() + ['\n'])

        if mots and mots[-1] == '\n':
            mots.pop()

        x, y = self.rect.x, self.rect.y
        hauteur_ligne = self.font.get_linesize() + self.espace_entre_lignes
        largeur_ligne = 0

        for mot in mots:
            if mot == '\n':
                données_mots.append({
                    'texte': '\n',
                    'x': 0,
                    'y': 0,
                    'caractères_visibles': 0
                })
                y += hauteur_ligne
                largeur_ligne = 0
                continue

            if largeur_ligne > 0:
                largeur_espace = self.font.size(' ')[0]
                largeur_ligne += largeur_espace

            largeur_mot = self.font.size(mot)[0]

            if largeur_ligne + largeur_mot > self.rect.width:
                y += hauteur_ligne
                largeur_ligne = 0

            données_mots.append({
                'texte': mot,
                'x': self.rect.x + largeur_ligne,
                'y': y,
                'caractères_visibles': 0
            })

            largeur_ligne += largeur_mot

        return données_mots



    def update(self):
        if self.fini:
            return

        temps_actuel = time.time()

        if self.en_pause_de_fin_de_phrase:
            if temps_actuel - self.timer_pause >= self.pause_après_phrase:
                self.en_pause_de_fin_de_phrase = False
                self.temps_depuis_update = temps_actuel
            else:
                return
        elif self.en_pause_de_virugle:
            if temps_actuel - self.timer_pause >= self.pause_après_virgule:
                self.en_pause_de_virugle = False
                self.temps_depuis_update = temps_actuel
            else:
                return

        temps_écoulé = temps_actuel - self.temps_depuis_update

        cmb_de_caractères_à_montré = temps_écoulé * self.caractères_par_seconde

        if cmb_de_caractères_à_montré >= 1:
            self.temps_depuis_update = temps_actuel

            caractères_restants_à_montrer = int(cmb_de_caractères_à_montré)
            pos_mot = 0

            while caractères_restants_à_montrer > 0 and pos_mot < len(self.données_mots):
                données_mot = self.données_mots[pos_mot]

                if données_mot['texte'] == '\n':
                    pos_mot += 1
                    continue

                caractères_restants_dans_mot = len(données_mot['texte']) - données_mot['caractères_visibles']

                if caractères_restants_dans_mot > 0:
                    pos_prochain_caractère = données_mot['caractères_visibles']
                    données_mot['caractères_visibles'] += 1
                    caractères_restants_à_montrer -= 1
                    self.caractères_montrés += 1

                    if est_fin_de_phrase(données_mot['texte'], pos_prochain_caractère):
                        self.en_pause_de_fin_de_phrase = True
                        self.timer_pause = temps_actuel
                        break
                    elif données_mot['texte'][pos_prochain_caractère] == ',':
                        self.en_pause_de_virugle = True
                        self.timer_pause = temps_actuel
                        break

                if données_mot['caractères_visibles'] >= len(données_mot['texte']):
                    pos_mot += 1

        if self.caractères_montrés >= self.caractères_totaux:
            self.fini = True

    def draw(self):
        for données_mot in self.données_mots:
            if données_mot['texte'] == '\n':
                continue

            if données_mot['caractères_visibles'] > 0:
                texte_visible = données_mot['texte'][:données_mot['caractères_visibles']]
                surface_texte = self.font.render(texte_visible, True, self.couleur_texte)
                self.surface.blit(surface_texte, (données_mot['x'], données_mot['y']))

    def force_arrêt(self):
        for word_data in self.données_mots:
            if word_data['texte'] != '\n':
                word_data['caractères_visibles'] = len(word_data['texte'])

        self.caractères_montrés = self.caractères_totaux
        self.fini = True