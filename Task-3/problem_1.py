'''HackerRank: Bus to Udayland'''

if __name__ == '__main__':
    n = int(input())
    rows = [input() for _ in range(n)]
    yes = False
    for i in range(n):
        if rows[i][:2] == 'OO':
            yes = True
            rows[i] = '++' + rows[i][2:]
            break
        elif rows[i][3:] == 'OO':
            yes = True
            rows[i] = rows[i][:3] + '++'
            break

    if yes:
        print('YES')
        print(*rows, sep='\n')
    else:
        print('NO')
