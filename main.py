# Import statements

# Make player character
from Tools.Encounters.encounters import random_encounter
from Tools.Entities.entities import create_player

player = create_player()

# loop variable
running = True

# Main body loop
while running:
    # Creates a random encounter
    player = random_encounter(player)
    # Checks if the player died
    if not player.alive:
        running = False
    else:
        # While the player has exp to level up, will keep leveling up
        while player.experience >= 10:
            player.level_up()
    # Else, it will keep going
