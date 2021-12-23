from time import sleep

from pygame import mixer

mixer.init()


def play_music_file_string(music_file):
    mixer.music.load(open(music_file))
    mixer.music.play()



