def count_digits(n: int) -> int:
    """
    Count the number of digits in a number
    """
    return len(str(n))


if __name__ == "__main__":
    print(count_digits(1234))  # 4
    print(count_digits(1234567890))  # 10
    print(count_digits(0))  # 1
    print(count_digits(
        123456789012345678901234567890123456789012345678901234567890)
    )  # 60
