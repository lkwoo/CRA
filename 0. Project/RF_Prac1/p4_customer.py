from p4_rental import Rental
from p4_movie import Movie


class Customer:
    def __init__(self, name: str):
        self._rentals = []
        self._name = name

    @property
    def get_name(self):
        return self._name

    def statement(self):
        total_amount = 0
        frequent_renter_points = 0
        result = f"Rental Record for {self.get_name}\n"

        for rental in self._rentals:
            this_amount = rental.get_amount()
            frequent_renter_points += rental.get_frequent_renter_points()

            # show figures for this rental
            result += rental.get_result()
            total_amount += this_amount

        # add footer lines
        result += f"Amount owed is {str(total_amount)}\n"
        result += f"You earned {str(frequent_renter_points)} frequent renter points"

        return result

    def add_rental(self, param: Rental):
        self._rentals.append(param)
