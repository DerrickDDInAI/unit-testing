# unit-testing

## What?
This repository comprises of **unit tests** to check whether the python code provided by *a fictitious company* works.

In total, there are 7 unit tests:
- 5 tests related to the company database.
- 2 tests related to the math functions (here: add()).

## Why?
This repository is actually a challenge for me to learn how to perform unit tests 
by using:
- assert python keyword
- unittest module
- pytest module and its features such as fixture and parametrization
- Mock objects

## When?
The deadline to complete this challenge is scheduled to 26/01/2021 H:17h00 PM.

## How?
In order to run the unit tests in this repository, 
you need:
- python 3
- unittest module
- pytest module
- re module
- typing module

To start the tests, you have several options:
1. Run all the tests at once by executing the command `pytest`
2. Run the tests related to the company database by executing the command `pytest -m pytest -m database_access`
3. Run the tests related to the math functions by executing the command `pytest -m math_functions`
