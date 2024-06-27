#Project Euler #5: Smallest multiple
import sys
import math
from functools import reduce
def lcm(a, b):
    return a * b // math.gcd(a, b)
def lcm_of_list(numbers):
    return reduce(lcm, numbers)
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    if n == 1:
        print(1)
    else:
        print(lcm_of_list(range(1, n + 1)))