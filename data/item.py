import csv
import sys
from typing import Dict

items = []


def get_item_list():
    """
    get all item list from
    the items.csv
    """
    with open("items.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            items.append(row)

    print(items)


def save_item(items: Dict):
    """
    save item that get dropped
    from monster
    """
    print(items)
    with open("items.csv", "a") as file:
        writer = csv.DictWriter(file, fieldnames=["name", "type", "effect"])
        writer.writerow(items)


command = {"get-item-list": get_item_list, "save-item": save_item}


def main():
    """
    run action from command line
    arguments
    """
    items_drop = {
        "name": "Attack Power Up",
        "type": "potion",
        "effect": "Increase Attack Power +10 for 10 Turn",
    }

    for arg in sys.argv[1:]:
        action = command.get(arg)
        if (arg == "save-item") and action:
            action(items_drop)
        elif action:
            action()
        else:
            raise ValueError(
                f"""
Command Error Invalid !!
========================
Command Available
{command.keys()}
"""
            )


main()
