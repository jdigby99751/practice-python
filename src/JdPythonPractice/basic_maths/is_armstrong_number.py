import math


def is_armstrong_number(n: int) -> bool:
    """
    Checks if a number is a palindrome
    """
    # num_digits = len(str(n))
    # check_value = 0
    # for digit in str(n):
    #     check_value += int(digit) ** num_digits

    num_digits = count_digits(n)
    check_value = 0
    for digit in extract_digits(n):
        check_value += digit ** num_digits

    if check_value == n:
        return True
    return False


def count_digits(n: int) -> int:
    """
    Count the number of digits in a number
    """
    if n == 0:
        return 1
    return int(math.log10(n) + 1)


def extract_digits(n: int) -> list[int]:
    """
    Gets the digits as a list
    """
    digits = []
    # for digit in str(n):
    #     digits.append(int(digit))

    while n > 0:
        digit = n % 10
        digits.append(digit)
        n = math.floor(n / 10)
    digits.reverse()
    return digits


if __name__ == "__main__":
    print(is_armstrong_number(1234))  # false
    print(is_armstrong_number(12321))  # true
