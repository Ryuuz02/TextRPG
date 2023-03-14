# Imports
from pygame import mixer

# Initializes the mixer
mixer.init()


# File to take in a string, and play that file location as music
def play_music_file_string(music_file):
    mixer.music.load(open(music_file))
    mixer.music.play()
