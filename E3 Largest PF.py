from math import ceil

actual = 600851475143
example = 12395

def find_divisors(value: int):
    if value == 2:
        return [value]

    for n in range(2, ceil(value ** (1/2))+1):
        if value % n == 0:
            return [n, int(value/n)]
    return [value]

def find_prime_factors(value: int):
    factors = find_divisors(value)

    if len(factors) == 1:
        return factors
    else:
        prime_factors = []
        for factor in find_divisors(value):
            prime_factors += find_prime_factors(factor)
        return prime_factors

def mul(array: list):
    total = 1
    for value in array:
        total *= value
    return total

print(find_prime_factors(actual))