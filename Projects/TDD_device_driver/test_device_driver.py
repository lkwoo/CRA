import pytest
from pytest_mock import MockerFixture

import hardware_interface
from hardware_interface import FlashMemoryDevice
from device_driver import DeviceDriver


def test_read_five_times(mocker: MockerFixture):
    hardware_mock = mocker.Mock()
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
    ...
