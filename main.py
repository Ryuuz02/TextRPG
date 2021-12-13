# Import statements
from random import choice


# Class for all moving beings (from enemies to the player to the npcs)
class being:
    def __init__(self, health, armor, evasion, attack, mana, speed):
        # Basic stats
        self.health = health
        self.armor = armor
        self.attack = attack
        self.evasion = evasion
        self.mana = mana
        self.equipment_lst = []
        self.speed = speed

    # Adds the stats of a gear if one of that type is not already equipped
    def equip_gear(self, equipped_gear):
        if self.check_unique(equipped_gear):
            self.equipment_lst.append(equipped_gear)
            self.health += equipped_gear.health
            self.armor += equipped_gear.armor
            self.attack += equipped_gear.attack
            self.evasion += equipped_gear.evasion
            self.mana += equipped_gear.mana
            self.speed += equipped_gear.speed

    # Removes the stats of a gear
    def unequip_gear(self, unequipped_gear):
        self.equipment_lst.pop(unequipped_gear)
        self.health -= unequipped_gear.health
        self.armor -= unequipped_gear.armor
        self.attack -= unequipped_gear.attack
        self.evasion -= unequipped_gear.evasion
        self.mana -= unequipped_gear.mana
        self.speed -= unequipped_gear.speed

    # Checks to see if the being is already wearing equipment of that type
    def check_unique(self, new_gear):
        equip_type_lst = []
        for i in range(0, len(self.equipment_lst)):
            equip_type_lst.append(type(self.equipment_lst[i]))
        if type(new_gear) in equip_type_lst:
            # If yes, returns false
            return False
        else:
            # Else, returns True
            return True


# The player character class
class player(being):
    def __init__(self, health, armor, evasion, attack, mana, speed):
        super().__init__(health, armor, evasion, attack, mana, speed)


# Class for all enemies
class enemy(being):
    def __init__(self, health, armor, evasion, attack, mana, speed, name):
        super().__init__(health, armor, evasion, attack, mana, speed)
        self.name = name


# Master list of all equipment
all_equipment_lst = []


# Parent class for all equipment, have the stats of the gear
class gear:
    def __init__(self, health, armor, evasion, attack, mana, speed, name):
        self.health = health
        self.armor = armor
        self.attack = attack
        self.evasion = evasion
        self.mana = mana
        self.speed = speed
        self.name = name
        # Adds itself to all_equipment_lst
        all_equipment_lst.append(self)


# Helmet equipment
class helmet(gear):
    def __init__(self, health, armor, evasion, attack, mana, speed, name):
        super().__init__(health, armor, evasion, attack, mana, speed, name)
        self.piece = "Helmet"


# Chest equipment
class chest(gear):
    def __init__(self, health, armor, evasion, attack, mana, speed, name):
        super().__init__(health, armor, evasion, attack, mana, speed, name)
        self.piece = "Chest"


# Hands equipment
class hands(gear):
    def __init__(self, health, armor, evasion, attack, mana, speed, name):
        super().__init__(health, armor, evasion, attack, mana, speed, name)
        self.piece = "Hands"


# Arms equipment
class arms(gear):
    def __init__(self, health, armor, evasion, attack, mana, speed, name):
        super().__init__(health, armor, evasion, attack, mana, speed, name)
        self.piece = "Arms"


# Legs equipment
class legs(gear):
    def __init__(self, health, armor, evasion, attack, mana, speed, name):
        super().__init__(health, armor, evasion, attack, mana, speed, name)
        self.piece = "Legs"


# Feet equipment
class feet(gear):
    def __init__(self, health, armor, evasion, attack, mana, speed, name):
        super().__init__(health, armor, evasion, attack, mana, speed, name)
        self.piece = "Feet"


# Two handed weapons
class two_hand(gear):
    def __init__(self, health, armor, evasion, attack, mana, speed, name):
        super().__init__(health, armor, evasion, attack, mana, speed, name)
        self.piece = "Two Hand Weapon"


# Off hand gear (shields, torches, etc.)
class off_hand(gear):
    def __init__(self, health, armor, evasion, attack, mana, speed, name):
        super().__init__(health, armor, evasion, attack, mana, speed, name)
        self.piece = "Off Hand Weapon"


# Gear that can go in either hand
class one_hand(gear):
    def __init__(self, health, armor, evasion, attack, mana, speed, name):
        super().__init__(health, armor, evasion, attack, mana, speed, name)
        self.piece = "One Hand Weapon"


# Function to make the player
def create_player():
    return player(50, 2, 5, 5, 20, 10)


# Function to make a goblin
def create_goblin():
    goblin = enemy(25, 1, 5, 3, 0, 11, "goblin")
    return random_equip(goblin)


# Randomly chooses a piece of gear from the equipment list
def choose_random_gear():
    return choice(all_equipment_lst)


# Equips a random piece of gear to a being
def random_equip(chosen_char):
    chosen_gear = choose_random_gear()
    print(chosen_char.name + " with a " + chosen_gear.name)
    chosen_char.equip_gear(chosen_gear)
    return chosen_char


# Some gear to test with
broadsword = two_hand(0, 0, -2, 5, 0, -1, "broadsword")
leather_chest = chest(0, 1, 5, 0, 0, 2, "leather_chest")

player_char = create_player()
# Some test code to make a character and make sure no errors when equipping
"""
player_char.equip_gear(broadsword)
player_char.equip_gear(broadsword)
player_char.equip_gear(leather_chest)
print(player_char.attack)
print(player_char.evasion)
print(player_char.speed)"""

# Testing out random_equip
"""foe = create_goblin()
print(foe.speed)"""
