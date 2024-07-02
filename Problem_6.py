#!/bin/python3
import sys
def sum_square_difference(n):
    sum_of_squares = sum(i ** 2 for i in range(1, n + 1))
    square_of_sum = sum(range(1, n + 1)) ** 2
    return abs(sum_of_squares - square_of_sum)
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(sum_square_difference(n))