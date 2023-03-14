# Import statements

# Make player character
from time import sleep

from Tools.Audio.Audio import play_music_file_string
from Tools.Encounters.encounters import random_encounter
from Tools.Entities.entities import create_player

player = create_player()


# loop variable
running = True

# Main body loop
while running:
    # Creates a random encounter
    player = random_encounter(player)
    player.reset_stats()
    # Checks if the player died
    if not player.alive:
        running = False
        # Tells the player they died
        print("You died")
        # Plays the death music, and sleeps to let it actually play out
        play_music_file_string("Tools/Audio/Death.mp3")
        sleep(10)
    else:
        # While the player has exp to level up, will keep leveling up
        while player.experience >= 10:
            player.level_up()
    # Else, it will keep going
