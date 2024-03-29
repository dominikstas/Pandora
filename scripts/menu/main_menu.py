import pygame
import sys
import os

# Create a full path to the fonts folder -> bauhaus font (for all the tekst)
FONT_FOLDER = os.path.join("assets", "fonts", "bauhaus")

def main_menu(screen, SCREEN_WIDTH, SCREEN_HEIGHT):
    
    """
    Main menu function displaying buttons and handling events.
    
    Args:
        screen (pygame.Surface): The surface representing the game window.
        SCREEN_WIDTH (int): Width of the game window.
        SCREEN_HEIGHT (int): Height of the game window.
    """
    
    # Set up colors
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GRAY = (150, 150, 150)

    # Set up fonts
    title_font = pygame.font.Font(os.path.join(FONT_FOLDER, "bauhaus.ttf"), 72)
    button_font = pygame.font.Font(os.path.join(FONT_FOLDER, "bauhaus.ttf"), 36)

    # Set up button dimensions
    # Think about better designs than this
    button_width = 200
    button_height = 50
    button_margin = 20

    # Set up button positions
    new_game_button_rect = pygame.Rect((SCREEN_WIDTH - button_width) // 2, SCREEN_HEIGHT // 2 - button_height - button_margin, button_width, button_height)
    load_button_rect = pygame.Rect((SCREEN_WIDTH - button_width) // 2, SCREEN_HEIGHT // 2, button_width, button_height)
    options_button_rect = pygame.Rect((SCREEN_WIDTH - button_width) // 2, SCREEN_HEIGHT // 2 + button_height + button_margin, button_width, button_height)
    exit_button_rect = pygame.Rect(SCREEN_WIDTH - button_width - 20, SCREEN_HEIGHT - button_height - 20, button_width, button_height)

    # Set up initial button colors
    # Gray for now -> think about better color 
    new_game_color = GRAY
    load_color = GRAY
    options_color = GRAY
    exit_color = GRAY

    while True:
        # Event handling loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    sys.exit()

            if event.type == pygame.MOUSEMOTION:
                # Check if mouse is over the buttons
                if new_game_button_rect.collidepoint(event.pos):
                    new_game_color = WHITE
                    pygame.mouse.set_cursor(*pygame.cursors.tri_left)
                else:
                    new_game_color = GRAY

                if load_button_rect.collidepoint(event.pos):
                    load_color = WHITE
                    pygame.mouse.set_cursor(*pygame.cursors.tri_left)
                else:
                    load_color = GRAY

                if options_button_rect.collidepoint(event.pos):
                    options_color = WHITE
                    pygame.mouse.set_cursor(*pygame.cursors.tri_left)
                else:
                    options_color = GRAY

                if exit_button_rect.collidepoint(event.pos):
                    exit_color = WHITE
                    pygame.mouse.set_cursor(*pygame.cursors.tri_left)
                else:
                    exit_color = GRAY

            if event.type == pygame.MOUSEBUTTONDOWN:
                if exit_button_rect.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()

        # Background color
        screen.fill((100, 120, 50))

        # Render the title
        title_text = title_font.render("This is Pandora", True, BLACK)
        title_rect = title_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4))
        screen.blit(title_text, title_rect)

        # Render the buttons
        pygame.draw.rect(screen, new_game_color, new_game_button_rect)
        pygame.draw.rect(screen, load_color, load_button_rect)
        pygame.draw.rect(screen, options_color, options_button_rect)
        pygame.draw.rect(screen, exit_color, exit_button_rect)

        # Render buttons tekst
        new_game_text = button_font.render("New Game", True, BLACK)
        new_game_text_rect = new_game_text.get_rect(center=new_game_button_rect.center)
        screen.blit(new_game_text, new_game_text_rect)

        load_text = button_font.render("Continue", True, BLACK)
        load_text_rect = load_text.get_rect(center=load_button_rect.center)
        screen.blit(load_text, load_text_rect)

        options_text = button_font.render("Options", True, BLACK)
        options_text_rect = options_text.get_rect(center=options_button_rect.center)
        screen.blit(options_text, options_text_rect)

        exit_text = button_font.render("Exit", True, BLACK)
        exit_text_rect = exit_text.get_rect(center=exit_button_rect.center)
        screen.blit(exit_text, exit_text_rect)

        # Update the display
        pygame.display.flip()