"""Generate a test for maximum pairwise product"""
import sys
import random

n = int(sys.argv[1])
myseed = int(sys.argv[2])
random.seed(myseed)

print(n)
print(' '.join([str(random.randint(1, 1000)) for _ in range(n)]))
