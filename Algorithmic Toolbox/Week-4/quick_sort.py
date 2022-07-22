import sys
from numpy import random


def partition(arr, p, q):
    i = p
    pivot = arr[p]
    for j in range(p + 1, q):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[p], arr[i] = arr[i], arr[p]
    return i


def quick_sort(arr, p, r):
    if p < r:
        q = partition(arr, p, r)
        quick_sort(arr, p, q - 1)
        quick_sort(arr, q + 1, r)


def main(arr_size):
    arr = random.randint(-arr_size, arr_size, size=arr_size)
    quick_sort(arr, 0, len(arr))
    print(arr)


if __name__ == '__main__':
    if len(sys.argv) == 2:
        main(int(sys.argv[1]))
    else:
        sys.exit("Usage: python quick_sort.py [size of array]")
