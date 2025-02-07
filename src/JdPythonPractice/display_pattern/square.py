def print_square(n: int) -> None:
    for i in range(n):
        for j in range(n):
            print("*", end=" ")
        print()


if __name__ == "__main__":
    print_square(5)
