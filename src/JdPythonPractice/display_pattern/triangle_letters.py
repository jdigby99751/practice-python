def print_triangle_letters(n: int) -> None:
    number_letters = -1
    for i in range(n):
        number_letters += 2
        number_blanks = n - i - 1
        for j in range(number_blanks):
            print(" ", end=" ")
        for j in range(i):
            print(chr(ord("A")+j), end=" ")
        for j in range(number_letters-i, 0, -1):
            print(chr(ord("A")+j-1), end=" ")
        print()


if __name__ == "__main__":
    print_triangle_letters(5)
