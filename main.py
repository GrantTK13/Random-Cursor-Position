import pyautogui
import random

pyautogui.moveTo(random.randrange(0, 1919), random.randrange(0, 1079))
print("Type the word 'new' in the command line to send your mouse to a random position.")
while True:
    if input() == "new":
        pyautogui.moveTo(random.randrange(0, 1919), random.randrange(0, 1079))
