import sys
from threading import Thread
from time import sleep
import keyboard
# Importing component/macro
from macro import crafting_macro

is_auto_craft = False
running = False

def crafting_potion():
    global running, is_auto_craft
    n = 1
    while (not is_auto_craft):
        if running and not is_auto_craft:
            print(f"Crafting Batch {n}...")
            crafting_macro.potion_batch([1, 2, 3])
            n += 1
            sleep(1)
        sleep(0.1)

def run_macro():
    global running, is_auto_craft
    while True:
        if keyboard.is_pressed('space'): 
            running = not running
            sleep(0.1)
        elif keyboard.is_pressed('ctrl+space'):
            running = False
            print("Ending Program")
            is_auto_craft = True
            sys.exit(1)

def main():
    Thread(target=run_macro).start()
    Thread(target=crafting_potion).start()