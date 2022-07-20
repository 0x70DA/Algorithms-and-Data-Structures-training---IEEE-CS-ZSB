'''HackerRank: CamelCase'''

def camelcase(s):
    count = 1
    for c in s:
        if c.isupper():
            count += 1
    
    return count

if __name__ == '__main__':
    s = input()
    result = camelcase(s)
    print(result)
