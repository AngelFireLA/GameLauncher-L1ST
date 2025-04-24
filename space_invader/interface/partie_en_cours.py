import pygame
import os
from ..moteur.partie import Partie
from ..utils import chemin_absolu_dossier
from . import menu_pause

MENU = 0
GAME = 1
GAME_OVER = 2

def main():
    pygame.init()

    screen_width, screen_height = 1024, 768
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Space Invader")
    clock = pygame.time.Clock()
    running = True

    state = MENU
    game = None

    menu_bg = pygame.image.load(chemin_absolu_dossier+"assets/images/background.jpg")
    menu_bg = pygame.transform.scale(menu_bg, (screen_width, screen_height))
    bg = pygame.image.load(chemin_absolu_dossier+"assets/images/bg1.png")
    bg = pygame.transform.scale(bg, (screen_width, screen_height))

    font_subtitle = pygame.font.Font(None, 50)
    font_title = pygame.font.Font(None, 80)
    font_small = pygame.font.Font(None, 36)

    while running:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if state == MENU:
                    if event.key == pygame.K_SPACE:
                        game = Partie(screen_width, screen_height)
                        state = GAME


                elif state == GAME_OVER:
                    if event.key == pygame.K_SPACE:
                        state = MENU
                elif state == GAME:
                    if event.key == pygame.K_ESCAPE:
                        running = menu_pause.main()
                        screen = pygame.display.set_mode((screen_width, screen_height))
                        state = GAME

        if state == MENU:
            screen.blit(menu_bg, (0, 0))
            start_text = font_subtitle.render("Appuyez sur Espace pour démarrer", True, (255, 215, 0))
            text_x = screen_width // 2 - start_text.get_width() // 2
            text_y = 600
            screen.blit(start_text, (text_x, text_y))

        elif state == GAME:
            screen.blit(bg, (0, 0))
            game.handle_input()
            game.update()
            if game.is_game_over():
                state = GAME_OVER
            game.draw(screen)

        elif state == GAME_OVER:
            screen.blit(menu_bg, (0, 0))

            title_text = font_title.render("GAME OVER", True, (255, 0, 0))
            screen.blit(
                title_text,
                (screen_width // 2 - title_text.get_width() // 2, 50)
            )

            final_score_text = font_small.render(f"Score final : {game.score}", True, (255, 255, 255))
            screen.blit(
                final_score_text,
                (screen_width // 2 - final_score_text.get_width() // 2, 120)
            )

            replay_text = font_small.render("Appuie sur Espace pour rejouer", True, (255, 255, 255))
            screen.blit(
                replay_text,
                (screen_width // 2 - replay_text.get_width() // 2, 190)
            )

        pygame.display.flip()


if __name__ == "__main__":
    main()
