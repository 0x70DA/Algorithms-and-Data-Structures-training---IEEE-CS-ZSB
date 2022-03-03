'''HackerRank: Colorful Stones (Simplified Edition)'''

if __name__ == '__main__':
    s, t = input(), input()
    pos = 0
    for c in t:
        if c == s[pos]:
            pos += 1

    print(pos + 1)
