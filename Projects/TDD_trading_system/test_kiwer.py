import pytest
from pytest_mock import MockerFixture
from kiwer_api import KiwerAPI
from nemo_api import NemoAPI


def test_read_five_times(mocker: MockerFixture):
    kiwer_mock = mocker.Mock()
    driver = DeviceDriver(hardware_mock)

    driver.read(0x5E)

    assert hardware_mock.read.call_count == 5


def test_read_successful(mocker: MockerFixture):
    hardware_mock = mocker.Mock(spec=FlashMemoryDevice)
    driver = DeviceDriver(hardware_mock)

    hardware_mock.read.side_effect = [10, 10, 10, 10, 10]

    ret = driver.read(0x5E)

    assert ret == 10


@pytest.mark.parametrize("lst", [
    (10, 10, 10, 10, 5),
    (10, 10, 5, 10, 10)
])
def test_read_failure(mocker: MockerFixture, lst):
    hardware_mock = mocker.Mock(spec=FlashMemoryDevice)
    driver = DeviceDriver(hardware_mock)

    hardware_mock.read.side_effect = lst

    with pytest.raises(Exception):
        driver.read(0x5E)


def test_write_success(mocker: MockerFixture):
    hardware_mock = mocker.Mock(spec=FlashMemoryDevice)
    driver = DeviceDriver(hardware_mock)

    hardware_mock.read.return_value = 0xFF
    driver.write(0x5E, 10)
    hardware_mock.write.assert_called_once()


def test_read_once_when_write(mocker: MockerFixture):
    hardware_mock = mocker.Mock(spec=FlashMemoryDevice)
    driver = DeviceDriver(hardware_mock)

    hardware_mock.read.return_value = 0xFF

    driver.write(0x5E, 10)

    hardware_mock.read.assert_called_once()  # 5번 read 됨


from pytest_mock import MockerFixture

from device_driver import DeviceDriver


class App:
    def __init__(self, device_driver):
        self.device_driver = device_driver

    def read_and_print(self, start_addr, end_addr):
        for addr in range(start_addr, end_addr + 1):
            print(self.device_driver.read(addr))

    def write_all(self, value):
        for addr in range(0x00, 0x04 + 1):
            self.device_driver.write(addr, value)


from unittest.mock import call


def test_read_all_address(mocker: MockerFixture):
    mock_device_driver = mocker.Mock(spec=DeviceDriver)
    app = App(mock_device_driver)

    app.read_and_print(0, 3)

    expected_call = [call(0), call(1), call(2), call(3)]
    mock_device_driver.read.assert_has_calls(expected_call, any_order=True)


def test_read_and_print(capsys, mocker: MockerFixture):
    mock_device_driver = mocker.Mock(spec=DeviceDriver)
    app = App(mock_device_driver)

    def func(a):
        if a == 0: return 5
        if a == 1: return 7
        if a == 2: return 8
        return ValueError

    mock_device_driver.read.side_effect = func

    app.read_and_print(0, 2)

    captured = capsys.readouterr()
    assert "5\n7\n8\n" == captured.out


def test_write_all(mocker: MockerFixture):
    mock_device_driver = mocker.Mock(spec=DeviceDriver)
    app = App(mock_device_driver)

    app.write_all(10)

    expected_call = [call(addr, 10) for addr in range(0x00, 0x04 + 1)]
    mock_device_driver.write.assert_has_calls(expected_call)
