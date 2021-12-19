# Class for spells


class spell:
    # Assigning variables
    def __init__(self, mana, spelltype, tier, name):
        self.mana = mana
        self.spelltype = spelltype
        self.tier = tier
        self.name = name

    # function to actually cast itself
    def cast_spell(self, user, opponent, is_player):
        # If the user has enough mana
        if user.mana >= self.mana:
            # Takes their mana
            user.mana -= self.mana
            # Tells the user
            print(user.name + " used " + str(self.mana) + " mana to cast " + self.name)
            # Casts the spell
            spell_function_dict[self.name](user, opponent)
        # If the user does not have the mana
        else:
            # If the user is the player, tells them they don't have enough
            if is_player:
                print("You do not have enough mana to use that")
            # Otherwise tells them that someone else failed to cast
            else:
                print(user.name + " tried to cast " + self.name + " but did not have the mana for it")


# Functions for spells
# !-----Reminder for all create functions, add their function and name to spell_function_dict and spell_lst-------!
# !-----Reminder for all create functions, add their function and name to spell_function_dict and spell_lst-------!
# !-----Reminder for all create functions, add their function and name to spell_function_dict and spell_lst-------!
# Fireball Spell
def fireball(user, opponent):
    # Does damage equal to 1.5 times caster damage
    inflicted_damage = user.damage * 1.5
    opponent.health -= inflicted_damage
    # Tells the user
    print(user.name + " hurled a fireball at " + opponent.name + " for " + str(inflicted_damage) + " damage")


# Heal spell
def heal(user, opponent):
    # Heals the caster for their damage plus a tenth of their max hp
    health_heal = user.damage + user.max_health / 10
    user.health += health_heal
    # Tells the user
    print(user.name + " healed themselves for " + str(health_heal) + " health")


# Icicle spell
def icicle(user, opponent):
    # Does damage equal to caster's damage
    inflicted_damage = user.damage
    opponent.health -= inflicted_damage
    # Reduces opponents speed by 10%
    opponent.speed *= 0.9
    # Tells the user
    print(user.name + " dropped an icicle on " + opponent.name + " for " + str(inflicted_damage) + " damage, they were "
                                                                                                   "also slowed by 10%")


# !-----Reminder for all create functions, add their function and name to spell_function_dict and spell_class_dict-----!
# !-----Reminder for all create functions, add their function and name to spell_function_dict and spell_class_dict-----!
# !-----Reminder for all create functions, add their function and name to spell_function_dict and spell_class_dict-----!
# Automates the process of creating spells and casting them using the 2 dictionaries
# Classes for each spell, has further information about them
Fireball = spell(5, "offense", 1, "Fireball")
Heal = spell(10, "defense", 1, "Heal")
Icicle = spell(5, "offense", 1, "Icicle")
# One dictionary that has every class
spell_class_dict = {"Fireball": Fireball, "Heal": Heal, "Icicle": Icicle}
# One dictionary that has all the functions
spell_function_dict = {"Fireball": fireball, "Heal": heal, "Icicle": icicle}


# Casts the spell
def cast_spell(user, opponent, spell_name, is_player):
    spell_class_dict[spell_name].cast_spell(user, opponent, is_player)
