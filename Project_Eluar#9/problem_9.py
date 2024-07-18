def find_max_pythagorean_triplet_product(n):
    max_product = -1
    for a in range(1, n // 3):
        # Calculate b and c
        b = (n * (n - 2 * a)) // (2 * (n - a))
        c = n - a - b
        if a * a + b * b == c * c:
            product = a * b * c
            if product > max_product:
                max_product = product
    return max_product

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    t = int(data[0])
    results = []
    
    for i in range(1, t + 1):
        n = int(data[i])
        result = find_max_pythagorean_triplet_product(n)
        results.append(result)
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
