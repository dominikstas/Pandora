#this aint working :D (yet)



import scripts.menu.options as options
import scripts.menu.load_game as load_game
import scripts.menu.new_game as new_game

import pygame
import sys
import os

# Set up colors
DARK_GREEN = (20, 80, 20)
BORDO = (128, 0, 32)
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)


# Create a full path to the fonts folder -> bauhaus font (for all the tekst)
FONT_FOLDER = os.path.join("assets", "fonts", "bauhaus")

def main_menu(game):
    """
    Main menu function displaying buttons and handling events.
    
    Args:
        game (Game): The Game object containing the screen and dimensions.
    """
    screen = game.screen
    SCREEN_WIDTH = game.width
    SCREEN_HEIGHT = game.height
    
    
    # Set up fonts
    title_font = pygame.font.Font(os.path.join(FONT_FOLDER, "bauhaus.ttf"), int(SCREEN_HEIGHT * 0.06))
    button_font = pygame.font.Font(os.path.join(FONT_FOLDER, "bauhaus.ttf"), int(SCREEN_HEIGHT * 0.03))
    
    # Set up buttons
    button_width = int(SCREEN_WIDTH * 0.25)
    button_height = int(SCREEN_HEIGHT * 0.1)
    button_margin = int(SCREEN_HEIGHT * 0.05)

    new_game_button_rect = pygame.Rect((SCREEN_WIDTH - button_width) // 2, SCREEN_HEIGHT // 2 - button_height - button_margin, button_width, button_height)
    load_button_rect = pygame.Rect((SCREEN_WIDTH - button_width) // 2, SCREEN_HEIGHT // 2, button_width, button_height)
    options_button_rect = pygame.Rect((SCREEN_WIDTH - button_width) // 2, SCREEN_HEIGHT // 2 + button_height + button_margin, button_width, button_height)
    exit_button_rect = pygame.Rect((SCREEN_WIDTH - button_width) // 2, SCREEN_HEIGHT // 2 + 2 * button_height + 2 * button_margin, button_width, button_height)

    new_game_color = DARK_GREEN
    load_color = DARK_GREEN
    options_color = DARK_GREEN
    exit_color = BORDO

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEMOTION:
                # Change button colors on mouse hover
                if new_game_button_rect.collidepoint(event.pos):
                    new_game_color = BLACK
                else:
                    new_game_color = DARK_GREEN

                if load_button_rect.collidepoint(event.pos):
                    load_color = BLACK
                else:
                    load_color = DARK_GREEN

                if options_button_rect.collidepoint(event.pos):
                    options_color = BLACK
                else:
                    options_color = DARK_GREEN

                if exit_button_rect.collidepoint(event.pos):
                    exit_color = BLACK
                else:
                    exit_color = BORDO

        if event.type == pygame.MOUSEBUTTONDOWN:
            if load_button_rect.collidepoint(event.pos):
                load_game.load_game_screen(game)
        elif options_button_rect.collidepoint(event.pos):
            options.options_screen(game)
        elif exit_button_rect.collidepoint(event.pos):
            pygame.quit()
            sys.exit()
        elif new_game_button_rect.collidepoint(event.pos):
            new_game.new_game(game)

        # Fill background
        screen.fill(BLACK)

        # Render buttons
        pygame.draw.rect(screen, new_game_color, new_game_button_rect, border_radius=10)
        pygame.draw.rect(screen, load_color, load_button_rect, border_radius=10)
        pygame.draw.rect(screen, options_color, options_button_rect, border_radius=10)
        pygame.draw.rect(screen, exit_color, exit_button_rect, border_radius=10)

        # Render button texts
        new_game_text = button_font.render("New Game", True, GRAY)
        new_game_text_rect = new_game_text.get_rect(center=new_game_button_rect.center)
        screen.blit(new_game_text, new_game_text_rect)

        load_text = button_font.render("Continue", True, GRAY)
        load_text_rect = load_text.get_rect(center=load_button_rect.center)
        screen.blit(load_text, load_text_rect)

        options_text = button_font.render("Options", True, GRAY)
        options_text_rect = options_text.get_rect(center=options_button_rect.center)
        screen.blit(options_text, options_text_rect)

        exit_text = button_font.render("Exit", True, GRAY)
        exit_text_rect = exit_text.get_rect(center=exit_button_rect.center)
        screen.blit(exit_text, exit_text_rect)

        # Renderowanie title
        title_text = title_font.render("This is Pandora", True, GRAY)
        title_rect = title_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4))
        screen.blit(title_text, title_rect)

        pygame.display.flip()

