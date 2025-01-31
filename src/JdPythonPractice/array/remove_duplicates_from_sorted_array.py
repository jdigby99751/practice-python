def remove_duplicates(arr: list[int]) -> int:
    i = 0
    for j in range(1, len(arr)):
        if arr[i] != arr[j]:
            i += 1
            arr[i] = arr[j]

    del arr[i + 1:]
    return i + 1

