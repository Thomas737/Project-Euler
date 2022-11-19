MULTS = [3, 5]
UP_TO = 1000

def multiples(mults: list, n: int):
    return clean_up([[divisor for mult in mults if not (divisor % mult)] for divisor in range(n)])

def clean_up(divisors: list):
    return [divisor[0] for divisor in divisors if len(divisor) > 0]

if __name__ == "__main__":
    print(sum(multiples(MULTS, UP_TO)))