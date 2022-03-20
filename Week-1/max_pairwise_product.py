def max_pairwise_product(arr):
    max_1 = max(arr)
    del arr[arr.index(max_1)]
    max_2 = max(arr)
    return max_1 * max_2


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    res = max_pairwise_product(arr)
    print(res)
