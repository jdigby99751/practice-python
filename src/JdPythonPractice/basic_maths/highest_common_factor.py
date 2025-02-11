def hcf(n: int, m: int) -> int:
    """
    Finds the highest common factor of two numbers
    """
    # max_num = max(n, m)
    # min_num = min(n, m)
    # diff = max_num - min_num
    # if diff == 0:
    #     # print(f"returning {max_num}")
    #     return max_num
    # if diff < 0:
    #     raise ValueError("No common factor")
    # else:
    #     return hcf(min_num, diff)

    while n > 0 and m > 0:
        if n > m:
            n = n % m
        else:
            m = m % n
    if n == 0:
        return m
    return n


if __name__ == "__main__":
    print(hcf(9, 12))  # 3
    print(hcf(17, 23))  # 1
