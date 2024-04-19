import pygame
import time
import os

# Create a full path to the fonts folder -> bauhaus font (for all the tekst)
FONT_FOLDER = os.path.join("assets", "fonts", "bauhaus")

class Game:
    def __init__(self, screen, width, height):
        self.screen = screen
        self.width = width
        self.height = height

def intro(game):
    """
    intro function displaying an animation.

    Args:
        game (Game): The Game object representing the game.
    """

    # Set up font
    font = pygame.font.Font(os.path.join(FONT_FOLDER, "bauhaus.ttf"), int(game.height * 0.06))

    # Clear the screen
    game.screen.fill((0, 0, 0))
    pygame.display.flip()

    # Display the animation
    animation_text = font.render("Welcome", True, (255, 255, 255))
    animation_rect = animation_text.get_rect(center=(game.width // 2, game.height // 2))
    game.screen.blit(animation_text, animation_rect)
    pygame.display.flip()

    # Wait for a few seconds
    pygame.time.wait(1000)
    
    game.screen.fill((0, 0, 0))  # Clear the screen
    animation_text = font.render("to", True, (255, 255, 255))
    animation_rect = animation_text.get_rect(center=(game.width // 2, game.height // 2))
    game.screen.blit(animation_text, animation_rect)
    pygame.display.flip()

    # Wait for a few seconds
    pygame.time.wait(1000)

    # Display "Pandora"
    game.screen.fill((0, 0, 0)) 
    pandora_text = font.render("Pandora", True, (20, 80, 20)) #Dark green
    pandora_text = pygame.transform.scale(pandora_text, (pandora_text.get_width() * 2, pandora_text.get_height() * 2))
    pandora_rect = pandora_text.get_rect(center=(game.width // 2, game.height // 2))
    game.screen.blit(pandora_text, pandora_rect)
    pygame.display.flip()

    # Wait for a few seconds
    pygame.time.wait(2000)
