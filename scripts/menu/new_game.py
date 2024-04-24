import pygame
import time
import os
import sys
import scripts.inter.interface as interface

# Create a full path to the fonts folder -> bauhaus font (for all the tekst)
FONT_FOLDER = os.path.join("assets", "fonts", "bauhaus")

def new_game(screen, SCREEN_WIDTH, SCREEN_HEIGHT):
    # Set up font
    font = pygame.font.Font(os.path.join(FONT_FOLDER, "bauhaus.ttf"), int(SCREEN_HEIGHT * 0.06))

    # Clear the screen
    screen.fill((0, 0, 0))
    pygame.display.flip()

    # Display the animation
    animation_texts = [
        " ",
        "Chapter 1 - Something",
        "Here you can see",
        "i mean, not right now",
        "cool intro",
        "and now you can play"
    ]
    animation_delays = [1000, 3000, 2000, 2000, 2000, 2000]  # Delays in milliseconds between each text

    intro_done = False
    current_text_index = 0
    start_time = pygame.time.get_ticks()

    while not intro_done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    intro_done = True

        current_time = pygame.time.get_ticks()
        if current_time - start_time >= animation_delays[current_text_index]:
            current_text_index += 1
            if current_text_index >= len(animation_texts):
                intro_done = True
            else:
                start_time = current_time
                screen.fill((0, 0, 0))
                animation_text = font.render(animation_texts[current_text_index], True, (255, 255, 255))
                animation_rect = animation_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
                screen.blit(animation_text, animation_rect)
                pygame.display.flip()

    # Launch the interface
    interface.interface(screen, SCREEN_WIDTH, SCREEN_HEIGHT)