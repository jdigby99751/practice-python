def print_left_sided_triangle_boolean_numbers(n: int) -> None:
    j_range = 0
    for i in range(n):
        if i % 2 == 0:
            boolean_value = 0
        else:
            boolean_value = 1
        j_range += 1
        for j in range(j_range):
            if boolean_value:
                boolean_value = 0
            else:
                boolean_value = 1
            print(boolean_value, end=" ")
        print()


if __name__ == "__main__":
    print_left_sided_triangle_boolean_numbers(5)
