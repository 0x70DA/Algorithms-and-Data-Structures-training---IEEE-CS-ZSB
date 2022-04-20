n = int(input())
arr = list(map(int, input().split()))
first, second = 0, 0
for i in range(n):
    for j in range(i+1, n):
        if arr[i] * arr[j] > first * second:
            first = arr[i]
            second = arr[j]

print(first * second)
