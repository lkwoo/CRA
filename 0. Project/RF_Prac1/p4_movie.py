class Movie:
    CHILDREN = 2
    NEW_RELEASE = 1
    REGULAR = 0

    def __init__(self, title: str, price_code: int) -> None:
        self._title = title
        self._price_code = price_code

    @property
    def price_code(self) -> int:
        return self._price_code

    @price_code.setter
    def price_code(self, price_code: int) -> None:
        self._price_code = price_code

    @property
    def get_title(self) -> str:
        return self._title
