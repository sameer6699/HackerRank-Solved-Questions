#project Eluar 
def max_pythagorean_triplet_product(n):
    max_product = -1
    for a in range(1, n // 3):
        for b in range(a + 1, n // 2):
            c = n - a - b
            if a * a + b * b == c * c:
                product = a * b * c
                if product > max_product:
                    max_product = product
    return max_product
import sys
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(max_pythagorean_triplet_product(n))
    