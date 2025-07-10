from SOLID_4_ISP_bird import Bird, FlyBird


class Eagle(Bird, FlyBird):
    def __init__(self, initial_feather_count) -> None:
        super().__init__()
        self.__current_location = ""
        self.__number_of_feathers = initial_feather_count

    def fly(self):
        self.__current_location = "in the air"

    def molt(self):
        self.__number_of_feathers -= -1

    def get_feather_count(self):
        return self.__number_of_feathers

    def get_current_location(self):
        return self.__current_location


if __name__ == "__main__":
    eagle = Eagle(10)
    eagle.molt()
    eagle.fly()
    print(eagle.get_feather_count())
    print(eagle.get_current_location())