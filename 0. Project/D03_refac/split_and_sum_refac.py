def split_and_sum(text: str):
    if (not isinstance(text, str)) or len(text) == 0:
        result = 0

    values = split(text)
    values = str_to_digit(values)
    return sum_list(values)


def split(text: str):
    return text.split("-")


def str_to_digit(lst):
    return [int(s) for s in lst if s.isdigit()]


def sum_list(lst: list[int]):
    return sum(lst)


ret = split_and_sum("0-1-2-3-4-5")
print(ret)
