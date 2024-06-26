import sys
def sum_of_multiples(limit):
    def sum_divisible_by(n):
        p = (limit - 1) // n
        return n * p * (p + 1) // 2
    return sum_divisible_by(3) + sum_divisible_by(5) - sum_divisible_by(15)
if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        n = int(input().strip())
        print(sum_of_multiples(n))