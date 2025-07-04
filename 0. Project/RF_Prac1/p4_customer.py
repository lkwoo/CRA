from p4_rental import Rental
from p4_movie import Movie


class Customer:
    def __init__(self, name: str):
        self._rentals = []
        self._name = name

    @property
    def get_name(self):
        return self._name

    def add_rental(self, param: Rental):
        self._rentals.append(param)

    @property
    def total_amount(self):
        total_amount = 0
        for rental in self._rentals:
            total_amount += rental.get_amount()

        return total_amount

    @property
    def frequent_renter_points(self):
        frequent_renter_points = 0
        for rental in self._rentals:
            frequent_renter_points += rental.get_frequent_renter_points()

        return frequent_renter_points

    def get_results(self):
        result = ""
        for rental in self._rentals:
            result += rental.get_result()
        return result

    def statement(self):
        result = f"Rental Record for {self.get_name}\n"
        result += self.get_results()
        result += f"Amount owed is {str(self.total_amount)}\n"
        result += f"You earned {str(self.frequent_renter_points)} frequent renter points"

        return result


