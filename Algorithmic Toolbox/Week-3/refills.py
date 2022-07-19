from math import inf


def refills(location, stops, m, d):
    if location + m >= d:
        return 0

    if not stops or (stops[0] - location) > m:
        return inf

    last_stop = location
    while not stops and (stops[0] - location) <= m:
        last_stop = stops[0]
        del stops[0]

    return 1 + refills(last_stop, stops, m, d)


def main():
    d, m = map(int, input().split())
    stops = list(map(int, input().split()))
    location = 0
    print(refills(location, stops, m, d))


if __name__ == '__main__':
    main()
