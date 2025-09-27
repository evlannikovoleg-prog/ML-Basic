from Music import Music


class Video(Music):
    def __init__(self, file_path: str, bitrate=512, compression=True, quality="FullHD", framerate=25):
        super().__init__(file_path, bitrate, compression)
        self.quality = quality
        self.framerate = framerate
