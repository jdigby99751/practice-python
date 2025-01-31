from sys import *
from collections import *
from math import *


def is_sorted(arr: list, n: int) -> int:
    for i in range(1, n):
        if arr[i] < arr[i-1]:
            return False
    return True


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    print(is_sorted(arr, n))
