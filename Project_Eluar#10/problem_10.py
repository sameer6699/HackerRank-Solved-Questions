import sys
def sieve_of_eratosthenes(max_n):
    is_prime = [True] * (max_n + 1)
    p = 2
    while (p * p <= max_n):
        if is_prime[p]:
            for i in range(p * p, max_n + 1, p):
                is_prime[i] = False
        p += 1
    primes = []
    sum_primes = [0] * (max_n + 1)
    cumulative_sum = 0    
    for p in range(2, max_n + 1):
        if is_prime[p]:
            primes.append(p)
            cumulative_sum += p
        sum_primes[p] = cumulative_sum
    return sum_primes
input = sys.stdin.read
data = input().split()
t = int(data[0])
queries = [int(data[i]) for i in range(1, t + 1)]
max_query = max(queries)
sum_primes = sieve_of_eratosthenes(max_query)
for n in queries:
    print(sum_primes[n])