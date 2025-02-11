import math


def count_digits(n: int) -> int:
    """
    Count the number of digits in a number
    """
    if n == 0:
        return 1
    return int(math.log10(n) + 1)

    # return len(str(n))


if __name__ == "__main__":
    count_digits(1234)  # 4
