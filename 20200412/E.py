import math
import itertools
from functools import reduce

def gcd_list(numbers):
    return reduce(math.gcd, numbers)


n, k  = map(int,input().split())
l = list(itertools.combinations_with_replacement(range(k+1)[1:], n))
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
    
s %= (10**9 + 7)

print(s)

