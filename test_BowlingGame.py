import pytest
from assertpy import assert_that

from BowlingGame import BowlingGame


class TestBowlingGame:
    @pytest.fixture
    def game(self):
        self.the_game = BowlingGame()

    def test_should_score_zero_when_no_rolls(self, game):
        assert_that(self.the_game.get_score()).is_equal_to(0)

    def test_should_score_20_when_pin_down_20_times(self, game):
        self.roll(20, 1)
        assert_that(self.the_game.get_score()).is_equal_to(20)

    def test_should_score_0_when_no_pin_down_20_times(self, game):
        self.roll(20, 0)
        assert_that(self.the_game.get_score()).is_equal_to(0)

    def test_should_score_spare(self, game):
        self.roll(2, 5)
        self.roll(1, 4)
        self.roll(17, 0)
        assert_that(self.the_game.get_score()).is_equal_to(18)

    def test_should_score_strike(self, game):
        self.roll1([10, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        assert_that(self.the_game.get_score()).is_equal_to(26)

    def roll(self, throws, pins):
        for i in range(0, throws):
            self.the_game.roll(pins)

    def roll1(self, list_of_pins):
        for pin in list_of_pins:
            self.the_game.roll(pin)
        pass
