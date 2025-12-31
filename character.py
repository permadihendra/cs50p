from typing import override


class Stat:
    def __init__(self, health: int, attack: int, defend: int, agility: int):
        self.health: int = health
        self.attack: int = attack
        self.defend: int = defend
        self.agility: int = agility

class Item(Stat):
    def __init__(self, id:int, name: str, type: str, 
                 health: int=0, attack: int=0, defend: int=0, agility: int=0):
        super().__init__(health, attack, defend, agility)
        self.id: int = id
        self.name: str = name
        self.type: str = type

class Character(Stat):
    
    def __init__(
        self, id: int, name: str, health: int, attack: int, defend: int, agility: int
    ):
        super().__init__(health, attack, defend, agility)
        self.id: int = id
        self.name: str = name
        # already defined in Stat
        #self.health: int = health
        #self.attack: int = attack
        #self.defend: int = defend 
        #self.agility: int = agility 
        self.inventory: list[Item] = [ ]
        self.equipment: dict[str, bool] = {"sword": False, "shield": False}
        self.equipment_list: list[Item] = []


    def equip_item(self, item:Item)-> None:
        if self.equipment[item.type] is True :
            print(f"Item '{item.type}' already equiped")
            return
        elif item not in self.inventory:
            print(f"Item '{item.name}' not found in inventory")
            return
        else:
            self.health += item.health
            self.attack += item.attack
            self.defend += item.defend
            self.agility += item.agility
            self.inventory.remove(item)
            self.equipment[item.type] = True
            self.equipment_list.append(item)
            print(f"Successfull equip: {item.name} !") 

    def equip_remove(self, item:Item)-> None:
        if item not in self.equipment_list:
            print(f"Item '{item.name}' not equiped")
            return
        elif self.equipment[item.type] is False:
            print(f"No '{item.type}' is equiped")
            return
        else:
            # Remove stats
            self.health -= item.health
            self.attack -= item.attack
            self.defend -= item.defend
            self.agility -= item.agility

            # Clear Equipemnt
            self.equipment_list.remove(item)
            self.inventory.append(item)
            self.equipment[item.type] = False
            print(f"Successfully remove '{item.name}' !")
            return

    def save_item(self, item: Item):
        self.inventory.append(item)
   
    @override
    def __str__(self) -> str:
        return (
f"""
=========================
CHARACTER INFO
=========================
ID   : {self.id}
NAME : {self.name}
-------------------------
STATS
-------------------------
Health  : {self.health}
Attack  : {self.attack}
Defend  : {self.defend}
Agility : {self.agility}
-------------------------
EQUIPPED
-------------------------
{[item.name for item in self.equipment_list]}
-------------------------
INVENTORY
-------------------------
{[item.name for item in self.inventory]}

        """)

def main():
    char = Character(1, "Joni", 100, 35, 30, 20)
    char2 = Character(2, "Hongki", 100, 20,20,10)
    sword = Item(id=1, name="Long Sword", type="sword", attack=10)
    shield = Item(id=1, name="Iron Shield", type="shield", defend=15)
    
    char.save_item(sword)
    char.save_item(shield)

    char.equip_item(sword) 
    char.equip_item(shield)

    print(char)

    char.equip_item(shield)

    char.equip_remove(shield)

    print(char)

    print(char2)


if __name__ == "__main__":
    main()
