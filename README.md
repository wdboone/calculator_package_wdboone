# calculator_package_wdboone

[![Tests](https://github.com/wdboone/calculator_package_wdboone/actions/workflows/tests.yaml/badge.svg)](https://github.com/wdboone/calculator_package_wdboone/actions/workflows/tests.yaml)
[![PyPI](https://img.shields.io/pypi/v/calculator_package_wdboone)](https://pypi.org/project/calculator_package_wdboone/)
[![Python](https://img.shields.io/pypi/pyversions/calculator_package_wdboone)](https://pypi.org/project/calculator_package_wdboone/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A small, fully tested and type-checked calculator package used to practice
industry-level Python packaging.

* [Description](#description)
* [Installation](#installation)
* [Usage](#usage)
* [Development](#development)
* [License](#license)

## Description

`Calculator` does add, subtract, multiply and divide. `FileCalculator` sums
the numbers in a file and shows a progress bar.

## Installation

```bash
pip install calculator_package_wdboone
```

## Usage

```python
from calculator_package_wdboone import Calculator

print(Calculator().add(1, 2))  # 3
```

Or from the terminal: `calc`

## Development

```bash
git clone git@github.com:wdboone/calculator_package_wdboone.git
cd calculator_package_wdboone
python3 -m venv .venv && source .venv/bin/activate
pip install -e ".[test]"
pre-commit install
tox
```

## License

MIT
