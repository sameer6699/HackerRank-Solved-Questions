def sieve_of_eratosthenes(limit):
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False
    for start in range(2, int(limit**0.5) + 1):
        if sieve[start]:
            for multiple in range(start*start, limit + 1, start):
                sieve[multiple] = False
    primes = [num for num, is_prime in enumerate(sieve) if is_prime]
    return primes
def nth_prime(n):
    limit = 125000
    primes = sieve_of_eratosthenes(limit)
    return primes[n-1] 

import sys
t = int(input().strip())
test_cases = []
for a0 in range(t):
    n = int(input().strip())
    test_cases.append(n)
results = [nth_prime(n) for n in test_cases]
for result in results:
    print(result)
