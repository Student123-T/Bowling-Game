import pytest
from bowling_game import BowlingGame


def roll_many(game, n, pins):
    for _ in range(n):
        game.roll(pins)


def test_gutter_game():
    g = BowlingGame()
    roll_many(g, 20, 0)
    assert g.score() == 0


def test_all_ones():
    g = BowlingGame()
    roll_many(g, 20, 1)
    assert g.score() == 20


def test_spare():
    g = BowlingGame()

    g.roll(5)
    g.roll(5)
    g.roll(5)

    roll_many(g, 17, 0)
    # the score objective is 20 because the spare gives a bonus of the next roll (5) to the first frame (10) and then we have the second frame with 5 pins
    assert g.score() == 20


def test_strike():

    g = BowlingGame()

    g.roll(10)
    g.roll(3)
    g.roll(4)

    roll_many(g, 16, 0)

    assert g.score() == 24


def test_perfect():

    g = BowlingGame()

    roll_many(g, 12, 10)

    assert g.score() == 300