import pygame
import sys
import scripts.menu.main_menu as menu
import scripts.menu.intro as intro

pygame.init()

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pandora")

if __name__ == "__main__":
    intro.intro(screen, SCREEN_WIDTH, SCREEN_HEIGHT)
    menu.main_menu(screen, SCREEN_WIDTH, SCREEN_HEIGHT)
