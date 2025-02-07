def print_left_sided_triangle_reverse_letters(n: int) -> None:
    j_range = n + 1
    for i in range(n):
        j_range -= 1
        for j in range(j_range):
            print(chr(ord("A")+j), end=" ")
        print()


if __name__ == "__main__":
    print_left_sided_triangle_reverse_letters(5)
