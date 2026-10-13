from calculator_package_wdboone import Calculator


class TestCalculator:
    def test_add(self):
        assert Calculator().add(1, 2) == 3, "add failed"

    def test_subtract(self):
        assert Calculator().subtract(1, 2) == -1, "subtract failed"

    def test_multiply(self):
        assert Calculator().multiply(3, 2) == 6, "multiply failed"

    def test_divide(self):
        assert Calculator().divide(8, 2) == 4, "divide failed"
