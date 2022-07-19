def change(money):
    count = 0
    while money > 0:
        if money >= 10:
            money -= 10
        elif money >= 5:
            money -= 5
        else:
            money -= 1
        count += 1

    return count


def main():
    money = int(input())
    print(change(money))


if __name__ == '__main__':
    main()
