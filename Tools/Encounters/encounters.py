# Creates a chest with an item the player can equip
from random import randint

from Tools.Combat.combat import combat
from Tools.Entities.entities import create_random_enemy
from Tools.Equipment.equipment import choose_random_gear, equip_prompt


def chest_encounter(player):
    chest_loot = choose_random_gear()
    chest_loot.stats()
    equip_choice = input("You find a chest with a " + chest_loot.name + " in it. Equip it? Y/N\n").lower()
    return equip_prompt(player, chest_loot, equip_choice)


# Randomly chooses if the next encounter is a combat encounter or if the player finds a chest
def random_encounter(player):
    rand_num = randint(1, 10)
    if rand_num <= 7:
        return combat_encounter(player)
    else:
        return chest_encounter(player)


# Creates an enemy then runs combat between the player and the enemy
def combat_encounter(player):
    # Creates a random enemy
    foe = create_random_enemy(player)
    # starts the combat loop
    combat(player, foe)
    # If the player is still alive
    if player.alive:
        # Gives the player the monster's experience
        player.experience += foe.experience
        # for each equipment worn by the monster
        for i in range(0, len(foe.equipment_lst)):
            # Asks if the player would like to equip it, and does accordingly
            iterated_equipment = foe.equipment_lst[i]
            equip_choice = input("The " + foe.name + " was wearing a " + iterated_equipment.name + ". Would you like "
                                                                                                   "to equip it? Y/N"
                                                                                                   "\n").lower()
            equip_prompt(player, iterated_equipment, equip_choice)
    return player
