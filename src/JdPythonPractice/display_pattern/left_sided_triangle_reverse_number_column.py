def print_left_sided_triangle_reverse_number_column(n: int) -> None:
    j_range = n + 1
    for i in range(n):
        j_range -= 1
        for j in range(j_range):
            print(j + 1, end=" ")
        print()


if __name__ == "__main__":
    print_left_sided_triangle_reverse_number_column(5)
