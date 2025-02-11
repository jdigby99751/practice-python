import math


def is_prime(n: int) -> bool:
    """
    Checks if a number is a prime number
    """
    if n == 1:
        return False

    for i in range(2, math.floor(math.sqrt(n))+1):
        if n % i == 0:
            return False

    return True


if __name__ == "__main__":
    print(is_prime(10))  # false
    print(is_prime(19))  # true
