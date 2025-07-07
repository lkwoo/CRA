from random import randrange


class Player:
    def __init__(self, name):
        self._name = name
        self._place = 0
        self._purse = 0
        self._in_penalty_box = False

    def get_coin(self):
        self._purse += 1
        print(f'{self._name} now has '
              f'{self._purse} Gold Coins.')

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def place(self):
        return self._place

    @place.setter
    def place(self, place):
        self._place = place

    @property
    def purse(self):
        return self._purse

    @purse.setter
    def purse(self, purse):
        self._purse = purse

    @property
    def in_penalty_box(self):
        return self._in_penalty_box

    @in_penalty_box.setter
    def in_penalty_box(self, val):
        self._in_penalty_box = val

    def move_player(self, roll):
        self._place = self._place + roll
        if self._place > 11:
            self._place = self._place - 12


class GameBetter:
    def __init__(self):
        self.players: list[Player] = []

        self.pop_questions = []
        self.science_questions = []
        self.sports_questions = []
        self.rock_questions = []

        self.current_player = 0

        for i in range(50):
            self.pop_questions.append(f'Pop Question {i}')
            self.science_questions.append(f'Science Question {i}')
            self.sports_questions.append(f'Sports Question {i}')
            self.rock_questions.append(f'Rock Question {i}')

    def get_current_player(self):
        return self.players[self.current_player]

    def next_player(self):
        self.current_player += 1
        if self.current_player == len(self.players):
            self.current_player = 0

    @property
    def is_playable(self):
        return self.how_many_players >= 2

    def add(self, player_name):
        self.players.append(Player(player_name))

        print(player_name + ' was added')
        print(f'They are player number {len(self.players)}')

        return True

    @property
    def how_many_players(self):
        return len(self.players)

    def rolling(self, roll: int):
        current_player = self.get_current_player()
        print(f'{current_player.name} is the current player')
        print(f'They have rolled a {roll}')

        if current_player.in_penalty_box:
            if roll % 2 == 0:
                print(f'{current_player.name} is not getting out of the penalty box')
                return
            else:
                print(f'{current_player.name} is getting out of the penalty box')

        current_player.move_player(roll)

        print(f'{current_player.name}\'s new location is '
              f'{current_player.place}')

        print(f'The category is {self._current_category}')
        self._ask_question()

    def _ask_question(self):
        if self._current_category == 'Pop':
            print(self.pop_questions.pop(0))
        if self._current_category == 'Science':
            print(self.science_questions.pop(0))
        if self._current_category == 'Sports':
            print(self.sports_questions.pop(0))
        if self._current_category == 'Rock':
            print(self.rock_questions.pop(0))

    @property
    def _current_category(self):
        current_player = self.get_current_player()
        if current_player.place in [0, 4, 8]:
            return 'Pop'
        if current_player.place in [1, 5, 9]:
            return 'Science'
        if current_player.place in [2, 6, 10]:
            return 'Sports'

        return 'Rock'

    def was_correctly_answered(self):
        current_player = self.get_current_player()
        if not current_player.in_penalty_box:
            print('Answer was correct!!!!')
            current_player.get_coin()

        winner = self._did_player_win()
        self.next_player()

        return winner

    def wrong_answer(self):
        current_player = self.get_current_player()
        if not current_player.in_penalty_box:
            print('Question was incorrectly answered')
            print(current_player.name + ' was sent to the penalty box')
            current_player.in_penalty_box = True

        self.next_player()
        return False

    def _did_player_win(self):
        current_player = self.get_current_player()
        return current_player.purse == 6


if __name__ == '__main__':
    not_a_winner = False

    game = GameBetter()

    game.add('Chet')
    game.add('Pat')
    game.add('Sue')

    while True:
        roll = randrange(6) + 1
        game.rolling(roll)

        if randrange(9) == 7:
            a_winner = game.wrong_answer()
        else:
            a_winner = game.was_correctly_answered()

        if not_a_winner:
            break
