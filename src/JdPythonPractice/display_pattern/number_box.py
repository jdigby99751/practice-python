def print_number_box(n: int) -> None:
    for i in range(n+(n-1)):
        if i >= n:
            abs_i = abs(n-i-2)
        else:
            abs_i = abs(n-i)
        for j in range(n+(n-1)):
            if j >= n:
                abs_j = abs(n-j-2)
            else:
                abs_j = abs(n-j)
            max_val = max(abs_i, abs_j)
            print(max_val, end=" ")
        print()


if __name__ == "__main__":
    for i in range(10):
        print_number_box(i)
