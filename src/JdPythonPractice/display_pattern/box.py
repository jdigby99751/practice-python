def print_box(n: int) -> None:
    for i in range(n):
        if i == 0 or i == n-1:
            for j in range(n):
                print("*", end=" ")
            print()
        else:
            for j in range(n):
                if j == 0 or j == n-1:
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()


if __name__ == "__main__":
    print_box(5)
