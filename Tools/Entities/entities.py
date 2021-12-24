# Class for all moving beings (from enemies to the player to the npcs)
from random import randint, choice
from time import sleep

from Tools.Audio.Audio import play_music_file_string
from Tools.Equipment.equipment import random_equip
from Tools.Images.ImageDisplay import display_image
from Tools.Skills.skills import use_skill
from Tools.Spells.spells import cast_spell


class being:
    def __init__(self, health, armor, evasion, damage, mana, speed):
        # Basic stats
        self.alive = True
        self.name = ""
        self.health = health
        self.max_health = health
        self.armor = armor
        self.total_armor = armor
        self.damage = damage
        self.total_damage = damage
        self.evasion = evasion
        self.total_evasion = evasion
        self.mana = mana
        self.max_mana = mana
        self.equipment_lst = []
        self.speed = speed
        self.total_speed = speed
        self.spell_lst = []
        self.skill_lst = []
        self.skill_cooldown_lst = []

    def add_skill(self, skill_name):
        self.skill_lst.append(skill_name)
        self.skill_cooldown_lst.append(0)

    def tick_skills(self):
        for i in range(0, len(self.skill_cooldown_lst)):
            if self.skill_cooldown_lst[i] != 0:
                self.skill_cooldown_lst[i] -= 1
            if issubclass(type(self), player):
                if self.skill_cooldown_lst[i] == 0:
                    print(self.skill_lst[i] + " is available")
                else:
                    print(self.skill_lst[i] + " still has " + str(self.skill_cooldown_lst[i]) + " turns until it is "
                                                                                                "available")

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
        pass

    def reset_stats(self):
        self.armor = self.total_armor
        self.speed = self.total_speed
        self.evasion = self.total_evasion
        self.damage = self.total_damage

    def determine_action(self, opponent):
        pass

    def cast_spell(self, opponent):
        pass

    def use_skill(self, opponent):
        pass


# The player character class
class player(being):
    def __init__(self, health, armor, evasion, damage, mana, speed, name):
        super().__init__(health, armor, evasion, damage, mana, speed)
        self.name = name
        self.level = 1
        self.experience = 0

        # If its the player

    def take_action(self, opponent):
        # Gives them an action prompt
        action_choice = input("What would you like to do? \n"
                              " 1: Attack your opponent\n"
                              " 2: Use magic\n"
                              " 3: Use Skill\n"
                              " 4: Run away(WIP)\n"
                              " 5: Inspect your foe\n")
        # Sleeps to pause for that action
        sleep(1)
        if action_choice == "1":
            # 1 is attack
            self.attack(opponent)
        elif action_choice == "2":
            # 2 is cast spell
            self.cast_spell(opponent)
        elif action_choice == "3":
            # 3 is use skill
            self.use_skill(opponent)
        elif action_choice == "4":
            print("That is currently a Work in Progress")
        elif action_choice == "5":
            # 5 prints the opponents stats
            opponent.stats()
        else:
            # if the user does not give valid choice
            print("You stand there confused, as you did not choose a valid option")

    # casts a spell
    def cast_spell(self, opponent):
        # Prints out all spells the player has
        print("Spells:")
        for i in range(0, len(self.spell_lst)):
            print(" " + str(i) + ": " + self.spell_lst[i])
        # Asks user which one to cast
        spell_choice = input("What spell would you like to cast (type the number tied to the spell), or type 'e' to "
                             "exit\n")
        # If the user wishes to back out of casting a spell
        if spell_choice == "e":
            self.take_action(opponent)
        # Otherwise
        else:
            # Makes sure the user properly inputs an integer
            try:
                # If it is in the spell list
                if int(spell_choice) < len(self.spell_lst):
                    # Casts the spell
                    cast_spell(self, opponent, self.spell_lst[int(spell_choice)], True)
                # Else, will tell the user
                else:
                    print("You don't have that many spells")
            except ValueError:
                print("Not a valid input")

    def use_skill(self, opponent):
        # Prints out all spells the player has
        print("Skills:")
        for i in range(0, len(self.skill_lst)):
            print(" " + str(i) + ": " + self.skill_lst[i])
        # Asks user which one to cast
        skill_choice = input("What skill would you like to use (type the number tied to the skill), or type 'e' to "
                             "exit\n")
        # If the user wishes to back out of casting a spell
        if skill_choice == "e":
            self.take_action(opponent)
        # Otherwise
        else:
            # Makes sure the user properly inputs an integer
            try:
                # If it is in the spell list
                if int(skill_choice) < len(self.skill_lst):
                    # Casts the spell
                    use_skill(self, opponent, self.skill_lst[int(skill_choice)], True,
                              self.skill_cooldown_lst[int(skill_choice)])
                # Else, will tell the user
                else:
                    print("You don't have that many skills")
            except ValueError:
                print("Not a valid input")

    # Refreshes health and mana back to maximum values
    def refresh_vitals(self):
        self.mana = self.max_mana
        self.health = self.max_health

    # Tells the user they leveled up, takes 10 experience, gives them stats, then refreshes their health and mana
    def level_up(self):
        # Level up music
        play_music_file_string("Tools/Audio/LevelUp.mp3")
        print(self.name + " leveled up to level " + str(self.level + 1))
        self.experience -= 10
        self.level += 1
        self.class_up()
        self.refresh_vitals()

    def class_up(self):
        pass


# <!-----------------Below are the different starting classes that the player can choose from-------------------------!>
# They start with different stats (and potentially spells) and get a different assortment of stats on level up
# These stats are the class specific class_up function

# Stereotypical offensive casting class
class mage(player):
    def __init__(self, name):
        super().__init__(40, 1, 10, 5, 20, 11, name)
        self.spell_lst.append("Fireball")
        self.spell_lst.append("Icicle")

    def class_up(self):
        self.max_mana += 5
        self.max_health += 5
        self.damage += 1
        self.speed += 1


# Heavy hitting no defense class
class barbarian(player):
    def __init__(self, name):
        super().__init__(60, 0, 0, 7, 0, 13, name)
        self.add_skill("Power Attack")
        self.add_skill("Intimidating Roar")

    def class_up(self):
        self.max_health += 10
        self.damage += 1.5
        self.speed += 1.5


# defensive/support caster
class cleric(player):
    def __init__(self, name):
        super().__init__(50, 1, 5, 5, 10, 10, name)
        self.spell_lst.append("Heal")
        self.add_skill("Defend")

    def class_up(self):
        self.max_health += 7
        self.damage += 1
        self.speed += 1
        self.max_mana += 5


# Tough all rounder class, tankier but much slower than barbarian
class knight(player):
    def __init__(self, name):
        super().__init__(50, 2, 0, 7, 0, 9, name)
        self.add_skill("Defend")
        self.add_skill("Power Attack")

    def class_up(self):
        self.max_health += 7
        self.armor += 1
        self.damage += 1.5
        self.speed += 1


# Class for all enemies
class enemy(being):
    def __init__(self, health, armor, evasion, damage, mana, speed, name, tier, spell_lst, experience):
        super().__init__(health, armor, evasion, damage, mana, speed)
        self.name = name
        # Tier is basically how good of a spellcaster they are
        self.tier = tier
        self.spell_lst = spell_lst
        self.experience = experience

    # Prints out the monster and the equipment they are wearing
    def print_self(self):
        if len(self.equipment_lst) > 0:
            print(self.name + " with " + self.equipment_to_string())
        else:
            print(self.name)

    # Attempts to cast a random spell that they have
    def cast_spell(self, opponent):
        cast_spell(self, opponent, choice(self.spell_lst), False)

    # Determines if they will attack or cast based on how good of a caster they are
    def determine_action(self, opponent):
        cast_chance = randint(1, 10)
        skill_chance = randint(1, 10)
        if cast_chance <= self.tier:
            self.cast_spell(opponent)
        elif skill_chance <= len(self.skill_lst):
            running = True
            while running:
                skill_choice = randint(0, len(self.skill_lst))
                if self.skill_cooldown_lst[skill_choice] == 0:
                    use_skill(self, opponent, self.skill_lst[skill_choice], True, self.skill_cooldown_lst[skill_choice])
                    running = False
        else:
            self.attack(opponent)

    def take_action(self, opponent):
        # If its the enemy
        sleep(3)
        self.determine_action(opponent)


# Function to make the player
def create_player():
    # Asks what class they would like
    class_choice = input("Would you like to be a mage, barbarian, knight or cleric\n").lower()
    # Asks their player name
    name_choice = input("What is your character's name?\n")
    # Creates the associated class as the player
    if class_choice == "mage":
        return mage(name_choice)
    elif class_choice == "barbarian":
        return barbarian(name_choice)
    elif class_choice == "cleric":
        return cleric(name_choice)
    elif class_choice == "knight":
        return knight(name_choice)
    # Or tells them that it is not an option and to try again
    else:
        print("That is not a valid option")
        return create_player()


# Functions to make monsters
# !-----Reminder for all create functions, add their function and name to monster_function_dict and monster_lst-------!
# !-----Reminder for all create functions, add their function and name to monster_function_dict and monster_lst-------!
# !-----Reminder for all create functions, add their function and name to monster_function_dict and monster_lst-------!
def create_goblin(scalar):
    goblin = enemy(25 * scalar, 1 * scalar, 5 * scalar, 3 * scalar, 0 * scalar, 11 * scalar, "Goblin", 0, [], 5)
    if scalar >= 5:
        goblin = random_equip(goblin)
    return random_equip(goblin)


def create_orc(scalar):
    orc = enemy(40 * scalar, 2 * scalar, -10 * scalar, 5 * scalar, 0 * scalar, 2 * scalar, "Orc", 0, [], 5)
    if scalar >= 5:
        orc = random_equip(orc)
    return orc


def create_wolf(scalar):
    wolf = enemy(30 * scalar, 0 * scalar, 15 * scalar, 5 * scalar, 0 * scalar, 14 * scalar, "Wolf", 0, [], 5)
    wolf.add_skill("Power Attack")
    return wolf


def create_dude(scalar):
    dude = enemy(35 * scalar, 1 * scalar, 4 * scalar, 4 * scalar, 0 * scalar, 10 * scalar, "Dude", 0, [], 5)
    if scalar >= 5:
        dude = random_equip(dude)
    return dude


def create_goblin_mage(scalar):
    goblin_mage = enemy(25 * scalar, 1 * scalar, 4 * scalar, 3 * scalar, 10 * scalar, 10 * scalar, "Goblin Mage",
                        1, ["Fireball"], 5)
    if scalar >= 5:
        goblin_mage.spell_lst.append("Icicle")
    return goblin_mage


# !-----Reminder for all create functions, add their function and name to monster_function_dict and monster_lst-------!
# !-----Reminder for all create functions, add their function and name to monster_function_dict and monster_lst-------!
# !-----Reminder for all create functions, add their function and name to monster_function_dict and monster_lst-------!
# Automates the process of creating enemies using the list and dictionary
monster_lst = ["Goblin", "Orc", "Wolf", "Dude", "Goblin Mage"]
monster_function_dict = {"Goblin": create_goblin, "Orc": create_orc, "Wolf": create_wolf, "Dude": create_dude,
                         "Goblin Mage": create_goblin_mage}


def create_scalar(player_char):
    return player_char.level * 0.3 + 0.7


# Creates a random enemy from all available enemies
def create_random_enemy(player_char):
    foe = monster_function_dict[choice(monster_lst)](create_scalar(player_char))
    display_image("Tools/Images/" + foe.name + ".jpg")
    return foe
