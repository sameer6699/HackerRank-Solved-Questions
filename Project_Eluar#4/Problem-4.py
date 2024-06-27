def is_palindrome(num):
    return str(num) == str(num)[::-1]
def largest_palindrome_less_than(N):
    max_palindrome = -1
    for i in range(999, 99, -1):
        for j in range(i, 99, -1):
            product = i * j
            if product < N and is_palindrome(product):
                max_palindrome = max(max_palindrome, product)
    return max_palindrome
if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()
    t = int(data[0].strip())
    results = []
    for a0 in range(1, t + 1):
        n = int(data[a0].strip())
        results.append(largest_palindrome_less_than(n))
    for result in results:
        print(result)