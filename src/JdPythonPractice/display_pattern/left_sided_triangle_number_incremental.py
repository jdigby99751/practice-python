def print_left_sided_triangle_number_incremental(n: int) -> None:
    j_range = 0
    number_to_print = 0
    for i in range(n):
        j_range += 1
        for j in range(j_range):
            number_to_print += 1
            print(number_to_print, end=" ")
        print()


if __name__ == "__main__":
    print_left_sided_triangle_number_incremental(5)
