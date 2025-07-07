class DeviceState:
    # cls.instance
    _instance = None

    # __new__
    def __new__(cls):
        if cls._instance is None:
            cls._instance = object.__new__(cls)
            cls._instance.connected = False
            cls._instance.battery_level = 100
            cls._instance.temperature = 25

        return cls._instance

    def connect(self):
        self.connected = True

    def disconnect(self):
        self.connected = False

    def update_battery_level(self, level):
        self.battery_level = level

    def update_temperature(self, temp):
        self.temperature = temp