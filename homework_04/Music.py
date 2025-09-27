from SomeFile import SomeFile

class Music(SomeFile):
    def __init__(self, file_path: str, bitrate=128, compression=False):
        super().__init__(file_path)
        self.bitrate = bitrate
        self.compression = compression
