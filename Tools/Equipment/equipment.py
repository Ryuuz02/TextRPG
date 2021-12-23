# Master list of all equipment
from random import choice

from Tools.Audio.Audio import play_music_file_string

all_equipment_lst = []


# Parent class for all equipment, have the stats of the gear
class gear:
    def __init__(self, health, armor, evasion, damage, mana, speed, name):
        self.health = health
        self.armor = armor
        self.damage = damage
        self.evasion = evasion
        self.mana = mana
        self.speed = speed
        self.name = name
        # Adds itself to all_equipment_lst
        all_equipment_lst.append(self)

    # Prints out the stats of the gear
    def stats(self):
        print(self.name)
        print(str(self.health) + " health")
        print(str(self.mana) + " mana")
        print(str(self.armor) + " armor")
        print(str(self.damage) + " attack")
        print(str(self.evasion) + " evasion")
        print(str(self.speed) + " speed")


# Helmet equipment
class helmet(gear):
    def __init__(self, health, armor, evasion, damage, mana, speed, name):
        super().__init__(health, armor, evasion, damage, mana, speed, name)
        self.piece = "Helmet"


# Chest equipment
class chest(gear):
    def __init__(self, health, armor, evasion, damage, mana, speed, name):
        super().__init__(health, armor, evasion, damage, mana, speed, name)
        self.piece = "Chest"


# Hands equipment
class hands(gear):
    def __init__(self, health, armor, evasion, damage, mana, speed, name):
        super().__init__(health, armor, evasion, damage, mana, speed, name)
        self.piece = "Hands"


# Arms equipment
class arms(gear):
    def __init__(self, health, armor, evasion, damage, mana, speed, name):
        super().__init__(health, armor, evasion, damage, mana, speed, name)
        self.piece = "Arms"


# Legs equipment
class legs(gear):
    def __init__(self, health, armor, evasion, damage, mana, speed, name):
        super().__init__(health, armor, evasion, damage, mana, speed, name)
        self.piece = "Legs"


# Feet equipment
class feet(gear):
    def __init__(self, health, armor, evasion, damage, mana, speed, name):
        super().__init__(health, armor, evasion, damage, mana, speed, name)
        self.piece = "Feet"


# Two handed weapons
class two_hand(gear):
    def __init__(self, health, armor, evasion, damage, mana, speed, name):
        super().__init__(health, armor, evasion, damage, mana, speed, name)
        self.piece = "Two Hand Weapon"


# Off hand gear (shields, torches, etc.)
class off_hand(gear):
    def __init__(self, health, armor, evasion, damage, mana, speed, name):
        super().__init__(health, armor, evasion, damage, mana, speed, name)
        self.piece = "Off Hand Weapon"


# Gear that can go in either hand
class one_hand(gear):
    def __init__(self, health, armor, evasion, damage, mana, speed, name):
        super().__init__(health, armor, evasion, damage, mana, speed, name)
        self.piece = "One Hand Weapon"


# Randomly chooses a piece of gear from the equipment list
def choose_random_gear():
    return choice(all_equipment_lst)


# Equips a random piece of gear to a being
def random_equip(chosen_char):
    chosen_gear = choose_random_gear()
    chosen_char.equip_gear(chosen_gear)
    return chosen_char


# function for grabbing/not grabbing equipment
def equip_prompt(player, loot, equip_choice):
    if equip_choice == "y":
        # Get item music
        play_music_file_string("Tools/Audio/GetItem.mp3")
        print("Equipping the " + loot.name)
        player.equip_gear(loot)
        return player
    else:
        print("You leave the " + loot.name + " behind, maybe someone else will use it")
        return player


# Some gear to test with
broadsword = two_hand(0, 0, -2, 5, 0, -1, "Broadsword")
leather_chest = chest(0, 1, 5, 0, 0, 2, "Leather chest")
