'''HackerRank: Insertion Sort - Part 1'''


def insertionSort1(n, arr):
    i = n - 1
    x = arr[i]
    while(i > 0 and x < arr[i-1]):
        arr[i] = arr[i-1]
        print(*arr)
        i -= 1

    arr[i] = x
    print(*arr)


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
