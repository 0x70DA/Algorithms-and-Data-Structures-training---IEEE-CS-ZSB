'''HackerRank: One-dimensional Japanese Crossword'''

if __name__ == '__main__':
    n = int(input())
    row = input()
    groups = []
    i = 0
    while i < n:
        if row[i] == 'B':
            count = 1
            j = i + 1
            while j < n:
                if row[j] == 'B':
                    count += 1
                elif row[j] == 'W':
                    break
                j += 1

            groups.append(count)
            i = j + 1
        else:
            i += 1

    print(len(groups))
    print(*groups)
