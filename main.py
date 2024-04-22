import tkinter as tk
from tkinter import ttk
import subprocess
import pygame
import sys
import argparse
import scripts.menu.main_menu as menu
import scripts.menu.intro as intro

def get_resolution():
    # Defining the variable selected_resolution
    selected_resolution = None
    root = tk.Tk()
    root.title("Resolution Selection")
    root.geometry("400x200")

    # Label to prompt the user to select resolution
    label = ttk.Label(root, text="Select resolution:")
    label.pack(pady=10)

    # Combobox for selecting resolution
    resolutions = ["800x600", "1024x768", "1280x720", "1920x1080"]
    resolution_combobox = ttk.Combobox(root, values=resolutions, state="readonly")
    resolution_combobox.pack(pady=10)
    resolution_combobox.current(0)

    # Function to confirm selected resolution
    def confirm_resolution():
        # Using nonlocal to refer to a variable from an outer scope
        nonlocal selected_resolution  
        selected_resolution = resolution_combobox.get()
        root.destroy() 

    # Button to confirm selected resolution
    confirm_button = ttk.Button(root, text="Confirm", command=confirm_resolution)
    confirm_button.pack(pady=10)

    root.mainloop()
    
    # Create Pygame window with selected resolution
    SCREEN_WIDTH, SCREEN_HEIGHT = map(int, selected_resolution.split('x'))
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Pandora")
    
    return selected_resolution, screen  

def parse_arguments():
    # Create an argument parser for the Pandora Game
    parser = argparse.ArgumentParser(description="Pandora Game")
    
    parser.add_argument("--resolution", type=str, default="800x600", help="Screen resolution (e.g., 800x600)")
    # Parse the arguments
    return parser.parse_args()

def main(resolution, screen):
    # Extract screen resolution from the parsed arguments
    SCREEN_WIDTH, SCREEN_HEIGHT = map(int, resolution.split('x'))

    # Display the introduction screen
    intro.intro(screen, SCREEN_WIDTH, SCREEN_HEIGHT)
    # Display the main menu
    menu.main_menu(screen, SCREEN_WIDTH, SCREEN_HEIGHT)

if __name__ == "__main__":
    selected_resolution, screen = get_resolution()  
    main(selected_resolution, screen)  
