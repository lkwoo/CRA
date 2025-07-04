from p4_movie import Movie


class Rental:
    def __init__(self, movie: Movie, days_rented: int) -> None:
        self._days_rented = days_rented
        self._movie = movie

    @property
    def get_days_rented(self) -> int:
        return self._days_rented

    def get_movie(self) -> Movie:
        return self._movie

    def get_price_code(self) -> int:
        return self._movie.price_code

    def get_amount(self) -> float:
        rental_days = self.get_days_rented
        amount = 0.0

        if self.get_price_code() == Movie.REGULAR:
            amount += 2
            if rental_days > 2:
                amount += (rental_days - 2) * 1.5
        elif self.get_price_code() == Movie.NEW_RELEASE:
            amount += rental_days * 3
        elif self.get_price_code() == Movie.CHILDREN:
            amount += 1.5
            if rental_days > 3:
                amount += (rental_days - 3) * 1.5

        return amount

    def get_frequent_renter_points(self) -> int:
        rental_days = self.get_days_rented

        frequent_renter_points = 1
        if (self.get_price_code() == Movie.NEW_RELEASE) and rental_days > 1:
            frequent_renter_points += 1

        return frequent_renter_points

    def get_result(self) -> str:
        return f"\t{self._movie.get_title}\t{str(self.get_amount())}\n"
