# to do: fix closing window

import tkinter as tk
from tkinter import ttk
import subprocess

import tkinter as tk
from tkinter import ttk
import subprocess

def run_main_with_resolution(resolution):
    # Creating a command to run the main.py script with the specified resolution
    command = ['python', 'main.py', '--resolution', resolution]
    subprocess.run(command)

def start_game():
    # Getting the selected resolution
    selected_resolution = resolution_combobox.get()
    # Running the main.py script with the selected resolution
    run_main_with_resolution(selected_resolution)
    # Closing the window after a short delay
    root.after(100, root.destroy)

# Creating the main window
root = tk.Tk()
root.title("Resolution Selection")

# Setting the window size
root.geometry("400x200")

# Adding a label
label = ttk.Label(root, text="Select resolution:")
label.pack(pady=10)

# Available resolutions
resolutions = ["800x600", "1024x768", "1280x720", "1920x1080"]

# Creating a drop-down list with available resolutions
resolution_combobox = ttk.Combobox(root, values=resolutions, state="readonly")
resolution_combobox.pack(pady=10)
resolution_combobox.current(0)  # Setting the default value

# Creating a button to start the game
start_button = ttk.Button(root, text="Start Game", command=start_game)
start_button.pack(pady=10)

# Running the main program loop
root.mainloop()

