import time
import random
from string import ascii_lowercase, ascii_uppercase

from Video import Video


class Mp4player():

    def __init__(self, what_to_play, bitrate, compression, quality, framerate):
        self.what_file = Video(what_to_play, bitrate, compression, quality, framerate)

    def videogen(self, speed, frames):
        alphabet = ascii_lowercase + ascii_uppercase
        for frame in range(0, frames):
            for y in range(1, speed):
                for i in range(speed * 5):
                    print(random.choice(alphabet), end='')
                time.sleep(random.random() / speed)
            print()

    def play(self, volume, speed):
        self.volume = volume
        self.speed = speed

        self.videogen(speed, 5)


if __name__ == "__main__":
    mp4player = Mp4player("file_example_MP4_480_1_5MG.mp4", 128, True, "HD", 25)
    mp4player.play(10, 5)
