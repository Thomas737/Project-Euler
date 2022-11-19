N = 13195

def prime_gen(max: int):
    primes = [2, 3]
    while primes[-1] < max:
        for possible_prime in range(primes[-1] + 1, int(max) + 1):
            # Checks whether possible_prime is divisible by any prime
            if not any([possible_prime % prime == 0 for prime in primes]):
                primes.append(possible_prime)
    return primes

def divisibility(n: int, primes: list):
    largest_prime = 1
    for prime in primes:
        if (n % prime):
            largest_prime = max(largest_prime, prime)
    return largest_prime

if __name__ == "__main__":
    primes = prime_gen(N/2)
    print(divisibility(N, primes))
