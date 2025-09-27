#  В проекте мы работаем с медиа-файлами (аудио, видео, фото).
#  Есть некоторый общий набор данных о файле, необходимый для реализации бизнес-логики
#  (имя, размер, дата создания, владелец...).
#  Для каждого типа медиа-файлов есть свой набор метаданных.

from pathlib import Path
from datetime import datetime


class SomeFile:
    def __init__(self, file_path: str):
        self.path = Path(file_path)
        self.name = self.path.name
        self._load_file_data()
    def _load_file_data(self) -> None:
        if self.path.exists() and self.path.is_file():
            stat_info = self.path.stat()
            #print(stat_info)
            self.size = stat_info.st_size
            self.creation_date = datetime.fromtimestamp(stat_info.st_ctime)
        else:
            self.size = 0
            self.creation_date = None
            self.modification_date = None

    def __str__(self) -> str:
        """Строковое представление файла."""
        return f"File: {self.name} ({self.size} bytes, created: {self.creation_date})"


# Пример использования
if __name__ == "__main__":
    file = SomeFile("README.md")
    print(file)
    print(f"Имя: {file.name}")
    print(f"Размер: {file.size} байт")
    print(f"Дата создания: {file.creation_date}")