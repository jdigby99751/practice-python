def missing_number(a: list[int]) -> int:
    j = 0
    for i in range(0, len(a)):
        j += 1
        if a[i] != j:
            return j
    return j + 1


def missing_number_xor(a: list[int]) -> int:
    xor1 = 0
    xor2 = 0
    for i in range(len(a)):
        xor2 ^= a[i]
        xor1 ^= i + 1

    xor1 ^= len(a) + 1

    return xor1 ^ xor2
