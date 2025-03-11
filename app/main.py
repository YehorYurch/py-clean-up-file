import os


class CleanUpFile:

    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback) -> None:
        try:
            os.remove(self.filename)
        except Exception as e:
            print(f"Помилка під час видалення файлу: {e}")
