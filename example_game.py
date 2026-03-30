"""
Example usage of BowlingGame
"""

from bowling_game import BowlingGame


def example_game():

    game = BowlingGame()

    rolls = [
        10,
        3, 6,
        5, 5,
        8, 1,
        10,
        10,
        10,
        9, 0,
        7, 3,
        10, 10, 8
    ]

    for r in rolls:
        game.roll(r)

    print("Example:", game.score())


def perfect_game():

    game = BowlingGame()

    for _ in range(12):
        game.roll(10)

    print("Perfect:", game.score())


def gutter_game():

    game = BowlingGame()

    for _ in range(20):
        game.roll(0)

    print("Gutter:", game.score())


def main():

    example_game()
    perfect_game()
    gutter_game()


if __name__ == "__main__":
    main()