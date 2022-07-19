def largest_concatenate(arr):
    result = ''
    while arr:
        max_num = max(arr)
        result += str(max_num)
        del arr[arr.index(max_num)]

    return result


def main():
    arr = list(map(int, input().split()))
    print(largest_concatenate(arr))


if __name__ == '__main__':
    main()
