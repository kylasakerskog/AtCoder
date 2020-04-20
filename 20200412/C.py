import math
import itertools
from functools import reduce

def gcd_list(numbers):
    return reduce(math.gcd, numbers)

k = int(input())
l = list(itertools.combinations_with_replacement(range(k+1)[1:], 3))
s = 0
n = 0

for i in l:
    x = len(set(i))
    if x == 3:
        n = 6
    elif x == 2:
        n = 3
    elif x == 1:
        n = 1
        
    s += gcd_list(list(i)) * n
    

print(s)

