import sys
import os
import pygame

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
    
    # Set up colors
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GRAY = (150, 150, 150)

    # Set up font
    title_font = pygame.font.Font(os.path.join(FONT_FOLDER, "bauhaus.ttf"), int(SCREEN_HEIGHT * 0.06))
    button_font = pygame.font.Font(os.path.join(FONT_FOLDER, "bauhaus.ttf"), int(SCREEN_HEIGHT * 0.03))

    # Set up button dimensions and positions
    button_width = int(SCREEN_WIDTH * 0.2)
    button_height = int(SCREEN_HEIGHT * 0.08)
    button_margin = int(SCREEN_HEIGHT * 0.02)
    return_button_rect = pygame.Rect(int(SCREEN_WIDTH * 0.02), SCREEN_HEIGHT - button_height - int(SCREEN_HEIGHT * 0.02), button_width, button_height)
    volume_button_rect = pygame.Rect(SCREEN_WIDTH // 2 - button_width // 2, SCREEN_HEIGHT // 2 - button_height // 2, button_width, button_height)
    resolution_button_rect = pygame.Rect(SCREEN_WIDTH // 2 - button_width // 2, SCREEN_HEIGHT // 2 + button_height // 2 + button_margin, button_width, button_height)

    # Set up initial button colors
    return_color = GRAY
    volume_color = GRAY
    resolution_color = GRAY

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
                    return_color = WHITE
                else:
                    return_color = GRAY

                if volume_button_rect.collidepoint(event.pos):
                    volume_color = WHITE
                else:
                    volume_color = GRAY

                if resolution_button_rect.collidepoint(event.pos):
                    resolution_color = WHITE
                else:
                    resolution_color = GRAY

            if event.type == pygame.MOUSEBUTTONDOWN:
                if return_button_rect.collidepoint(event.pos):
                    return
                elif volume_button_rect.collidepoint(event.pos):
                    # to do
                    pass
                elif resolution_button_rect.collidepoint(event.pos):
                    # Open resolution menu
                    menu_open = not menu_open

            if menu_open and event.type == pygame.MOUSEBUTTONDOWN:
                for _, rect, resolution in resolution_buttons:
                    if rect.collidepoint(event.pos):
                        # Change resolution
                        pygame.display.set_mode(resolution)
                        menu_open = False
                        break

        # Background color
        screen.fill((100, 120, 50))

        # Render the title
        title_text = title_font.render("Options", True, BLACK)
        title_rect = title_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4))
        screen.blit(title_text, title_rect)

        # Render the buttons
        pygame.draw.rect(screen, return_color, return_button_rect)
        return_text = button_font.render("Return", True, BLACK)
        return_text_rect = return_text.get_rect(center=return_button_rect.center)
        screen.blit(return_text, return_text_rect)

        # In future: volume up and down
        pygame.draw.rect(screen, volume_color, volume_button_rect)
        volume_text = button_font.render("Volume", True, BLACK)
        volume_text_rect = volume_text.get_rect(center=volume_button_rect.center)
        screen.blit(volume_text, volume_text_rect)

        pygame.draw.rect(screen, resolution_color, resolution_button_rect)
        resolution_text = button_font.render("Change Resolution", True, BLACK)
        resolution_text_rect = resolution_text.get_rect(center=resolution_button_rect.center)
        screen.blit(resolution_text, resolution_text_rect)

        # Render resolution menu if open
        if menu_open:
            resolution_buttons.clear()
            menu_x = resolution_button_rect.left
            menu_y = resolution_button_rect.bottom + button_margin
            for text, width, height in resolution_options:
                resolution_text = button_font.render(text, True, BLACK)
                resolution_text_rect = resolution_text.get_rect(x=menu_x, y=menu_y)
                resolution_buttons.append((text, resolution_text_rect, (width, height)))
                menu_y += resolution_text_rect.height + button_margin
            for text, rect, _ in resolution_buttons:
                pygame.draw.rect(screen, WHITE, rect, 1)  # Draw button outlines
                screen.blit(button_font.render(text, True, BLACK), rect)

        # Update the display
        pygame.display.flip()
