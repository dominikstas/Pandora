import sys
import os
import pygame

# Set up colors
DARK_GREEN = (20, 80, 20)
BORDO = (128, 0, 32)
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)

# Create a full path to the fonts folder -> bauhaus font (for all the tekst)
FONT_FOLDER = os.path.join("assets", "fonts", "bauhaus")

def load_game_screen(screen, SCREEN_WIDTH, SCREEN_HEIGHT):
    """
    Continue game screen function displaying buttons and handling events.
    
    Args:
        screen (pygame.Surface): The surface representing the game window.
        SCREEN_WIDTH (int): Width of the game window.
        SCREEN_HEIGHT (int): Height of the game window.
    """
   
    # Set up font and colors
    title_font = pygame.font.Font(os.path.join(FONT_FOLDER, "bauhaus.ttf"), int(SCREEN_HEIGHT * 0.06))
    button_font = pygame.font.Font(os.path.join(FONT_FOLDER, "bauhaus.ttf"), int(SCREEN_HEIGHT * 0.03))

    BUTTON_COLOR = DARK_GREEN
    BUTTON_HOVER_COLOR = BLACK
    TEXT_COLOR = GRAY

    # Set up button dimensions and positions
    button_width = int(SCREEN_WIDTH * 0.2)
    button_height = int(SCREEN_HEIGHT * 0.08)
    button_margin = int(SCREEN_HEIGHT * 0.02)
    return_button_rect = pygame.Rect(int(SCREEN_WIDTH * 0.02), SCREEN_HEIGHT - button_height - int(SCREEN_HEIGHT * 0.02), button_width, button_height)

    # Set up initial button colors
    return_color = BUTTON_COLOR

    while True:
        # Event handling loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEMOTION:
                # Check if mouse is over the buttons
                if return_button_rect.collidepoint(event.pos):
                    return_color = BUTTON_HOVER_COLOR
                else:
                    return_color = BUTTON_COLOR

            if event.type == pygame.MOUSEBUTTONDOWN:
                if return_button_rect.collidepoint(event.pos):
                    return

        # Background color
        screen.fill(BLACK)

        # Render the title
        title_text = title_font.render("Load game", True, GRAY)
        title_rect = title_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4))
        screen.blit(title_text, title_rect)

        # Render the buttons
        pygame.draw.rect(screen, return_color, return_button_rect)
        return_text = button_font.render("Return", True, GRAY)
        return_text_rect = return_text.get_rect(center=return_button_rect.center)
        screen.blit(return_text, return_text_rect)

        # Update the display
        pygame.display.flip()

