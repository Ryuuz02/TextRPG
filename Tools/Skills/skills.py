# Class for skills


class skill:
    # Assigning variables
    def __init__(self, cooldown, skilltype, tier, name):
        self.cooldown = cooldown
        self.skilltype = skilltype
        self.tier = tier
        self.name = name

    # function to actually use itself
    def use_skill(self, user, opponent, is_player, remaining_cooldown):
        # If the user has enough mana
        if remaining_cooldown == 0:
            # Tells the user
            print(user.name + " used " + self.name + " on " + opponent.name)
            skill_index = user.skill_lst.index(self.name)
            user.skill_cooldown_lst[skill_index] = self.cooldown
            # uses the skill
            skill_function_dict[self.name](user, opponent)
        # If the user does not have the mana
        else:
            # If the user is the player, tells them they don't have enough
            if is_player:
                print(self.name + " is still on cooldown")
            # Otherwise tells them that someone else failed to use
            else:
                print(user.name + " tried to use " + self.name + " too quickly")


# Functions for skills
# !-----Reminder for all create functions, add their function and name to skill_function_dict and skill_lst-------!
# !-----Reminder for all create functions, add their function and name to skill_function_dict and skill_lst-------!
# !-----Reminder for all create functions, add their function and name to skill_function_dict and skill_lst-------!
# Power Attack skill
def power_attack(user, opponent):
    # Does damage equal to 1.5 times user damage
    inflicted_damage = user.damage * 1.5
    opponent.health -= (inflicted_damage - opponent.armor)
    # Tells the user
    print(user.name + " used a power attack on " + opponent.name + " for " + str(inflicted_damage) + " but " +
          str(opponent.armor) + " damage was blocked")


# Defend skill
def defend(user, opponent):
    # Increases the user's armor by a tenth of their armor
    armor_increase = user.armor / 10
    user.armor += armor_increase
    # Tells the user
    print(user.name + " defended themselves, increasing their armor by " + str(armor_increase))


# Icicle skill
def intimidating_roar(user, opponent):
    # Reduces opponents damage by 10%
    opponent.damage *= 0.9
    # Tells the user
    print(user.name + " roared at " + opponent.name + ", reducing their damage by " + str(10 / 9 * opponent.damage))


# !-----Reminder for all create functions, add their function and name to skill_function_dict and skill_class_dict-----!
# !-----Reminder for all create functions, add their function and name to skill_function_dict and skill_class_dict-----!
# !-----Reminder for all create functions, add their function and name to skill_function_dict and skill_class_dict-----!
# Automates the process of creating skills and using them using the 2 dictionaries
# Classes for each skill, has further information about them
Power_Attack = skill(3, "offense", 1, "Power Attack")
Defend = skill(2, "defense", 1, "Defend")
Intimidating_Roar = skill(2, "utility", 1, "Intimidating Roar")
# One dictionary that has every class
skill_class_dict = {"Power Attack": Power_Attack, "Defend": Defend, "Intimidating Roar": Intimidating_Roar}
# One dictionary that has all the functions
skill_function_dict = {"Power Attack": power_attack, "Defend": defend, "Intimidating Roar": intimidating_roar}


# uses the skill
def use_skill(user, opponent, skill_name, is_player, remaining_cooldown):
    skill_class_dict[skill_name].use_skill(user, opponent, is_player, remaining_cooldown)
