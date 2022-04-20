import random
import sys
import os

tests = int(sys.argv[1])
n = int(sys.argv[2])

for i in range(tests):
    print('Test #' + str(i))
    os.system('python generate.py ' + str(n) + ' ' + str(i) + ' > input.txt')
    os.system('python max_pairwise_naive.py < input.txt > max_pairwise_naive.txt')
    os.system('python max_pairwise_product.py < input.txt > max_pairwise_product.txt')

    with open('max_pairwise_naive.txt') as f:
        model = f.read()
    print('Model: ', model)
    with open('max_pairwise_product.txt') as f:
        main = f.read()
    print('Main: ', main)
    if model != main:
        break
