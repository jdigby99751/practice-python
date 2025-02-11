import math


def divisors(n: int) -> list[int]:
    """
    Checks if a number is a palindrome
    """
    # num_digits = len(str(n))
    # check_value = 0
    # for digit in str(n):
    #     check_value += int(digit) ** num_digits

    divisors = []
    divisors_second_half = []

    for i in range(1, math.floor(math.sqrt(n))+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors_second_half.append(n // i)

    divisors_second_half.reverse()
    divisors.extend(divisors_second_half)

    return divisors


if __name__ == "__main__":
    print(divisors(1234))  # false
    print(divisors(12321))  # true
