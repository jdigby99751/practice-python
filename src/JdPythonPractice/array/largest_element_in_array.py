from sys import *
from collections import *
from math import *


def largest_element(arr: list, n: int) -> int:
    max_value = arr[0]
    for item in arr:
        if item > max_value:
            max_value = item
    return max_value


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    print(largest_element(arr, n))
