'''HackerRank: Sereja and Dima'''

if __name__ == '__main__':
    n = int(input())
    cards = list(map(int, input().split()))
    s, d = 0, 0
    while len(cards) > 0:
        s += cards.pop(0) if cards[0] > cards[-1] else cards.pop(-1)
        if len(cards) == 0:
            break
        d += cards.pop(0) if cards[0] > cards[-1] else cards.pop(-1)

    print(s, d, sep=' ')
