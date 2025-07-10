import io
import random
import sys
from random import randrange

from Game import Game
from GameBetter import GameBetter
from IGame import IGame


def play_game(game: IGame, seed_num) -> str:
    # buffer
    output = io.StringIO()
    origin_stdout = sys.stdout
    sys.stdout = output

    try:
        not_a_winner = False

        game.add('Chet')
        game.add('Pat')
        game.add('Sue')

        random.seed(seed_num)

        while True:
            roll = randrange(6) + 1
            game.rolling(roll)

            if randrange(9) == 7:
                not_a_winner = game.wrong_answer()
            else:
                not_a_winner = game.was_correctly_answered()

            if not not_a_winner: break
    finally:
        sys.stdout = origin_stdout

    return output.getvalue()


def test_():
    assert play_game(Game(), 1) == play_game(GameBetter(), 1)
    assert play_game(Game(), 2) == play_game(GameBetter(), 2)
    assert play_game(Game(), 5) == play_game(GameBetter(), 5)
    assert play_game(Game(), 9) == play_game(GameBetter(), 9)
    assert play_game(Game(), 111) == play_game(GameBetter(), 111)
