def maximum_loot(w, weights, cost):
    if w == 0 or not weights:
        return 0

    m = cost.index(max(cost))
    amount = min(weights[m], w)
    value = cost[m] * amount / weights[m]
    del cost[m], weights[m]
    return value + maximum_loot(w, weights, cost)


def main():
    w = int(input())
    weights = list(map(int, input().split()))
    cost = list(map(int, input().split()))
    print(maximum_loot(w, weights, cost))


if __name__ == '__main__':
    main()
