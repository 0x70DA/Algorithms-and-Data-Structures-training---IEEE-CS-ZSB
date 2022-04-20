def fib(n):
    lst = [0, 1]
    for i in range(2, n):
        lst.append(lst[i-1] + lst[i-2])
        
    return lst[n-1]


def main():
    n = int(input())
    print(fib(n))


if __name__ == '__main__':
    main()
