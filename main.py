from typing import Dict

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


def display_stat(name: str):
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


def main():
    char["name"] = create_char()
    display_stat(char["name"])
    equip_item(items["iron_sword"], "sword")
    equip_item(items["wooden_shield"], "shield")
    display_stat(char["name"])


if __name__ == "__main__":
    main()
