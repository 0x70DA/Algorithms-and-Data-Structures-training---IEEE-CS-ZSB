'''HackerRank: Nastya and an Array'''

if __name__ == '__main__':
    _ = int(input())
    arr = set(map(int, input().split()))
    arr = list(arr)
    print(len(arr) - arr.count(0))
