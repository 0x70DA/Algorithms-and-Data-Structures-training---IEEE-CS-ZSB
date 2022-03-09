'''HackerRank: Counting Sticks'''


def counting_sticks(a, b, c):
    if len(c) == len(a) + len(b):
        print(f"{a}+{b}={c}")
    elif len(c) - len(a) - len(b) == 2:
        c = c[:-1]
        a += '|'
        print(f"{a}+{b}={c}")
    elif len(c) - len(a) - len(b) == -2:
        if len(a) > len(b):
            a = a[:-1]
        else:
            b = b[:-1]
        c += '|'
        print(f"{a}+{b}={c}")
    else:
        print('Impossible')


if __name__ == '__main__':
    s = input()
    plus = s.index('+')
    equals = s.index('=')
    a = s[:plus]
    b = s[plus+1:equals]
    c = s[equals+1:]

    counting_sticks(a, b, c)
