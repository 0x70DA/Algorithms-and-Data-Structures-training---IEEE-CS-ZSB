'''HackerRank: Coder'''

if __name__ == '__main__':
    n = int(input())
    if n % 2 == 0:
        print(int(n * n / 2))
    else:
        print(int((n * n + 1) / 2))

    arr = ['C', '.'] * n
    for i in range(n):
        if i % 2 == 1:
            print(*arr[1:n+1], sep='')
        else:
            print(*arr[:n], sep='')
