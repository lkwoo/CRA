from SOLID_4_ISP_bird import Bird, SwimBird

class Penguin(Bird, SwimBird):
    def __init__(self, initial_feather_count) -> None:
        super().__init__()
        self.__current_location = ""
        self.__number_of_feathers = initial_feather_count

    # def fly(self):
    #     raise Exception('Unsupported Operation Exception')

    def molt(self):
        self.__number_of_feathers -= 1

    def swim(self):
        self.__current_location = "in the water"

    def get_feather_count(self):
        return self.__number_of_feathers

    def get_current_location(self):
        return self.__current_location


if __name__ == "__main__":
    penguin = Penguin(10)
    penguin.molt()
    penguin.swim()
    print(penguin.get_feather_count())
    print(penguin.get_current_location())