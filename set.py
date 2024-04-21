import tkinter as tk
from tkinter import ttk
import subprocess

def get_resolution():
    # Defining the variable selected_resolution
    selected_resolution = None
    root = tk.Tk()
    root.title("Resolution Selection")
    root.geometry("400x200")

    label = ttk.Label(root, text="Select resolution:")
    label.pack(pady=10)

    resolutions = ["800x600", "1024x768", "1280x720", "1920x1080"]
    resolution_combobox = ttk.Combobox(root, values=resolutions, state="readonly")
    resolution_combobox.pack(pady=10)
    resolution_combobox.current(0)

    def confirm_resolution():
        # Using nonlocal to refer to a variable from an outer scope
        nonlocal selected_resolution  
        selected_resolution = resolution_combobox.get()
        root.destroy() 

    confirm_button = ttk.Button(root, text="Confirm", command=confirm_resolution)
    confirm_button.pack(pady=10)

    root.mainloop()
    return selected_resolution


def main():
    resolution = get_resolution()
    subprocess.Popen(['python', 'start.py', resolution])

if __name__ == "__main__":
    main()
