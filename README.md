# Calculator by Python

A calculator with limited operation (+, -, *, /, (, ) only) by Python.
Allow users to input an expression (ex: 4 + 5 / 9 * (7 + 5)) to output a result.
Unit test cases (calss and function) and coverage reports included

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Tests](#tests)

## Installation

### Prerequisites

- Git https://github.com/git-guides/install-git
- Python 3.12.4 https://www.python.org/downloads/
- Coverage tools in Python https://coverage.readthedocs.io/en/7.6.0/

### Steps

Clone the repository:<br>
    
- Open CMD or PowerShell and type the command below:<br><br>
```sh
git clone https://github.com/h102136/Calculator_Python
```
```sh
cd Calculator_Python/calculator
```
<br>

- The path setting of the program located is completed.
    
## Usage

Run the program:<br><br>

- Type the command below on the current path:<br>
```sh
python calculator.py
```
<br>

- The program will show the info below:<br>
```sh
Enter an expression ex:(7+8.5)*5-9/3 (+, -, *, / only) or Q for quit: 
```
<br>

- Then you are good to input a expression and get a result.

## Tests

### Running Tests

- Set the path to "tests" folder, assuming you are currently in "calculator" folder<br>
```sh
cd ../tests
```
<br>

- Run the test:<br>
```sh
python test_calculator.py 
```
<br>


- Check the coverage of test case:<be>

```sh
coverage run -m unittest test_calculator.py
```
<br>

- Check the coverage report:<be><br>
```sh
coverage report
```
<br>

```sh
coverage html
```