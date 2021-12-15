# Import statements
from random import choice, randint
from time import sleep


# Class for all moving beings (from enemies to the player to the npcs)
class being:
    def __init__(self, health, armor, evasion, damage, mana, speed):
        # Basic stats
        self.alive = True
        self.name = ""
        self.health = health
        self.max_health = health
        self.armor = armor
        self.damage = damage
        self.evasion = evasion
        self.mana = mana
        self.max_mana = mana
        self.equipment_lst = []
        self.speed = speed

    # Adds the stats of a gear if one of that type is not already equipped
    def equip_gear(self, equipped_gear):
        if self.check_unique(equipped_gear):
            self.equipment_lst.append(equipped_gear)
            self.health += equipped_gear.health
            self.armor += equipped_gear.armor
            self.damage += equipped_gear.damage
            self.evasion += equipped_gear.evasion
            self.mana += equipped_gear.mana
            self.speed += equipped_gear.speed

    # Removes the stats of a gear
    def unequip_gear(self, unequipped_gear):
        self.equipment_lst.pop(unequipped_gear)
        self.health -= unequipped_gear.health
        self.armor -= unequipped_gear.armor
        self.damage -= unequipped_gear.damage
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

    # Converts all equipment being worn to a string so that we can print it
    def equipment_to_string(self):
        equipment_string = ""
        for i in range(0, len(self.equipment_lst)):
            if i > 0:
                equipment_string += ", " + self.equipment_lst[i].name
            else:
                equipment_string += self.equipment_lst[i].name
        return equipment_string

    # Prints out all the stats of the being
    def stats(self):
        print(self.name)
        print("Equipped with " + self.equipment_to_string())
        print(str(self.health) + "/" + str(self.max_health) + " health remaining")
        print(str(self.mana) + "/" + str(self.max_mana) + " mana remaining")
        print(str(self.armor) + " armor")
        print(str(self.damage) + " attack")
        print(str(self.evasion) + " evasion")
        print(str(self.speed) + " speed")

    # Attacks the opponent
    def attack(self, opponent):
        # Damage is the damage it would normally do, minus the opponent's armor
        inflicted_damage = self.damage - opponent.armor
        opponent.health -= inflicted_damage
        print(self.name + " attacked " + opponent.name + " for " + str(inflicted_damage) + " damage")
        # If one of them are dead
        if opponent.health <= 0:
            # Will return the proper string for if the player or monster dies
            if type(opponent) == enemy:
                print("You've slain the " + opponent.name)
            elif type(opponent) == player:
                print("You have been slain by " + self.name)
            opponent.alive = False

    # Each turn, all combatants will take their action
    def take_action(self, opponent):
        # Check to make sure they are alive
        if self.alive:
            # If its the player
            if type(self) == player:
                # Gives them an action prompt
                action_choice = input("What would you like to do? \n"
                                      " 1: Attack your opponent\n"
                                      " 2: Use magic(WIP)\n"
                                      " 3: Defend(WIP)\n"
                                      " 4: Run away(WIP)\n"
                                      " 5: Inspect your foe\n")
                # Sleeps to pause for that action
                sleep(1)
                if action_choice == "1":
                    # 1 is attack
                    self.attack(opponent)
                elif action_choice == "2":
                    print("That is currently a Work in Progress")
                elif action_choice == "3":
                    print("That is currently a Work in Progress")
                elif action_choice == "4":
                    print("That is currently a Work in Progress")
                elif action_choice == "5":
                    # 5 prints the opponents stats
                    opponent.stats()
                else:
                    # if the user does not give valid choice
                    print("You stand there confused, as you did not choose a valid option")
            elif type(self) == enemy:
                # If its the enemy
                sleep(3)
                if self.mana == 0:
                    # if they have no mana, will just attack
                    self.attack(opponent)


# The player character class
class player(being):
    def __init__(self, health, armor, evasion, damage, mana, speed):
        super().__init__(health, armor, evasion, damage, mana, speed)
        self.name = "Player"


# Class for all enemies
class enemy(being):
    def __init__(self, health, armor, evasion, damage, mana, speed, name):
        super().__init__(health, armor, evasion, damage, mana, speed)
        self.name = name

    # Prints out the monster and the equipment they are wearing
    def print_self(self):
        if len(self.equipment_lst) > 0:
            print(self.name + " with " + self.equipment_to_string())
        else:
            print(self.name)


# Master list of all equipment
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


# Function to make the player
def create_player():
    return player(50, 2, 5, 5, 20, 10)


# Functions to make monsters
# !-----Reminder for all create functions, add their function and name to monster_function_dict and monster_lst-------!
# !-----Reminder for all create functions, add their function and name to monster_function_dict and monster_lst-------!
# !-----Reminder for all create functions, add their function and name to monster_function_dict and monster_lst-------!
def create_goblin():
    goblin = enemy(25, 1, 5, 3, 0, 11, "Goblin")
    return random_equip(goblin)


def create_orc():
    orc = enemy(40, 2, -10, 5, 0, 2, "Orc")
    return orc


def create_wolf():
    wolf = enemy(30, 0, 15, 5, 0, 14, "Wolf")
    return wolf


def create_dude():
    dude = enemy(35, 1, 4, 4, 0, 10, "Dude")
    return dude


def create_goblin_mage():
    goblin_mage = enemy(25, 1, 4, 3, 10, 10, "Goblin Mage")
    return goblin_mage


# !-----Reminder for all create functions, add their function and name to monster_function_list and monster_lst-------!
# !-----Reminder for all create functions, add their function and name to monster_function_list and monster_lst-------!
# !-----Reminder for all create functions, add their function and name to monster_function_list and monster_lst-------!
# Automates the process of creating enemies using the list and dictionary
monster_lst = ["Goblin", "Orc", "Wolf", "Dude", "Goblin Mage"]
monster_function_dict = {"Goblin": create_goblin, "Orc": create_orc, "Wolf": create_wolf, "Dude": create_dude,
                         "Goblin Mage": create_goblin_mage}


# Randomly chooses a piece of gear from the equipment list
def choose_random_gear():
    return choice(all_equipment_lst)


# Equips a random piece of gear to a being
def random_equip(chosen_char):
    chosen_gear = choose_random_gear()
    chosen_char.equip_gear(chosen_gear)
    return chosen_char


# Creates a random enemy from all available enemies
def create_random_enemy():
    return monster_function_dict[choice(monster_lst)]()


# Takes a turn, where each opponent uses an action against eachother
def turn(opponent1, opponent2, turn_counter):
    print("Starting turn " + str(turn_counter))
    opponent1.take_action(opponent2)
    opponent2.take_action(opponent1)


# Combat loop
def combat(opponent1, opponent2):
    turn_counter = 1
    print("You encounter a ", end="")
    opponent2.print_self()
    while opponent1.alive and opponent2.alive:
        # If they are both still alive, determines next turn order by speed comparison
        if opponent1.speed >= opponent2.speed:
            turn(opponent1, opponent2, turn_counter)
        else:
            turn(opponent2, opponent1, turn_counter)
        turn_counter += 1


# Creates a chest with an item the player can equip
def chest_encounter():
    chest_loot = choose_random_gear()
    chest_loot.stats()
    equip_choice = input("You find a chest with a " + chest_loot.name + " in it. Equip it? Y/N\n").lower()
    equip_prompt(chest_loot, equip_choice)


# function for grabbing/not grabbing equipment
def equip_prompt(loot, equip_choice):
    if equip_choice == "y":
        print("Equipping the " + loot.name)
        player_char.equip_gear(loot)
    else:
        print("You leave the " + loot.name + " behind, maybe someone else will use it")


# Randomly chooses if the next encounter is a combat encounter or if the player finds a chest
def random_encounter():
    rand_num = randint(1, 10)
    if rand_num <= 7:
        combat_encounter()
    else:
        chest_encounter()


# Creates an enemy then runs combat between the player and the enemy
def combat_encounter():
    # Creates a random enemy
    foe = create_random_enemy()
    # starts the combat loop
    combat(player_char, foe)
    # If the player is still alive
    if player_char.alive:
        # for each equipment worn by the monster
        for i in range(0, len(foe.equipment_lst)):
            # Asks if the player would like to equip it, and does accordingly
            iterated_equipment = foe.equipment_lst[i]
            equip_choice = input("The " + foe.name + " was wearing a " + iterated_equipment.name + ". Would you like "
                                                                                                   "to equip it? Y/N"
                                                                                                   "\n").lower()
            equip_prompt(iterated_equipment, equip_choice)


# Some gear to test with
broadsword = two_hand(0, 0, -2, 5, 0, -1, "Broadsword")
leather_chest = chest(0, 1, 5, 0, 0, 2, "Leather chest")

# Make player character
player_char = create_player()
# Some test code to make a character and make sure no errors when equipping
"""
player_char.equip_gear(broadsword)
player_char.equip_gear(broadsword)
player_char.equip_gear(leather_chest)
print(player_char.damage)
print(player_char.evasion)
print(player_char.speed)"""

# Testing out random_equip
"""foe = create_goblin()
print(foe.speed)"""

# loop variable
running = True

# Main body loop
while running:
    # Creates a random encounter
    random_encounter()
    # Checks if the player died
    if not player_char.alive:
        running = False
    # Else, it will keep going
