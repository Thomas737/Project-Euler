from math import ceil

def prime_gen(n_of_primes: int):
    primes = [2, 3, 5]

    while len(primes) < n_of_primes:
        counter = ceil(primes[-1]/2)*2+1
        while not is_prime(counter, primes):
            counter += 2
        primes.append(counter)
    
    return primes

def is_prime(value: int, primes: list[int]):
    max_prime = ceil(value**(1/2))+1

    for prime in primes:
        if prime < max_prime:
            if value % prime == 0:
                return False
        else:
            return True

print(prime_gen(10001))