def print_triangle(n: int) -> None:
    number_stars = -1
    for i in range(n):
        number_stars += 2
        number_blanks = n - i - 1
        for j in range(number_blanks):
            print(" ", end=" ")
        for j in range(number_stars):
            print("*", end=" ")
        print()


if __name__ == "__main__":
    print_triangle(5)
