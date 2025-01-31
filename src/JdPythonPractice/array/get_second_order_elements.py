def get_second_order_elements(n: int, a: list[int]) -> list[int]:
    max_value = a[0]
    max_value_2 = None
    min_value = a[0]
    min_value_2 = None
    for i in range(n):
        if a[i] > max_value:
            max_value_2 = max_value
            max_value = a[i]
        elif max_value_2 is None and a[i] != max_value:
            max_value_2 = a[i]
        elif max_value_2 is not None and a[i] > max_value_2 and a[i] != max_value:
            max_value_2 = a[i]
        if a[i] < min_value:
            min_value_2 = min_value
            min_value = a[i]
        elif min_value_2 is None and a[i] != min_value:
            min_value_2 = a[i]
        elif min_value_2 is not None and a[i] < min_value_2 and a[i] != min_value:
            min_value_2 = a[i]

    return [max_value_2, min_value_2]
