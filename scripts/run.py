from calculator_package_wdboone import Calculator

if __name__ == "__main__":
    c = Calculator()
    print("2 + 3 =", c.add(2, 3))
    print("5 - 1 =", c.subtract(5, 1))
    print("4 * 6 =", c.multiply(4, 6))
    print("10 / 2 =", c.divide(10, 2))
