from pathlib import Path

from tqdm import tqdm

from ..calculator import Calculator

DEFAULT_FILE = Path(__file__).parent / "nums.csv"


class FileCalculator(Calculator):
    def __init__(self, path: Path = DEFAULT_FILE, expected_lines: int = 3) -> None:
        self.path: Path = path
        self.expected_lines: int = expected_lines

    def add_file(self) -> float:
        total: float = 0
        with self.path.open() as f:
            lines = tqdm(f, total=self.expected_lines, desc="Summing lines in file")
            for line in lines:
                total += float(line)
        return total
