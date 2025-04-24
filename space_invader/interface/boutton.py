import pygame
from ..utils import dict_couleurs

class Boutton:
    def __init__(self, x, y, largeur, hauteur, texte, couleur, couleur_surlignee=None, couleur_texte=(255,255,255)):
        self.x = x - largeur//2
        self.y = y - hauteur//2
        self.largeur = largeur
        self.hauteur = hauteur
        self.rect = pygame.Rect(self.x, self.y, largeur, hauteur)
        self.texte = texte
        self.couleur = couleur
        self.couleur_surlignee = couleur_surlignee if couleur_surlignee else dict_couleurs.get("bleu", couleur)
        self.couleur_texte = couleur_texte
        self.radius = hauteur//2
        self.font = pygame.font.SysFont(None, int(hauteur*0.8))

    def est_clique(self):
        if pygame.mouse.get_pressed()[0] and self.rect.collidepoint(pygame.mouse.get_pos()):
            return True
        return False

    def afficher(self, screen):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            color = self.couleur_surlignee
        else:
            color = self.couleur
        pygame.draw.rect(screen, color, self.rect, border_radius=self.radius)
        pygame.draw.rect(screen, (0,0,0), self.rect, width=2, border_radius=self.radius)
        texte_surf = self.font.render(self.texte, True, self.couleur_texte)
        trect = texte_surf.get_rect(center=self.rect.center)
        screen.blit(texte_surf, trect)