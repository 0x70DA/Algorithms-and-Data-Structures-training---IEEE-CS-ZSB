'''HackerRank: Weighted Uniform Strings'''


def get_weights(s):
    weights = set()
    rep = 1
    for i in range(len(s)):
        if i+1 < len(s) and s[i+1] == s[i]:
            rep += 1
        else:
            rep = 1

        weights.add((ord(s[i])-96) * rep)

    return weights


def main():
    s = input()
    weights = get_weights(s)
    for _ in range(int(input())):
        print("Yes" if int(input()) in weights else "No")


if __name__ == '__main__':
    main()
