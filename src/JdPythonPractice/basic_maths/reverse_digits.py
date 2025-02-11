def reverse_digits(n: int) -> int:
    """
    Reverse the digits of a number
    """
    reversed_number = 0
    while n > 0:
        remainder = n % 10
        reversed_number = reversed_number * 10 + remainder
        n = n // 10
    return reversed_number
    # return int(str(n)[::-1])


if __name__ == "__main__":
    print(reverse_digits(1234))  # 4321
