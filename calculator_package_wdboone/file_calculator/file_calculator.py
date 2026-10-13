from pathlib import Path

from ..calculator import Calculator

DEFAULT_FILE = Path(__file__).parent / "nums.csv"


class FileCalculator(Calculator):
    def __init__(self, path: Path = DEFAULT_FILE) -> None:
        self.path: Path = path

    def add_file(self) -> int | None:
        total: int | None = None
        with self.path.open() as f:
            for line in f:
                if total is None:
                    total = int(line)
                else:
                    total += int(line)
        return total
