'''HackerRank: Brain's Photos'''
import sys

if __name__ == '__main__':
    n, m = map(int, input().split())
    for _ in range(n):
        for c in input().split():
            if c not in ['B', 'W', 'G']:
                print('#Color')
                sys.exit()

    print('#Black&White')
