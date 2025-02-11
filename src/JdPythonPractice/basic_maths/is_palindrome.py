def is_palindrome(n: int) -> bool:
    """
    Checks if a number is a palindrome
    """
    # return n == int(str(n)[::-1])
    return n == reverse_digits(n)


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


if __name__ == "__main__":
    print(is_palindrome(1234))  # false
    print(is_palindrome(12321))  # true
