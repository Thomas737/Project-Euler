MAX = 4000000

def fibonacci(max: int):
    sequence = [1, 2]
    while sequence[-1] < max:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

def even_only(sequence: list):
    return [n for n in sequence if not (n % 2)]

if __name__ == "__main__":
    sequence = fibonacci(MAX)
    print(sum(even_only(sequence)))
