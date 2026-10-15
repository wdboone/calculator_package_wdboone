from .calculator import Calculator


def main() -> None:
    c = Calculator()
    print(c.add(1, 2))  # noqa: T201


if __name__ == "__main__":
    main()
