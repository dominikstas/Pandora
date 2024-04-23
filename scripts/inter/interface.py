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

def interface(screen, SCREEN_WIDTH, SCREEN_HEIGHT):
    """
    Game main interface
    
    Args:
        screen (pygame.Surface): The surface representing the game window.
        SCREEN_WIDTH (int): Width of the game window.
        SCREEN_HEIGHT (int): Height of the game window.
    """
   
    # Set up font and colors
    button_font = pygame.font.Font(os.path.join(FONT_FOLDER, "bauhaus.ttf"), int(SCREEN_HEIGHT * 0.03))

    BUTTON_COLOR = DARK_GREEN
    BUTTON_HOVER_COLOR = BLACK
    TEXT_COLOR = GRAY

    menu_rect = pygame.Rect(10, 10, 100, 40) 

    while True:
        # Event handling loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if menu_rect.collidepoint(event.pos):
                    # Open menu
                    small_menu(screen, SCREEN_WIDTH, SCREEN_HEIGHT)

        # Background color
        screen.fill(BLACK)

        # Draw menu button
        pygame.draw.rect(screen, BUTTON_COLOR, menu_rect)
        menu_text = button_font.render("Menu", True, TEXT_COLOR)
        menu_text_rect = menu_text.get_rect(center=menu_rect.center)
        screen.blit(menu_text, menu_text_rect)

        # Update the display
        pygame.display.flip()

def small_menu(screen, SCREEN_WIDTH, SCREEN_HEIGHT):
    """
    Small menu displayed in the center of the screen.
    
    Args:
        screen (pygame.Surface): The surface representing the game window.
        SCREEN_WIDTH (int): Width of the game window.
        SCREEN_HEIGHT (int): Height of the game window.
    """
    button_font = pygame.font.Font(os.path.join(FONT_FOLDER, "bauhaus.ttf"), int(SCREEN_HEIGHT * 0.03))

    BUTTON_COLOR = DARK_GREEN
    BUTTON_HOVER_COLOR = BLACK
    TEXT_COLOR = GRAY

     # Define small menu rectangle (redesign in future)
    menu_rect = pygame.Rect(SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 - 100, 200, 200) 

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    # Close menu
                    return
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if menu_rect.collidepoint(event.pos):
                    # Check if "Exit" button clicked
                    if menu_rect.collidepoint(event.pos):
                        pygame.quit()
                        sys.exit()

        # Background color
        screen.fill(BLACK)

        # Draw menu
        pygame.draw.rect(screen, BUTTON_COLOR, menu_rect)

        # Draw exit button
        exit_button_rect = pygame.Rect(menu_rect.centerx - 50, menu_rect.centery - 30, 100, 40)
        pygame.draw.rect(screen, BUTTON_COLOR, exit_button_rect)
        exit_text = button_font.render("Exit", True, TEXT_COLOR)
        exit_text_rect = exit_text.get_rect(center=exit_button_rect.center)
        screen.blit(exit_text, exit_text_rect)

        # Update the display
        pygame.display.flip()

def main():
    # Initialize pygame
    pygame.init()

    # Set up the screen
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Call the interface function
    interface(screen, SCREEN_WIDTH, SCREEN_HEIGHT)

    # Main loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

