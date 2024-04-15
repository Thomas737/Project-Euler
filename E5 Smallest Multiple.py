from math import ceil

def get_all_divisors(value: int):
    divisors = []

    for n in range(2, ceil(value ** (1/2))+1):
        if value % n == 0:
            divisors += [n, int(value/n)]

    return divisors

actual = list(range(11, 21))

total = 1
for n in actual:
    total *= n

divisors = get_all_divisors(total)

for divisor in divisors:
    if all(n in get_all_divisors(divisor) for n in actual):
        print(divisor)