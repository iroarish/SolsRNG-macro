from . import potions
from . import keyboard_listener 
from time import sleep

#ToDo no class for crafting potions yet just the macro for practice


def potion_batch(potion_list):
    potion_dict = {
        1 : potions.warp_potion,
        2 : potions.fortune_iii,
        3 : potions.warp_potion,
    }
    if potion_list:
        for potion in potion_list:
            if keyboard_listener.running:
                craft(potion_dict[potion].potion_name, potion_dict[potion].potion_button)
    else:
        print("Potion Batch is empty...")

def craft(potion_name, button_loc):
    print(f"Crafting Item...{potion_name}... Button Image located at {button_loc}")
    sleep(2)