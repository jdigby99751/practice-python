def print_negative_triangle(n: int) -> None:
    for i in range(n-1, 0, -1):
        for j in range(n-i):
            print("*", end=" ")
        for j in range(i):
            print(" ", end=" ")
        for j in range(i):
            print(" ", end=" ")
        for j in range(n-i):
            print("*", end=" ")
        print()
    for i in range(n):
        for j in range(n-i):
            print("*", end=" ")
        for j in range(i):
            print(" ", end=" ")
        for j in range(i):
            print(" ", end=" ")
        for j in range(n-i):
            print("*", end=" ")
        print()


if __name__ == "__main__":
    print_negative_triangle(5)
