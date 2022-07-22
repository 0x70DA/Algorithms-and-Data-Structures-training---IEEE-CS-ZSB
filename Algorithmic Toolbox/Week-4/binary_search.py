def binary_search(arr, value, left, right):
    index = None
    if left <= right:
        mid = (left + right) // 2
        if value > arr[mid]:
            left = mid + 1
            index = binary_search(arr, value, left, right)
        elif value < arr[mid]:
            right = mid - 1
            index = binary_search(arr, value, left, right)
        else:
            index = mid

    return index


if __name__ == '__main__':
    arr = list(map(int, input().split()))
    value = int(input())
    left = 0
    right = len(arr) - 1
    print(binary_search(arr, value, left, right))
