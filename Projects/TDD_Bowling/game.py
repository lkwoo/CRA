class Game:
    def __init__(self):
        self._history = []

    def roll(self, pin_cnt):
        self._history.append(pin_cnt)

    def score(self):
        score = 0
        round_num = 0
        left = 10
        roll_cnt = 0

        for i, pin_cnt in enumerate(self._history):
            left -= pin_cnt
            roll_cnt += 1

            # strike
            if roll_cnt == 1 and left <= 0:
                left = 10
                roll_cnt = 0
                round_num += 1
                if round_num < 10:
                    if i + 1 < len(self._history):
                        score += self._history[i + 1]
                    if i + 2 < len(self._history):
                        score += self._history[i + 2]

            # spare
            elif roll_cnt == 2 and left <= 0:
                left = 10
                roll_cnt = 0
                round_num += 1
                if round_num < 10:
                    if i + 1 < len(self._history):
                        score += self._history[i + 1]

            if roll_cnt == 2:
                round_num += 1
                roll_cnt = 0
                left = 10

            score += pin_cnt
            print(f'{i}: {score}')

        return score
