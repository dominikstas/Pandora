import pygame
import sys

def main_menu(screen, SCREEN_WIDTH, SCREEN_HEIGHT):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    sys.exit()

        screen.fill((100, 120, 50))

        font = pygame.font.Font(None, 48)
        text = font.render("This is Pandora", True, (0, 0, 0))
        text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4))
        screen.blit(text, text_rect)

        font = pygame.font.Font(None, 36)
        text = font.render("Kliknij se spacje", True, (0, 0, 0))
        text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50))  # Przesunięcie o 50 pikseli niżej
        screen.blit(text, text_rect)
        
        pygame.display.flip()
