'''HackerRank: Beautiful Matrix'''

if __name__ == '__main__':
    arr = [list(map(int, input().split())) for _ in range(5)]
    for i in range(5):
        for j in range(5):
            if arr[i][j] == 1:
                d = abs(i - 2) + abs(j - 2)
                print(d)
                break
