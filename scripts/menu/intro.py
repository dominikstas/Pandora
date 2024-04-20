import pygame
import time
import os

# Create a full path to the fonts folder -> bauhaus font (for all the tekst)
FONT_FOLDER = os.path.join("assets", "fonts", "bauhaus")

def intro(screen, SCREEN_WIDTH, SCREEN_HEIGHT):
    """
    intro function displaying an animation.

    Args:
        screen (pygame.Surface): The surface representing the game window.
        SCREEN_WIDTH (int): Width of the game window.
        SCREEN_HEIGHT (int): Height of the game window.
    """

    # Set up font
    font = pygame.font.Font(os.path.join(FONT_FOLDER, "bauhaus.ttf"), int(SCREEN_HEIGHT * 0.06))

    # Clear the screen
    screen.fill((0, 0, 0))
    pygame.display.flip()

    # Display the animation
    animation_text = font.render("Welcome", True, (255, 255, 255))
    animation_rect = animation_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
    screen.blit(animation_text, animation_rect)
    pygame.display.flip()

    # Wait for a few seconds
    pygame.time.wait(1000)
    
    screen.fill((0, 0, 0))  # Clear the screen
    animation_text = font.render("to", True, (255, 255, 255))
    animation_rect = animation_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
    screen.blit(animation_text, animation_rect)
    pygame.display.flip()

    # Wait for a few seconds
    pygame.time.wait(1000)

    # Display "Pandora"
    screen.fill((0, 0, 0)) 
    pandora_text = font.render("Pandora", True, (20, 80, 20)) #Dark green
    pandora_text = pygame.transform.scale(pandora_text, (pandora_text.get_width() * 2, pandora_text.get_height() * 2))
    pandora_rect = pandora_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
    screen.blit(pandora_text, pandora_rect)
    pygame.display.flip()


    # Wait for a few seconds
    pygame.time.wait(2000)

