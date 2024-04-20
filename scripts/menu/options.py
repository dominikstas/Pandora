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

def options_screen(screen, SCREEN_WIDTH, SCREEN_HEIGHT):
    """
    Options screen function displaying buttons and handling events.
    
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
    volume_button_rect = pygame.Rect(SCREEN_WIDTH // 2 - button_width // 2, SCREEN_HEIGHT // 2 - button_height // 2, button_width, button_height)
    resolution_button_rect = pygame.Rect(SCREEN_WIDTH // 2 - button_width // 2, SCREEN_HEIGHT // 2 + button_height // 2 + button_margin, button_width, button_height)

    # Set up initial button colors
    return_color = BUTTON_COLOR
    volume_color = BUTTON_COLOR
    resolution_color = BUTTON_COLOR

    # Resolution options
    resolution_options = [("800x600", 800, 600), ("1200x600", 1200, 600), ("1280x720", 1280, 720), ("1536x864", 1536, 864), ("1920x1080", 1920, 1080)]
    resolution_buttons = []
    menu_open = False

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

                if volume_button_rect.collidepoint(event.pos):
                    volume_color = BUTTON_HOVER_COLOR
                else:
                    volume_color = BUTTON_COLOR

                if resolution_button_rect.collidepoint(event.pos):
                    resolution_color = BUTTON_HOVER_COLOR
                else:
                    resolution_color = BUTTON_COLOR

            if event.type == pygame.MOUSEBUTTONDOWN:
                if return_button_rect.collidepoint(event.pos):
                    return
                elif volume_button_rect.collidepoint(event.pos):
                    # to do
                    pass
               

        # Background color
        screen.fill(BLACK)

        # Render the title
        title_text = title_font.render("Options", True, GRAY)
        title_rect = title_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4))
        screen.blit(title_text, title_rect)

        # Render the buttons
        pygame.draw.rect(screen, return_color, return_button_rect)
        return_text = button_font.render("Return", True, GRAY)
        return_text_rect = return_text.get_rect(center=return_button_rect.center)
        screen.blit(return_text, return_text_rect)

        # In future: volume up and down
        pygame.draw.rect(screen, volume_color, volume_button_rect)
        volume_text = button_font.render("Volume", True, GRAY)
        volume_text_rect = volume_text.get_rect(center=volume_button_rect.center)
        screen.blit(volume_text, volume_text_rect)

        # Update the display
        pygame.display.flip()

