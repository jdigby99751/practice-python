def print_left_right_triangles_numbers(n: int) -> None:
    for i in range(n):
        number_to_print = 0
        number_stars = i + 1
        number_blanks = n - i - 1
        for j in range(number_stars):
            number_to_print += 1
            print(number_to_print, end=" ")
        for j in range(number_blanks):
            print(" ", end=" ")
        for j in range(number_blanks):
            print(" ", end=" ")
        for j in range(number_stars):
            print(number_to_print, end=" ")
            number_to_print -= 1            
        print()


if __name__ == "__main__":
    print_left_right_triangles_numbers(5)
