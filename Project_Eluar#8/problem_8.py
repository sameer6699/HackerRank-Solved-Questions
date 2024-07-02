def greatest_product(n, k, num):
    max_product = 0
    for i in range(n - k + 1):
        product = 1
        for j in range(k):
            product *= int(num[i + j])
        if product > max_product:
            max_product = product
    return max_product
import sys
t = int(input().strip())
for a0 in range(t):
    n, k = input().strip().split(' ')
    n, k = [int(n), int(k)]
    num = input().strip()
    print(greatest_product(n, k, num))