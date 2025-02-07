def print_left_right_triangles(n: int) -> None:
    for i in range(n):
        number_stars = i + 1
        number_blanks = n - i - 1
        for j in range(number_stars):
            print("*", end=" ")
        for j in range(number_blanks):
            print(" ", end=" ")
        for j in range(number_blanks):
            print(" ", end=" ")
        for j in range(number_stars):
            print("*", end=" ")
        print()


if __name__ == "__main__":
    print_left_right_triangles(5)
