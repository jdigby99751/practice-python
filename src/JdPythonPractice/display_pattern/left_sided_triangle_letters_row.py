def print_left_sided_triangle_letters_row(n: int) -> None:
    j_range = 0
    for i in range(n):
        j_range += 1
        for j in range(j_range):
            print(chr(ord("A")+i), end=" ")
        print()


if __name__ == "__main__":
    print_left_sided_triangle_letters_row(5)
