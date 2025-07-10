from abc import ABC, abstractmethod


class Notifier(ABC):
    @abstractmethod
    def alarm(self, weather_conditions):
        ...


class Emailer(Notifier):
    def alarm(self, weather_conditions):
        self.generate_weather_alert(weather_conditions)

    def generate_weather_alert(self, weather_conditions: str):
        if weather_conditions == 'sunny':
            alert = 'It is ' + weather_conditions
            print(alert)


class Phone(Notifier):
    def generate_weather_alert(self, weather_conditions: str):
        if weather_conditions == 'rainy':
            print('It is ' + weather_conditions)

    def alarm(self, weather_conditions):
        self.generate_weather_alert(weather_conditions)


class WeatherTracker:
    def __init__(self) -> None:
        super().__init__()
        self.__current_conditions = ""
        self._notifiers: list[Notifier] = [Phone(), Emailer()]

    def set_current_conditions(self, weather_description: str) -> None:
        self.__current_conditions = weather_description

    def notify(self):
        for notifier in self._notifiers:
            notifier.alarm(self.__current_conditions)