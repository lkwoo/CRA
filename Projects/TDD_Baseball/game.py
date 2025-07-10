class GameResult:
    def __init__(self, solved, striks, balls):
        self._solved = solved
        self._strikes = striks
        self._balls = balls

    @property
    def solved(self):
        return self._solved

    @property
    def strikes(self):
        return self._strikes

    @property
    def balls(self):
        return self._balls

class Game:
    def __init__(self):
        self.question = ""

    @property
    def question(self):
        raise AttributeError("읽을 수 없는 속성")

    @question.setter
    def question(self, question):
        self._question = question

    def get_strikes(self, guess_num):
        return sum(1 for i in range(3) if guess_num[i] == self._question[i])

    def get_balls(self, guess_num):
        return sum(1 for i in range(3) if guess_num[i] != self._question[i] and guess_num[i] in self._question)

    def guess(self, guess_num: str) -> GameResult | None:
        if not (len(guess_num) == 3 and guess_num.isdigit() and len(set(guess_num)) == 3):
            raise TypeError()

        strikes = self.get_strikes(guess_num)
        balls = self.get_balls(guess_num)
        solved = strikes == 3

        return GameResult(solved, strikes, balls)
