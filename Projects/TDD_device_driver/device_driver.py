from hardware_interface import FlashMemoryDevice


class DeviceDriver:
    """
    This class is used by the operating system to interact with the hardware 'FlashMemoryDevice'.
    """

    def __init__(self, device: FlashMemoryDevice):
        """
        :type device: hardware_interface.FlashMemoryDevice
        """
        self._device = device

    def write(self, address: int, data: int) -> None:
        # TODO: implement this method
        self._device.write(address, data)

    def write_all(self, data: int) -> None:
        addresses = [0x00, 0x01, 0x02, 0x03, 0x04]
        [self._device.write(addr, data) for addr in addresses]

    def read(self, address: int) -> int:
        # TODO: implement this method
        first_read = self._device.read(address)
        self.assert_all_same(address, first_read)
        return first_read

    def assert_all_same(self, address, ret):
        for i in range(4):
            if ret != self._device.read(address):
                raise Exception()


