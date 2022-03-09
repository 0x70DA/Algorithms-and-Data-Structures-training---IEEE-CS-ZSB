'''HackerRank: BerOS file system'''

if __name__ == '__main__':
    path = input()
    normalized = '/'
    for i in range(len(path)):
        if path[i] != '/' or (path[i] == '/' and normalized[-1] != '/'):
            normalized += path[i]

    if len(normalized) > 1 and normalized[-1] == '/':
        print(normalized[:-1])
    else:
        print(normalized)
