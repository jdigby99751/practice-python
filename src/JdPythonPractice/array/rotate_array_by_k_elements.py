def rotate_array(n: int, a: list[int], k: int = 1, dir: str = "right") -> list[int]:
    if dir == "right":
        return a[n - k:] + a[0:n - k]

    elif dir == "left":
        return a[k:] + a[0:k]
