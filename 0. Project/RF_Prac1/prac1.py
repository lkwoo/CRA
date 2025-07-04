import pytest


class Player:
    def __init__(self, level, hp ,mp, name):
        self.__level = level
        self.__hp = hp
        self.__mp = mp
        self.__name = name

    def level_up(self):
        self.__hp += 10
        self.__mp -= 20
        self.__level += 1

    def get_level(self):
        return self.__level

    def get_hp(self):
        return self.__hp

    def get_mp(self):
        return self.__mp

    def get_name(self):
        return self.__name


def test_game_player_effect():
    p = Player(10, 180, 200, "hwan")
    p.level_up()

    assert p.get_hp() == 190
    assert p.get_mp() == 180
    assert p.get_level() == 11
