class BowlingGame:
    def __init__(self):
        self.score = 0

    def get_score(self):
        return self.score

    def roll(self, pins):
        self.score += pins
