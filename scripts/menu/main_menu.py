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
    
    while True:
        # Event handling loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    sys.exit()

        '''
        to do in future
        
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Check if the mouse click occurred within the New Game button area
                if new_game_button_rect.collidepoint(event.pos):
                   
                # Check if the mouse click occurred within the Load button area
                if load_button_rect.collidepoint(event.pos):

                # Check if the mouse click occurred within the Options button area
                if options_button_rect.collidepoint(event.pos):
            '''        

        # Set background color
        screen.fill((100, 120, 50))

        # Render the title
        title_font = pygame.font.Font(os.path.join(FONT_FOLDER, "bauhaus.ttf"), 72)
        title_text = title_font.render("This is Pandora", True, (0, 0, 0))
        title_rect = title_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4))
        screen.blit(title_text, title_rect)

        # Render:
        
        # "Continue" button
        load_font = pygame.font.Font(os.path.join(FONT_FOLDER, "bauhaus.ttf"), 36)
        load_text = load_font.render("Continue", True, (0, 0, 0))
        load_button_rect = load_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        screen.blit(load_text, load_button_rect)

        # "New Game" button
        new_game_font = pygame.font.Font(os.path.join(FONT_FOLDER, "bauhaus.ttf"), 36)
        new_game_text = new_game_font.render("New Game", True, (0, 0, 0))
        new_game_button_rect = new_game_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50))
        screen.blit(new_game_text, new_game_button_rect)

        # "Options" button
        options_font = pygame.font.Font(os.path.join(FONT_FOLDER, "bauhaus.ttf"), 36)
        options_text = options_font.render("Options", True, (0, 0, 0))
        options_button_rect = options_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 100))
        screen.blit(options_text, options_button_rect)

        # Update the display
        pygame.display.flip()
