# Even Fibonacci numbers
import sys
def sum_of_even_fibonacci(limit):
    a, b = 1, 2
    sum_even = 0
    while a <= limit:
        if a % 2 == 0:
            sum_even += a
        a, b = b, a + b
    return sum_even
if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        n = int(input().strip())
        print(sum_of_even_fibonacci(n))