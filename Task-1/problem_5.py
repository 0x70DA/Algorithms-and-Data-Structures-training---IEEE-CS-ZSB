"""BeeCrowd: Fuel Spent"""

if __name__ == '__main__':
    time = int(input())
    speed = int(input())
    distance = speed * time
    fuel = distance / 12
    print(f"{fuel:.3f}")
