def multiples(mults: list, n: int):
    return sum([divisor for divisor in range(n) if (divisor % mult == 0 for mult in mults)])

if __name__ == "__main__":
    mults = [3, 5]
    up_to = 1000
    print(multiples(mults, up_to))