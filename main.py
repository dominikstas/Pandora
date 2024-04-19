import pygame
import sys
import scripts.menu.main_menu as menu
import scripts.menu.intro as intro
import scripts.menu.options as options

class Game:
    def __init__(self, screen, width, height):
        self.screen = screen
        self.width = width
        self.height = height

def main():
    pygame.init()

    SCREEN_WIDTH = 1200
    SCREEN_HEIGHT = 600

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Pandora")

    game = Game(screen, SCREEN_WIDTH, SCREEN_HEIGHT)

    if __name__ == "__main__":
        intro.intro(game)
        menu.main_menu(game)


if __name__ == "__main__":
    main()
