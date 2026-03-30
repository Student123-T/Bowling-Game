======================
Bowling Game Project
======================

Project Description: -
-------------------
This project is a Bowling Game scoring system developed in Python. 
The program calculates the total score of a bowling game based on official bowling rules, 
including strikes, spares, and open frames.

The project demonstrates software testing concepts such as unit testing, debugging, 
refactoring, and documentation.

--------------------------------------------------

Project Files: -
-------------

bowling_game.py
- Main backend program
- Contains BowlingGame class
- Handles rolls and score calculation

example_games.py
- Demonstrates how the program works
- Includes different game scenarios:
  • Example game
  • Perfect game
  • Gutter game

test_bowling.py
- Contains unit tests using pytest
- Tests different scenarios like:
  • Gutter game
  • Strike
  • Spare
  • Perfect game

bowling_game.html
- Generated PythonDoc documentation
- Contains API documentation for the program

README.txt
- Project overview and instructions

--------------------------------------------------

How to Run the Program: -
----------------------

1. Run example games:
   python example_games.py

2. Run unit tests:
   python -m pytest test_bowling_game.py

--------------------------------------------------

Features: -
--------

- Calculates bowling score correctly
- Handles:
  • Strike (10 + next 2 rolls bonus)
  • Spare (10 + next roll bonus)
  • Open frames
- Supports full 10-frame game
- Includes multiple test cases

--------------------------------------------------

Testing: -
-------

Unit testing is done using pytest.

Test cases include:
- Gutter game (all 0)
- Perfect game (300 score)
- Spare case
- Strike case
- Regular game

All test cases pass successfully after debugging and fixes.

--------------------------------------------------

Debugging and Improvements: -
--------------------------

The following issues were identified and fixed:

- Index out of range errors
- Incorrect frame logic
- Missing validation

Refactoring improvements:

- Added helper functions (_is_strike, _is_spare)
- Added type hints
- Improved readability
- Added docstrings for documentation

--------------------------------------------------


Made By: -
------

Name: Tanmmey Arora
Course: Software Testing / IT Course
Institution: Whitecliffe

--------------------------------------------------

Conclusion: -
----------

This project helped in understanding software testing, debugging, 
and refactoring. It demonstrates how to build reliable software 
and verify correctness using unit testing.