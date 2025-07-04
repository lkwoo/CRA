from SOLID_2_OCP_vehicle import Vehicle, DrivingMode
from abc import ABC, abstractmethod


class DrivingMode(ABC):
    @abstractmethod
    def change_driving_mode(self, vehicle: Vehicle):
        ...


class SportMode(DrivingMode):
    def change_driving_mode(self, vehicle):
        vehicle.set_power(500)
        vehicle.set_suspension_height(10)


class ComportMode(DrivingMode):
    def change_driving_mode(self, vehicle):
        vehicle.set_power(400)
        vehicle.set_suspension_height(20)


class DefaultMode(DrivingMode):
    def change_driving_mode(self, vehicle):
        vehicle.set_power(400)
        vehicle.set_suspension_height(20)


class EventHandler:
    def __init__(self, vehicle:Vehicle) -> None:
        super().__init__()
        self.__vehicle = vehicle

    def change_driving_mode(self, driving_mode: DrivingMode):
        driving_mode.change_driving_mode(self.__vehicle)

        # when we need to add another mode (e.g. ECONOMY) 2 classes will change DrivingMode and EventHandler.


def test_comport():
    v = Vehicle()
    h = EventHandler(v)

    h.change_driving_mode(ComportMode())
    assert v.get_power() == 400 and v.get_suspension_height() == 20


def test_sport():
    v = Vehicle()
    h = EventHandler(v)

    h.change_driving_mode(SportMode())
    assert v.get_power() == 500 and v.get_suspension_height() == 10


def test_default():
    v = Vehicle()
    h = EventHandler(v)

    h.change_driving_mode(DefaultMode())
    assert v.get_power() == 400 and v.get_suspension_height() == 20