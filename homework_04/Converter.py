import os
import shutil

from Video import Video
from Music import Music

class Converter:
    def __init__(self, file_to_convert):
        converting_file = file_to_convert
        name, extension = os.path.splitext(file_to_convert)
        new_file = name + "_converted" + extension

        typ = ""
        if extension == ".mp3":
            typ = "музыкальный"
            converting_file = Music(file_to_convert)
            self.actual_converter(converting_file.path, typ, new_file)
        elif extension == ".mp4":
            typ = "видео"
            converting_file = Video(file_to_convert)
            self.actual_converter(converting_file.path, typ, new_file)
            print(converting_file)
        else:
            print("Неищвестный пока программе формат файла. Программа работает только с двумя: mp3 и mp4.")

    def actual_converter(self, orig, typ, new):
        print(f"Формат файла {orig} -- это известный программе {typ} "
              f"формат \"{typ}\"\nБудет произведена конвертация файла в новый: {new}")
        try:
            shutil.copy(orig, new)
            print(f"Файл '{orig}' сконвертирован в новый улучшенный файл '{new}' успешно.")
        except FileNotFoundError:
            print(f"Ощибка: Файл '{orig}' не найден/нет прав доступа.")
        except Exception as e:
            print(f"An error occurred: {e}")



if __name__ == "__main__":
    print("Добро пожаловать в Ковертер медиафайлов 1.0.0.1")
    converter = Converter(input("Введите полный путь к файлу для его конвертации: ")) #("C:\\Users\\oevlannikov\\ML-Basic\\homework_04\\file_example_MP3_700KB.mp3")
