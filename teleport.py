import os
import importlib.util
import pygame

def find_scene(scene_folder, scene_name):
    """
    Finds and imports the specified scene module.

    Args:
        scene_folder (str): Path to the folder containing scene modules.
        scene_name (str): Name of the scene module without extension.

    Returns:
        module: Imported scene module.
    """
    scene_path = os.path.join(scene_folder, scene_name + ".py")
    if os.path.exists(scene_path):
        spec = importlib.util.spec_from_file_location(scene_name, scene_path)
        scene_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(scene_module)
        return scene_module
    else:
        raise FileNotFoundError(f"Scene '{scene_name}' not found in folder '{scene_folder}'.")

def main():
    # Set resolution
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600

    # Initialize pygame
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Path to the folder containing scene modules
    scenes_folder = os.path.join("scripts", "inter")

    # Find and import the specified scene module
    try:
        scene_module = find_scene(scenes_folder, "interface")
    except FileNotFoundError as e:
        print(e)
        return

    # Call the main function of the scene module
    scene_module.interface(screen, SCREEN_WIDTH, SCREEN_HEIGHT)

if __name__ == "__main__":
    main()
