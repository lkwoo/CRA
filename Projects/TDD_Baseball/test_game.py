import pytest
from game import Game


@pytest.fixture
def game():
    return Game()


def assert_illegal_argument(game, guess_num):
    with pytest.raises(TypeError):
        game.guess(guess_num)


def assert_matched_number(res, solved, strikes, balls):
    assert res.solved == solved
    assert res.strikes == strikes
    assert res.balls == balls


@pytest.mark.parametrize("invalid_input", [None, "12", "1234", "122", "12e"])
def test_exception_when_input_length_unmatch(game, invalid_input):
    assert_illegal_argument(game, invalid_input)


def test_return_success(game):
    game.question = "123"
    assert_matched_number(game.guess("123"), solved=True, strikes=3, balls=0)


def test_return_fail(game):
    game.question = "123"
    assert_matched_number(game.guess("456"), solved=False, strikes=0, balls=0)


def test_0_strikes_0_ball(game):
    game.question = "527"
    assert_matched_number(game.guess("136"), solved=False, strikes=0, balls=0)

    game.question = "369"
    assert_matched_number(game.guess("125"), solved=False, strikes=0, balls=0)

    game.question = "098"
    assert_matched_number(game.guess("345"), solved=False, strikes=0, balls=0)


def test_0_strikes_1_ball(game):
    game.question = "527"
    assert_matched_number(game.guess("713"), solved=False, strikes=0, balls=1)

    game.question = "369"
    assert_matched_number(game.guess("987"), solved=False, strikes=0, balls=1)

    game.question = "098"
    assert_matched_number(game.guess("102"), solved=False, strikes=0, balls=1)


def test_0_strikes_2_ball(game):
    game.question = "527"
    assert_matched_number(game.guess("712"), solved=False, strikes=0, balls=2)

    game.question = "369"
    assert_matched_number(game.guess("983"), solved=False, strikes=0, balls=2)

    game.question = "098"
    assert_matched_number(game.guess("109"), solved=False, strikes=0, balls=2)


def test_1_strikes_0_ball(game):
    game.question = "527"
    assert_matched_number(game.guess("536"), solved=False, strikes=1, balls=0)

    game.question = "369"
    assert_matched_number(game.guess("325"), solved=False, strikes=1, balls=0)

    game.question = "098"
    assert_matched_number(game.guess("045"), solved=False, strikes=1, balls=0)


def test_1_strikes_1_ball(game):
    game.question = "527"
    assert_matched_number(game.guess("573"), solved=False, strikes=1, balls=1)

    game.question = "369"
    assert_matched_number(game.guess("619"), solved=False, strikes=1, balls=1)

    game.question = "098"
    assert_matched_number(game.guess("891"), solved=False, strikes=1, balls=1)


def test_1_strikes_2_ball(game):
    game.question = "527"
    assert_matched_number(game.guess("572"), solved=False, strikes=1, balls=2)

    game.question = "369"
    assert_matched_number(game.guess("639"), solved=False, strikes=1, balls=2)

    game.question = "098"
    assert_matched_number(game.guess("890"), solved=False, strikes=1, balls=2)



def test_2_strikes_0_ball(game):
    game.question = "527"
    assert_matched_number(game.guess("528"), solved=False, strikes=2, balls=0)

    game.question = "369"
    assert_matched_number(game.guess("359"), solved=False, strikes=2, balls=0)

    game.question = "098"
    assert_matched_number(game.guess("198"), solved=False, strikes=2, balls=0)


def test_3_strikes_0_ball(game):
    game.question = "527"
    assert_matched_number(game.guess("527"), solved=True, strikes=3, balls=0)

    game.question = "369"
    assert_matched_number(game.guess("369"), solved=True, strikes=3, balls=0)

    game.question = "098"
    assert_matched_number(game.guess("098"), solved=True, strikes=3, balls=0)


