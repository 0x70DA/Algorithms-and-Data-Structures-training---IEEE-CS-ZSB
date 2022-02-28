'''HackerRank: Mishka and Contest'''

if __name__ == '__main__':
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    count = 0
    while len(arr) > 0:
        if arr[0] <= k:
            count += 1
            del arr[0]
        elif arr[-1] <= k:
            count += 1
            del arr[-1]
        else:
            break

    print(count)
