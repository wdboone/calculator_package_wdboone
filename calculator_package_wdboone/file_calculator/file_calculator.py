from pathlib import Path

from ..calculator import Calculator

DEFAULT_FILE = Path(__file__).parent / "nums.csv"


class FileCalculator(Calculator):
    def __init__(self, path: Path = DEFAULT_FILE) -> None:
        self.path: Path = path

    def add_file(self) -> float | None:
        total: float | None = None
        with self.path.open() as f:
            for line in f:
                if total is None:
                    total = float(line)
                else:
                    total += float(line)
        return total
