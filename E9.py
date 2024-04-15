

def is_triplet(a: int, b: int):
    c = (a**2 + b**2) ** (1/2)
    if c == float(int(c)): return int(c)
    return False

def find_all_triplets(maximum):
    for a in range(1, maximum):
        for b in range(1, maximum):
            c = is_triplet(a, b)
            if c:
                if a + b + c == 1000:
                    return a * b * c

print(find_all_triplets(1000))