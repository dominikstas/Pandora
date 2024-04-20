import pygame
import sys
import scripts.menu.main_menu as menu
import scripts.menu.intro as intro
import argparse

def parse_arguments():
    # Create an argument parser for the Pandora Game
    parser = argparse.ArgumentParser(description="Pandora Game")
    # Add an argument for screen resolution with a default value of "800x600"
    parser.add_argument("--resolution", type=str, default="800x600", help="Screen resolution (e.g., 800x600)")
    # Parse the arguments
    return parser.parse_args()

def main():
    # Parse command-line arguments
    args = parse_arguments()

    # Extract screen resolution from the parsed arguments
    SCREEN_WIDTH, SCREEN_HEIGHT = map(int, args.resolution.split('x'))

    pygame.init()

    # Create the game window with the specified resolution
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Pandora")

    # Display the introduction screen
    intro.intro(screen, SCREEN_WIDTH, SCREEN_HEIGHT)
    # Display the main menu
    menu.main_menu(screen, SCREEN_WIDTH, SCREEN_HEIGHT)

if __name__ == "__main__":
    main()
