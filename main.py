import os
import subprocess
import time
from typing import Dict

GAME_PLAY: bool = True

char = {
    "name": "New Player",
    "stats": {
        "hp": 100,
        "atp": 20,
        "def": 10,
        "agi": 10,
    },
    "sword": None,
    "shield": None,
    "equiped_sword": False,
    "equiped_shield": False,
}

items = {
    "iron_sword": {
        "type": "sword",
        "name": "Iron Sword",
        "atp": 5,
        "def": 0,
        "agi": 3,
    },
    "wooden_shield": {
        "type": "shield",
        "name": "Wooden Shield",
        "atp": 0,
        "def": 5,
        "hp": 10,
    },
}


def create_char() -> str:
    name = input("Enter Character Name : ")
    return name


def equip_item(item: Dict, type: str):
    # Add the item bonus stats
    try:
        if type == "sword":
            char["sword"] = item
        elif type == "shield":
            char["shield"] = item
        for stat, value in item.items():
            if stat in char["stats"]:
                char["stats"][stat] += value
        print(f"Equip *{item['name']}* success!")
    except ValueError:
        print("Equip item failed!")


def equip_item_set():
    equip_item(items["iron_sword"], "sword")
    equip_item(items["wooden_shield"], "shield")
    time.sleep(1)
    print("back to menu ...")
    time.sleep(2)
    back_to_menu()


def display_stat():
    clear_screen()
    print(
        f"""
Character Name : {char["name"]}
====================================
Stats :
HP: {char["stats"]["hp"]} ATP: {char["stats"]["atp"]} DEF: {char["stats"]["def"]} AGI: {char["stats"]["agi"]}
-------
Items :
Sword : {char["sword"]}
Shield : {char["shield"]}
"""
    )
    time.sleep(1)
    print("back to menu ...")
    time.sleep(2)
    back_to_menu()


def clear_screen():
    if os.name == "nt":
        # Use subprocess for better practice on modern Windows
        subprocess.run("cls", shell=True)
    else:
        # Use subprocess for better practice on Unix/Linux/macOS
        subprocess.run("clear", shell=True)


def back_to_menu():
    clear_screen()
    display_menu(char["name"], menu_display)
    choice = int(input("What sould you like to do? "))
    select_action(menu_action, choice)


def stop_game():
    global GAME_PLAY
    GAME_PLAY = False


def exit():
    clear_screen()
    print("Thank you for playing")
    time.sleep(1)
    print("Exiting Game ...")
    time.sleep(1)
    print("...")
    stop_game()


# Game Menu - Action
menu_action = {
    1: display_stat,
    2: equip_item_set,
    9: exit,
    0: back_to_menu,
}

menu_display = {
    "1": "Show Stats",
    "2": "Equip Item Set",
    "9": "Exit Game",
    "0": "back to menu",
}


def display_menu(name: str, menu_display: Dict):
    clear_screen()
    print(
        f"""
Welcome to the wonderful Journey : {name} !
====================================
Please Select Action Menu:"""
    )
    for key, value in menu_display.items():
        print(f"[{key}] -> {value}")


## cs50 implement raise exception
def select_action(menu_action: Dict, choice: int):
    action = menu_action.get(choice)

    if action:
        action()
    else:
        raise ValueError("Invalid Action")


def main():
    # Create Char Name
    char["name"] = create_char()

    display_menu(char["name"], menu_display)
    choice = int(input("What sould you like to do? "))
    select_action(menu_action, choice)


if __name__ == "__main__":
    while GAME_PLAY:
        # print(GAME_PLAY)
        main()
