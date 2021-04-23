import math


def square_root(a):
    """ Return 9-decimal place result if the result is less than 10
        otherwise return 8-decimal place result
    """
    result = math.sqrt(a)

    if result < 10:
        place = 9
    else:
        place = 8

    return round(result, place)
