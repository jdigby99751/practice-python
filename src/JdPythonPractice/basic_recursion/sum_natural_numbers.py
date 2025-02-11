def sum_natural_numbers(n: int):
    if n == 1:
        return 1
    return n + sum_natural_numbers(n-1)


if __name__ == "__main__":
    print(sum_natural_numbers(10))  # 55
    print(sum_natural_numbers(6))  # 21