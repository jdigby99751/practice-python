def print_triangle_reverse(n: int) -> None:
    number_stars = n + n + 1
    for i in range(n):
        number_stars -= 2
        number_blanks = i
        for j in range(number_blanks):
            print(" ", end=" ")
        for j in range(number_stars):
            print("*", end=" ")
        print()


if __name__ == "__main__":
    print_triangle_reverse(5)
