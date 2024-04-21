import subprocess
import sys

# The purpose of this code is to take the resolution selected from the 
# tkinter window in set.py and pass it to the pygame menu in main.py

def main(resolution):
    process = subprocess.Popen(['python', 'main.py', '--resolution', resolution])
    process.wait() 
    sys.exit() 

if __name__ == "__main__":
    resolution = sys.argv[1] 
    main(resolution)
