'''HackerRank: Transmigration'''

if __name__ == '__main__':
    line = input().split()
    n, m, k = int(line[0]), int(line[1]), int(line[2][2:])
    skills = {}
    for _ in range(n):
        line = input().split()
        skills[line[0]] = int(line[1])

    new_skills = [input() for _ in range(m)]

    # Update old skills
    count = 0
    delete = []
    for key, value in skills.items():
        value = int(k * value / 100)
        if value < 100:
            delete.append(key)
        else:
            skills[key] = value
            count += 1

    for key in delete:
        del skills[key]

    for skill in new_skills:
        if skill not in skills.keys():
            skills[skill] = 0
            count += 1

    skills = dict(sorted(skills.items()))

    print(count)
    for key, value in skills.items():
        print(key, value, sep=' ')
