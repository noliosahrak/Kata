import pytest
from assertpy import assert_that

from BowlingGame import BowlingGame


class TestBowlingGame:
    @pytest.fixture
    def game(self):
        self.the_game = BowlingGame()

    def test_should_score_zero_when_no_rolls(self, game):
        assert_that(self.the_game.get_score()).is_equal_to(0)

    def test_should_score_one_when_rolled_one(self, game):
        self.the_game.roll(1)
        assert_that(self.the_game.get_score()).is_equal_to(1)

