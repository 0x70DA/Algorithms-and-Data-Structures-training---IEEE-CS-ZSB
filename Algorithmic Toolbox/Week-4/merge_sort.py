import sys
from numpy import random


def merge_sort(arr):
    if len(arr) > 1:

        left_array = arr[:len(arr) // 2].copy()  # from the start of the array to the half way point.
        right_array = arr[len(arr) // 2:].copy()  # from the half point to the end.
        # Recursivly sort the the two halves.
        merge_sort(left_array)
        merge_sort(right_array)

        # Merge the two arrays into the original array.
        i = j = k = 0
        while i < len(left_array) and j < len(right_array):
            if left_array[i] < right_array[j]:
                arr[k] = left_array[i]
                i += 1
            else:
                arr[k] = right_array[j]
                j += 1
            k += 1

        while i < len(left_array):
            arr[k] = left_array[i]
            i += 1
            k += 1

        while j < len(right_array):
            arr[k] = right_array[j]
            j += 1
            k += 1


def main(arr_size):
    arr = random.randint(-arr_size, arr_size, size=arr_size)
    merge_sort(arr)
    print(arr)


if __name__ == '__main__':
    if len(sys.argv) == 2:
        main(int(sys.argv[1]))
    else:
        sys.exit("Usage: python merge_sort.py [size of array]")
