def move_zeros(n: int, a: list[int]) -> list[int]:
    j = -1
    for i in range(n):
        if a[i] == 0:
            j = i
            break

    if j == -1:
        return a

    for i in range(j+1, n):
        if a[i] != 0:
            a[j], a[i] = a[i], a[j]
            j += 1

    return a
