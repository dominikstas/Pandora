import pygame
import sys
import os

# Create a full path to the fonts folder -> bauhaus font (for all the tekst)
FONT_FOLDER = os.path.join("assets", "fonts", "bauhaus")

def load_game_screen(screen, SCREEN_WIDTH, SCREEN_HEIGHT):
    """
    Load game screen function displaying buttons and handling events.
    
    Args:
        screen (pygame.Surface): The surface representing the game window.
        SCREEN_WIDTH (int): Width of the game window.
        SCREEN_HEIGHT (int): Height of the game window.
    """
    
    # Set up colors
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GRAY = (150, 150, 150)

    # Set up font
    title_font = pygame.font.Font(os.path.join(FONT_FOLDER, "bauhaus.ttf"), 72)
    button_font = pygame.font.Font(os.path.join(FONT_FOLDER, "bauhaus.ttf"), 36)

    # Set up button dimensions and positions
    button_width = 200
    button_height = 50
    button_margin = 20
    return_button_rect = pygame.Rect(20, SCREEN_HEIGHT - button_height - 20, button_width, button_height)

    # Set up initial button colors
    # Again, waiting for better design
    return_color = GRAY

    while True:
        # Event handling loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEMOTION:
                # Check if mouse is over the return button
                if return_button_rect.collidepoint(event.pos):
                    return_color = WHITE
                    pygame.mouse.set_cursor(*pygame.cursors.tri_left)
                else:
                    return_color = GRAY

            if event.type == pygame.MOUSEBUTTONDOWN:
                if return_button_rect.collidepoint(event.pos):
                    return

        # Background color
        screen.fill((100, 120, 50))

        # Render the title
        title_text = title_font.render("Load game", True, BLACK)
        title_rect = title_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4))
        screen.blit(title_text, title_rect)

        # Render the return button
        pygame.draw.rect(screen, return_color, return_button_rect)
        return_text = button_font.render("Return", True, BLACK)
        return_text_rect = return_text.get_rect(center=return_button_rect.center)
        screen.blit(return_text, return_text_rect)

        # Update the display
        pygame.display.flip()
