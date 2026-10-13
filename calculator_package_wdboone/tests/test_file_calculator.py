from calculator_package_wdboone import FileCalculator


def test_file_calculator():
    assert FileCalculator().add_file() == 6, "add_file failed"
