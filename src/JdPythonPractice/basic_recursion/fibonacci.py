def fibonacci_numbers(n: int, arr: list[int] = None):
    if not arr:
        arr = []
        arr.append(0)
        arr.append(1)

    if n == 1:
        return arr
    fibonacci_numbers(n-1, arr)
    arr.append(arr[-1] + arr[-2])
    return arr


def fibonacci(n: int):
    if n <= 1:
        return n
    last = fibonacci(n-1)
    second_last = fibonacci(n-2)
    return last + second_last


if __name__ == "__main__":

    print(fibonacci(5))  # 0 1 1 2 3 5
    print(fibonacci(6))  # 0 1 1 2 3 5 8

    print(fibonacci_numbers(5))  # 0 1 1 2 3 5
    print(fibonacci_numbers(6))  # 0 1 1 2 3 5 8
