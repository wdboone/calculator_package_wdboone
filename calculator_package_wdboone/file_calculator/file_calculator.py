from pathlib import Path

from ..calculator import Calculator

DEFAULT_FILE = Path(__file__).parent / "nums.csv"


class FileCalculator(Calculator):
    def __init__(self, path=DEFAULT_FILE):
        self.path = path

    def add_file(self):
        total = None
        with self.path.open() as f:
            for line in f:
                if total is None:
                    total = line
                else:
                    total += line
        return total
