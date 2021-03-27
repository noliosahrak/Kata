class BowlingGame:
    def __init__(self):
        self.number_of_rolls = 0
        self.rolls = [0 for i in range(0, 21)]

    def get_score(self):
        print(self.rolls)
        score = 0
        cursor = 0
        for i in range(0, 10):
            if self.is_spare(cursor):
                score += 10
                score += self.rolls[cursor+2]
                cursor += 2
            else:
                score += self.rolls[cursor] + self.rolls[cursor+1]
                cursor += 2
        return score

    def roll(self, pins):
        self.rolls[self.number_of_rolls] = pins
        self.number_of_rolls += 1

    def is_spare(self, cursor):
        return self.rolls[cursor] + self.rolls[cursor + 1] == 10
