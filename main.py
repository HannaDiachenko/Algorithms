from sorts.bubble_sort import bubble_sort
from sorts.merge_sort import merge_sort
from sorts.quick_sort import quick_sort

in_data = input("Print values (<1000) for sort\n")
data = in_data.split()

algorithm = int(input("Choose sorting algorithm\n"
                      "1 - bubble sort\n"
                      "2 - merge sort\n"
                      "3 - quick sort\n"))


class InvalidType(Exception):
    pass


def is_int(values):
    if values.isalpha():
        raise InvalidType("Value is not a number")
    else:
        return True


data = [int(d) for d in data if is_int(d)]


def choose_sort(alg: int):
    if alg == 1:
        return bubble_sort(data)
    elif alg == 2:
        return merge_sort(data)
    elif alg == 3:
        return quick_sort(data)
    else:
        return "Wrong choice"


print(choose_sort(algorithm))
