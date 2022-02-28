'''HackerRank: Andryusha and Socks'''

if __name__ == '__main__':
    n = int(input())
    socks = list(map(int, input().split()))
    arr = [0] * 2 * n
    count = 0
    current_max = 0
    for i in socks:
        arr[i] += 1
        if arr[i] == 2:
            count -= 1
        else:
            count += 1
        current_max = max(current_max, count)

    print(current_max)
