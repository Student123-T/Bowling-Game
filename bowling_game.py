"""
Bowling Game Implementation
Backend scoring system
"""

class BowlingGame:
    """
    Bowling game scoring system.
    """

    def __init__(self):
        self.rolls: list[int] = []

    def roll(self, pins: int) -> None:
        """Record pins"""
        self.rolls.append(pins)

    def score(self) -> int:
        """Calculate score"""
        score = 0
        frame_index = 0

        for frame in range(10):

            if self._is_strike(frame_index):
                score += 10 + self._strike_bonus(frame_index)
                frame_index += 1

            elif self._is_spare(frame_index):
                score += 10 + self._spare_bonus(frame_index)
                frame_index += 2

            else:
                score += (
                    self.rolls[frame_index]
                    + self.rolls[frame_index + 1]
                )
                frame_index += 2

        return score

    def _is_strike(self, i: int) -> bool:
        return self.rolls[i] == 10

    def _is_spare(self, i: int) -> bool:
        return self.rolls[i] + self.rolls[i + 1] == 10

    def _strike_bonus(self, i: int) -> int:
        return self.rolls[i + 1] + self.rolls[i + 2]

    def _spare_bonus(self, i: int) -> int:
        return self.rolls[i + 2]