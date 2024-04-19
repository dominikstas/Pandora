import pygame
import time
import os

# Create a full path to the fonts folder -> bauhaus font (for all the tekst)
FONT_FOLDER = os.path.join("assets", "fonts", "bauhaus")

def new_game(game):
    """
    New game screen function displaying an animation.

    Args:
        game (Game): The Game object representing the game.
    """

    # Set up font
    font = pygame.font.Font(os.path.join(FONT_FOLDER, "bauhaus.ttf"), int(game.height * 0.06))

    # Clear the screen
    game.screen.fill((0, 0, 0))
    pygame.display.flip()

    # Display the animation
    animation_text = font.render("Chapter 1 - Something", True, (20, 80, 20)) #Dark green    
    animation_rect = animation_text.get_rect(center=(game.width // 2, game.height // 2))
    game.screen.blit(animation_text, animation_rect)
    pygame.display.flip()

    # Wait for a few seconds
    pygame.time.wait(3000)
    
    game.screen.fill((0, 0, 0))  # Clear the screen
    animation_text = font.render("Here you can see", True, (255, 255, 255))
    animation_rect = animation_text.get_rect(center=(game.width // 2, game.height // 2))
    game.screen.blit(animation_text, animation_rect)
    pygame.display.flip()
    
    # Wait for a few seconds
    pygame.time.wait(2000)
    
    game.screen.fill((0, 0, 0))  # Clear the screen
    animation_text = font.render("i mean, not right now", True, (255, 255, 255))
    animation_rect = animation_text.get_rect(center=(game.width // 2, game.height // 2))
    game.screen.blit(animation_text, animation_rect)
    pygame.display.flip()

    # Wait for a few seconds
    pygame.time.wait(2000)

    game.screen.fill((0, 0, 0))  # Clear the screen
    animation_text = font.render("cool intro", True, (255, 255, 255))
    animation_rect = animation_text.get_rect(center=(game.width // 2, game.height // 2))
    game.screen.blit(animation_text, animation_rect)
    pygame.display.flip()
    
    pygame.time.wait(2000)
    
    game.screen.fill((0, 0, 0))  # Clear the screen
    animation_text = font.render("and now you can play", True, (255, 255, 255))
    animation_rect = animation_text.get_rect(center=(game.width // 2, game.height // 2))
    game.screen.blit(animation_text, animation_rect)
    pygame.display.flip()

    # Wait for a few seconds
    pygame.time.wait(2000)

    # Add the logic to start the actual game
