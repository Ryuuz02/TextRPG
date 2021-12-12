class being:
    def __init__(self, health, armor, evasion, attack, mana, speed):
        self.health = health
        self.armor = armor
        self.attack = attack
        self.evasion = evasion
        self.mana = mana
        self.equipment_lst = []
        self.speed = speed

    def equip_gear(self, equipped_gear):
        self.equipment_lst.append(gear)
        self.health += equipped_gear.health
        self.armor += equipped_gear.armor
        self.attack += equipped_gear.attack
        self.evasion += equipped_gear.evasion
        self.mana += equipped_gear.mana
        self.speed += equipped_gear.speed


class player(being):
    def __init__(self, health, armor, evasion, attack, mana, speed):
        super().__init__(health, armor, evasion, attack, mana, speed)


class enemy(being):
    def __init__(self, health, armor, evasion, attack, mana, speed):
        super().__init__(health, armor, evasion, attack, mana, speed)


class gear:
    def __init__(self, health, armor, evasion, attack, mana, speed):
        self.health = health
        self.armor = armor
        self.attack = attack
        self.evasion = evasion
        self.mana = mana
        self.speed = speed


"""
test_char = player(50, 2, 5, 5, 20)
test_enemy = enemy(10, 1, 2, 2, 5)
print(test_char.attack)
print(test_enemy.attack)
"""
broadsword = gear(0, 0, -2, 5, 0, -1)


def create_player():
    return player(50, 2, 5, 5, 20, 10)


def create_goblin():
    return enemy(25, 1, 5, 3, 0, 11)


player_char = create_player()
player_char.equip_gear(broadsword)
print(player_char.attack)
