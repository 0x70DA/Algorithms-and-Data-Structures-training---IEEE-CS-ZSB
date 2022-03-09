'''HackerRank: Jabber ID'''
import re

if __name__ == '__main__':
    s = input()
    id_regex = re.compile(r'^\w{1,16}@(\w{1,16}\.)*\w{1,16}(/\w{1,16})?$')
    if id_regex.match(s):
        print('YES')
    else:
        print('NO')
