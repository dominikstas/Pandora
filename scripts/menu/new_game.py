import pygame
import time
import os
import scripts.inter.interface as interface

# Create a full path to the fonts folder -> bauhaus font (for all the tekst)
FONT_FOLDER = os.path.join("assets", "fonts", "bauhaus")

def new_game(screen, SCREEN_WIDTH, SCREEN_HEIGHT):
    """
    New game screen function displaying an animation.

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
    animation_text = font.render("Chapter 1 - Something", True, (20, 80, 20)) #Dark green    
    animation_rect = animation_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
    screen.blit(animation_text, animation_rect)
    pygame.display.flip()

    # Wait for a few seconds
    pygame.time.wait(3000)
    
    screen.fill((0, 0, 0))  # Clear the screen
    animation_text = font.render("Here you can see", True, (255, 255, 255))
    animation_rect = animation_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
    screen.blit(animation_text, animation_rect)
    pygame.display.flip()
    
    # Wait for a few seconds
    pygame.time.wait(2000)
    
    screen.fill((0, 0, 0))  # Clear the screen
    animation_text = font.render("i mean, not right now", True, (255, 255, 255))
    animation_rect = animation_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
    screen.blit(animation_text, animation_rect)
    pygame.display.flip()

    # Wait for a few seconds
    pygame.time.wait(2000)

    screen.fill((0, 0, 0))  # Clear the screen
    animation_text = font.render("cool intro", True, (255, 255, 255))
    animation_rect = animation_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
    screen.blit(animation_text, animation_rect)
    pygame.display.flip()
    
    pygame.time.wait(2000)
    
    screen.fill((0, 0, 0))  # Clear the screen
    animation_text = font.render("and now you can play", True, (255, 255, 255))
    animation_rect = animation_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
    screen.blit(animation_text, animation_rect)
    pygame.display.flip()

    # Wait for a few seconds
    pygame.time.wait(2000)

    interface.interface(screen, SCREEN_WIDTH, SCREEN_HEIGHT)
