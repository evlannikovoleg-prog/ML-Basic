import time
import random

from Music import Music

class Mp3player():

    def __init__(self, file_path: str, bitrate, compression):
        self.what_file = Music(file_path, bitrate, compression)

    def play(self, volume, speed):
        self.volume = volume
        self.speed = speed
        for i in reversed(range(1, speed)):
            volumes = [".", ":", "|"]

            for i in range(speed*5):
                if volume in range(1,4):
                    print(volumes[0], end='')
                if volume in range(4,8):
                    print(volumes[1], end='')
                if volume in range(8,11):
                    print(volumes[2], end='')
            time.sleep(random.random())


if __name__ == "__main__":
    mp3player = Mp3player("file_example_MP3_700KB.mp3", 128, True)
    mp3player.play(10, 5)

