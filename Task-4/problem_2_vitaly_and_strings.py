'''HackerRank: Vitaly and Strings'''


if __name__ == '__main__':
    s, t = input(), input()
    s = list(s)
    for i in range(len(s)-1, -1, -1):
        if s[i] != "z":
            s[i] = chr(ord(s[i])+1)
            break
        else:
            s[i] = "a"
    s = ''.join(s)
    if s == t:
        print("No such string")
    else:
        print(s)
